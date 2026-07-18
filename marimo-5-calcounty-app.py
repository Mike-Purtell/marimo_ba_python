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

    return (pl,)


@app.cell
def _(pl):
    df_cal = (
        pl.read_excel('assets/california_counties_wikipedia.xlsx')
        .lazy()
        .with_columns(
            pl.col('FIPS').cast(pl.UInt8),
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
        .sort('Pop', descending=True)
        .with_row_index(name='Pop_Rank', offset=1)
        .sort('Pop_Density_Sq_Mile', descending=True)
        .with_row_index(name='Pop_Density_Rank', offset=1)
        .sort('Area_Sq_Mile', descending=True)
        .with_row_index(name='Area_Rank', offset=1)
        .sort('County', descending=False)
        .select([
            'County', 'FIPS', 'Seat', 'Established', 
            'Pop',  'Pop_Rank', 
            'Area_Sq_Mile', 'Area_Sq_KM', 'Area_Rank',
            'Pop_Density_Sq_Mile', 'Pop_Density_Sq_KM', 'Pop_Density_Rank',   
            'Formation', 'Etymology'
        ])
        .collect()
    )
    print(list(df_cal.columns))
    df_cal
    return (df_cal,)


@app.cell
def _(df_cal):
    print(f'{df_cal.get_column('Pop').sum() = :,}')


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Marimo with Plotly
    Jupyter does not provide built-in data visualization tools.
    Libraries like Plotly, Matplotlib, Altair or others are required.
    """)
    return


if __name__ == "__main__":
    app.run()
