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
    import matplotlib.pyplot as plt
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
    ### Select a Data Viz parameter
    California has 58 Counties. Pick one of 3 demographics to be displayed in top 10 and bottom 10 horizontal bar charts
    """)
    return


@app.cell
def _(mo):
    demo = mo.ui.multiselect(
        ['Population', 'Population Density', 'Area'],
        max_selections=1,
        full_width=True,
    )
    return (demo,)


@app.cell
def _(demo, mo):
    mo.center(demo)
    return


@app.cell
def _(demo):
    demo_view = demo.value[0] if demo.value else None
    return (demo_view,)


@app.cell
def _(demo_view):
    demo_view
    return


@app.cell
def _():
    ### Marimo with Plotly
    return


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
        )
        fig2 = px.bar(
            df_cal.sort('Pop_Rank', descending=True).head(10),
            x='Pop',
            y='County',
            title = f'Bottom 10', subtitle = demo_view,
        )

    if demo_view == 'Population Density':
        fig1 = px.bar(
            df_cal.sort('Pop_Density_Sq_Mile', descending=False).tail(10),
            x='Pop_Density_Sq_Mile',
            y='County', 
            title = f'Top 10',subtitle = demo_view,
        )
        fig2 = px.bar(
            df_cal.sort('Pop_Density_Sq_Mile', descending=False).head(10),
            x='Pop_Density_Sq_Mile',
            y='County',
            title = f'Bottom 10', subtitle = demo_view,
        )

    if demo_view == 'Area':
        fig1 = px.bar(
            df_cal.sort('Area_Sq_Mile', descending=False).tail(10),
            x='Area_Sq_Mile',
            y='County', 
            title = f'Top 10',subtitle = demo_view,
        )
        fig2 = px.bar(
            df_cal.sort('Area_Sq_Mile', descending=False).head(10),
            x='Area_Sq_Mile',
            y='County',
            title = f'Bottom 10', subtitle = demo_view,
        )
    # Update layout to set custom height and width, offset y-labels from bars
    w = 400
    h = 400
    fig1.update_layout(width=w, height=h, yaxis=dict(ticklabelstandoff=10))
    fig2.update_layout(width=w, height=h, yaxis=dict(ticklabelstandoff=10))

    # Wrap figures in mo.ui.plotly for reactive support
    fig1_ui = mo.ui.plotly(fig1)
    fig2_ui = mo.ui.plotly(fig2)
    # Arrange them side‑by‑side in an HStack
    layout = mo.hstack(
        [fig1_ui, fig2_ui],
        widths="equal"  # Equal width for both
    )

    # Display the layout
    layout
    return


if __name__ == "__main__":
    app.run()