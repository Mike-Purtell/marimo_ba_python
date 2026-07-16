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
    This brief notebook showcases marimo dataframe displays
    """)
    return


@app.cell
def _():
    import polars as pl
    import pandas as pd

    print(f'Polars version {pl.__version__}')
    print(f'Pandas version {pd.__version__}')
    return pd, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Hello World of dataframes
    Multiplication tables are often the first structured table people learn
    """)
    return


@app.cell
def _(pd):
    df_pandas = (
        pd.DataFrame({str(i): [j * i for j in range(11)] for i in range(11)}, dtype='uint8')
    )
    df_pandas # displays columns, index. No data types or dataframe shape
    return (df_pandas,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Dataframe displays in Jupyter
    The Pandas DataFrame above doesn’t display its datatypes or shape. The Polars DataFrame below includes both. Each DataFrame is simply a different representation of the same experimental data.
    """)
    return


@app.cell
def _(df_pandas, pl):
    df_polars =  pl.from_pandas(df_pandas)
    df_polars 
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
