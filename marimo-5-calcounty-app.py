import marimo

__generated_with = "0.23.14"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Marimo Notebook
    This notebook showcases datavisualization with Marimo
    """)
    return


@app.cell
def _():
    import polars as pl
    import polars.selectors as cs
    print(f'Polars version {pl.__version__}')
    import plotly.express as px
    # For choropleth map
    import json
    from urllib.request import urlopen

    return json, pl, px, urlopen


@app.cell
def _(pl):
    df_cal = (
        pl.read_excel('assets/california_counties_wikipedia.xlsx')
        .lazy()
        .with_columns(
            # Normalize to CA county FIPS format (06001, 06013, ...)
            pl.concat_str([
                pl.lit('06'),
                pl.col('FIPS').cast(pl.Int64).cast(pl.String).str.zfill(3)
            ]).alias('FIPS'),
            pl.col('Established').cast(pl.UInt16),
            pl.col('Pop').cast(pl.UInt32),
            pl.col('Area_Sq_Mile').cast(pl.UInt16), 
            pl.col('Area_Sq_KM').cast(pl.UInt16),
            pl.col('County').str.strip_chars()
        )
        .with_columns(
            Pop_Density_Sq_Mile = 
                (pl.col('Pop')/pl.col('Area_Sq_Mile'))
                .round(1),
            Pop_Density_Sq_KM = (pl.col('Pop')/pl.col('Area_Sq_KM')).round(1)
        )
        .with_columns(
            Pop_Rank = pl.col('Pop').rank(method='min', descending=True),
            Pop_Density_Rank = pl.col('Pop_Density_Sq_Mile')
                                .rank(method='min', descending=True),
            Area_Rank = pl.col('Area_Sq_Mile').rank(method='min', descending=True),        
        )
        .sort('County', descending=False)
        .select([
            'County', 'Seat', 'Established', 
            'Pop',  'Pop_Rank', 
            'Area_Sq_Mile', 'Area_Sq_KM', 'Area_Rank',
            'Pop_Density_Sq_Mile', 'Pop_Density_Sq_KM', 'Pop_Density_Rank',   
            'Formation', 'Etymology', 'FIPS',
        ])
        .collect()
    )
    print(list(df_cal.columns))
    df_cal
    return (df_cal,)


@app.cell
def _(df_cal):
    print(f"{df_cal.get_column('Pop').sum() = :,}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Select a County
    California has 58 Counties. Least populous is Alpine County, most populous is Los Angeles County. See for your self by sorting on any dataframe column using Marimo dataframe interface.
    """)
    return


@app.cell
def _(df_cal, mo, pl):
    county_select = mo.ui.multiselect(
        df_cal.select(pl.col('County')).to_series().to_list(),
        max_selections=1,
        full_width=True,
    )
    return (county_select,)


@app.cell
def _(county_select, mo):
    mo.center(county_select)
    return


@app.cell
def _(county_select):
    county = county_select.value[0] if county_select.value else None
    return (county,)


@app.cell
def _(county):
    county
    return


@app.cell
def _():
    ### Marimo with Plotly
    return


@app.cell
def _(df_cal, json, pl, px, urlopen):
    # Load US counties GeoJSON (includes FIPS codes)
    with urlopen("https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json") as response:
        counties = json.load(response)

    # Filter GeoJSON to only CA counties (STATE FIPS = "06")
    ca_features = [f for f in counties["features"] if f["properties"]["STATE"] == "06"]
    df_ca = pl.DataFrame({
        'County': [f['properties']['NAME'] for f in ca_features],
        'FIPS': [f['id'] for f in ca_features]
    })
    matched_fips = set(df_cal.get_column('FIPS').to_list()) & set(df_ca.get_column('FIPS').to_list())
    print(f'FIPS matched for map: {len(matched_fips)} / {len(ca_features)} CA counties')

    # Choropleth payload can be very heavy in marimo app mode; plot county centroids
    # instead so the map reliably renders in all browsers.
    def _extract_lon_lat(geometry):
        geom_type = geometry['type']
        coords = geometry['coordinates']
        if geom_type == 'Polygon':
            ring = coords[0]
        else:
            ring = coords[0][0]
        lon = sum(pt[0] for pt in ring) / len(ring)
        lat = sum(pt[1] for pt in ring) / len(ring)
        return lon, lat

    centroids = [_extract_lon_lat(f['geometry']) for f in ca_features]
    df_centroids = pl.DataFrame({
        'FIPS': [f['id'] for f in ca_features],
        'lon': [c[0] for c in centroids],
        'lat': [c[1] for c in centroids],
    })
    df_map = df_cal.join(df_centroids, on='FIPS', how='left')

    fig = px.scatter(
        df_map.to_pandas(),
        x='lon',
        y='lat',
        color='Pop',
        size='Pop',
        hover_name='County',
        hover_data={'FIPS': True, 'lat': ':.3f', 'lon': ':.3f'},
        size_max=30,
        title='CA County Map',
        color_continuous_scale='Blues',
    )
    fig.update_traces(marker_line_color='white', marker_line_width=0.6, opacity=0.9)
    fig.update_layout(
        template='plotly_white',
        coloraxis_showscale=False,
        title_font_size=24,
        title_font_color='gray',
        height=600,
        margin={"r":50,"t":50,"l":0,"b":0},
        paper_bgcolor='white',
        plot_bgcolor='white',
    )
    fig.update_xaxes(title='Longitude', showgrid=True, gridcolor='lightgray')
    fig.update_yaxes(
        title='Latitude',
        showgrid=True,
        gridcolor='lightgray',
        scaleanchor='x',
        scaleratio=1,
    )
    # fig.update_traces(
    #     hovertemplate= (
    #     '<b>County: %{customdata[0]}</b><br>' +
    #     'Total: %{customdata[1]:,}<br>' +
    #     'Active: %{customdata[2]:,}<br>' +
    #     '% Active: %{customdata[3]:.2f}%' +
    #     '<extra></extra>'
    #     )
    # )
    fig
    return (fig,)


@app.cell
def _(fig, mo):
    plot = mo.ui.plotly(fig)
    plot
    return (plot,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Marimo with Plotly
    """)
    return


if __name__ == "__main__":
    app.run()
