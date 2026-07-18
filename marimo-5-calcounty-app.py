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

    return cs, pl


@app.cell
def _(cs, pl):
    target_columns = [
        'County',
        'A', '2020-POP', '2021-POP', '2022-POP', '2023-POP', '2024-POP', '2025-POP',
        'B', '2020-RANK', '2021-RANK', '2022-RANK', '2023-RANK', '2024-RANK', '2025-RANK',
    ]

    df_statewide = (
        pl.read_excel(
            'co-est2025-chg-06.xlsx',
            read_options={"skip_rows": 4, "n_rows": 59}
        )
        .pipe(
            lambda d: d.select(d.columns[:15]).rename(
                dict(zip(d.columns[:15], target_columns, strict=False))
            )
        )
        .drop(['A', 'B'])
        .filter(pl.col('County') != 'California')  # skip statewide tallies
        .with_columns(
            pl.col('County')
                .str.replace(' County, California','')
                .str.slice(1, None),
            cs.contains('RANK').cast(pl.UInt8), # Rank out of 589 counties
            cs.contains('POP').cast(pl.UInt32), # LA County 10M+ residents
        )
    )
    df_statewide
    return (df_statewide,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Select a County
    California has 58 Counties. Least populous is Alpine County, most populous is Los Angeles County. See for your self by sorting on any dataframe column using Marimo dataframe interface.
    """)
    return


@app.cell
def _(df_statewide, mo, pl):
    county_select = mo.ui.multiselect(
        df_statewide.select(pl.col('County')).to_series().to_list(),
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
def _(county, df_statewide, pl):
    df_county = (
        df_statewide.filter(pl.col('County') == county)
        .transpose(
            header_name='Year-Stat',
            include_header=True
        )
        .filter(pl.col('Year-Stat') != 'County')
        .select(
            Year = pl.col('Year-Stat').str.split('-').list.first().cast(pl.UInt16),
            Stat_Name = pl.col('Year-Stat').str.split('-').list.last(),
            Stat_Value = pl.col('column_0')
        )
        .pivot(columns='Stat_Name', values='Stat_Value')
        .with_columns(
            pl.col('POP').cast(pl.UInt32),
            pl.col('RANK').cast(pl.UInt8)
        )
        

        #df.pivot(index="foo", columns="bar", values="baz", aggregate_function="sum")
    
        # .unstack(
        #     columns('Stat_Name')
        # )
        # .group_by('Stat_Name').agg(pl.len())
    )
    return (df_county,)


@app.cell
def _(df_county):
    df_county
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
