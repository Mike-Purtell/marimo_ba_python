import marimo

__generated_with = "0.23.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Marimo Notebook
    this notebook was created using Marimo's built into tool that coverts jupyter to
    marimo to show advantages and limitations of reactivity
    """)
    return


@app.cell
def _():
    import polars as pl
    import pandas as pd

    print(f'Polars version {pl.__version__}')
    print(f'Pandas version {pd.__version__}')
    return


@app.cell
def _():
    # declare X, assign value of 1
    x = 1
    print(f'{x = }')
    return


@app.cell
def _():
    # declare x, assign value of 3
    x_1 = 3
    print(f'x = {x_1}')
    return (x_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What is x?
    The 2nd block, x was changed to x_1 by the marimo notebook converter.
    It even changed the f-string (correctly)
    If declared as x the reactivity model would break.
    """)
    return


@app.cell
def _(x_1):
    print(f'x = {x_1}')
    return


if __name__ == "__main__":
    app.run()
