# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastexcel==0.20.2",
#     "marimo>=0.23.16",
#     "matplotlib==3.11.1",
#     "plotly==6.9.0",
#     "polars==1.43.2",
# ]
# ///

import marimo

__generated_with = "0.23.16"
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
    import plotly.graph_objects as go

    return go, pl, px


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
    return (df_cal,)


@app.cell
def _(mo):
    demo = mo.ui.radio(
        options=['Population', 'Population Density', 'Area'], 
        value="Population", 
        label='',  # choose a statistic:',
        inline =  True   # Make them appear side-by-side
    )
    return (demo,)


@app.cell
def _(demo):
    demo_view = demo.value if demo.value else None
    return (demo_view,)


@app.cell
def _(demo_view, df_cal, go, mo, px):
    print(f'display top 10 and bottom 10 charts by county {demo_view}')
    fig1 = fig2 = go.Figure()

    if demo_view == 'Population':
        fig1 = px.bar(
            df_cal.sort('Pop_Rank', descending=True).tail(10),
            x='Pop',
            y='County', 
            title = f'Top 10',subtitle = demo_view,
            labels={'Pop': 'Population'}
        )
        fig2 = px.bar(
            df_cal.sort('Pop_Rank', descending=True).head(10),
            x='Pop',
            y='County',
            title = f'Bottom 10', subtitle = demo_view,
            labels={'Pop': 'Population'}
        )

    if demo_view == 'Population Density':
        fig1 = px.bar(
            df_cal.sort('Pop_Density_Sq_Mile', descending=False).tail(10),
            x='Pop_Density_Sq_Mile',
            y='County', 
            title = f'Top 10',subtitle = demo_view,
            labels={'Pop_Density_Sq_Mile': 'Population per Square Mile'}
        )
        fig2 = px.bar(
            df_cal.sort('Pop_Density_Sq_Mile', descending=False).head(10),
            x='Pop_Density_Sq_Mile',
            y='County',
            title = f'Bottom 10', subtitle = demo_view,
            labels={'Pop_Density_Sq_Mile': 'Population per Square Mile'}
        )

    if demo_view == 'Area':
        fig1 = px.bar(
            df_cal.sort('Area_Sq_Mile', descending=False).tail(10),
            x='Area_Sq_Mile',
            y='County', 
            title = f'Top 10',subtitle = demo_view,
            labels={'Area_Sq_Mile': 'Area (Square Miles)'}
        )
        fig2 = px.bar(
            df_cal.sort('Area_Sq_Mile', descending=False).head(10),
            x='Area_Sq_Mile',
            y='County',
            title = f'Bottom 10', subtitle = demo_view,
            labels={'Area_Sq_Mile': 'Area (Square Miles)'}
        )

    # Update layout to set custom height and width, offset y-labels from bars
    h = 400
    w = 400
    fig1.update_layout(width=w, height=h, yaxis=dict(ticklabelstandoff=10))
    fig2.update_layout(width=w, height=h, yaxis=dict(ticklabelstandoff=10))
    for fig in (fig1, fig2):
        fig.update_layout(clickmode='event+select')
        fig.update_traces(
            selected=dict(marker=dict(color='green')),
        )

    # Wrap figures in mo.ui.plotly so a selected bar can update the info block.
    fig1_ui = mo.ui.plotly(fig1)
    fig2_ui = mo.ui.plotly(fig2)
    return fig1_ui, fig2_ui


@app.cell
def _(mo):
    get_selected_county, set_selected_county = mo.state(None)
    return get_selected_county, set_selected_county


@app.cell
def _(fig1_ui, fig2_ui, set_selected_county):
    selected_points = fig1_ui.points + fig2_ui.points
    if selected_points:
        set_selected_county(selected_points[0].get('y'))
    return


@app.cell
def _(df_cal, get_selected_county, mo, pl):
    selected_county = get_selected_county()
    selected_county_row = (
        df_cal.filter(pl.col('County') == selected_county).row(0, named=True)
        if selected_county
        else None
    )
    if selected_county_row:
        county_info = mo.Html(
            f"""
            <div style='padding: 0.75rem 1rem; border: 1px solid var(--border-color);'>
                <strong>{selected_county_row['County']}</strong><br>
                Formation: {selected_county_row['Formation']}<br>
                Etymology: {selected_county_row['Etymology']}
            </div>
            """
        )
    else:
        county_info = mo.Html('')
    return (county_info,)


@app.cell
def _(county_info, demo, demo_view, description, df_cal, fig1_ui, fig2_ui, mo):

    dataframe_info = '''
        SHOW ME: This polars dataframe is used for all visualizations in this 
        notebook. Use the Transform block to interactively process a dataframe with a GUI, 
        no coding required. When you're done, you can copy the code that the GUI 
        generated for you and paste it into your notebook.
    '''
    layout = mo.vstack([
        mo.Html(dataframe_info),
        mo.ui.dataframe(df_cal),
        mo.Html('<br>'),
        mo.left(demo),
        mo.Html('<br>'),
        mo.left(mo.Html(f' <h1>California County {demo_view}</h1>')),
        mo.Html('<br>'),
        mo.Html(description),
        county_info,
        mo.hstack([fig1_ui, fig2_ui], widths='equal'),
    ])
    return (layout,)


@app.cell
def _(demo_view):
    description = ''
    if demo_view == 'Population':
        description = (
            '''
            California’s 58 counties span the widest population extremes of any 
            state in the country. Los Angeles County dominates the high end, while 
            Alpine County anchors the low end, and the spread between them is 
            nearly 10 million people.
    '''
        )
    elif demo_view == 'Population Density':
        description = (
            '''
            California’s county population density ranges from hyper‑urban to 
            frontier‑level sparse, with a spread of nearly 18,000 people per square mile 
            between the top and bottom. The single most important fact: San Francisco 
            County is by far the densest, while Inyo, Alpine, and Modoc anchor the lowest 
            end at ~2 people per square mile.
            '''
        )
    elif demo_view == 'Area':
        description = (
            '''
            California’s counties span one of the widest area ranges of any state. The
            largest county in the contiguos United States (San Bernardino) is larger than
            9 other states, including New Jersey and Massachusetts. The smallest county in
            California is San Francisco, which also has the largest population density in
            our state.  California’s county areas reflect our mix of
            vast deserts, mountain regions, and compact urban cores.
            '''
        )
    return (description,)


@app.cell
def _(layout):
    layout
    return


if __name__ == "__main__":
    app.run()
