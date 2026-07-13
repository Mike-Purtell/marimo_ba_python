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


@app.cell
def _(mo):
    simple_slider = mo.ui.slider(1, 10, 1)
    simple_slider
    return


@app.cell
def _(mo):
    better_slider = mo.ui.slider(1, 10, 1, label = 'better slider')
    better_slider
    return


@app.cell
def _(mo):
    best_slider = mo.ui.slider(1, 100, 1, label = 'best slider', value = 25)
    return (best_slider,)


@app.cell
def _(best_slider, mo):
    mo.md(f"""
    {best_slider} value: {best_slider.value}
    """)
    return


@app.cell
def _(best_slider, mo):

    # print(' x'*best_slider.value)
    mo.md('\U0001F530  '*best_slider.value)
    return


app._unparsable_cell(
    r"""
    mo.md(f'best slider value: best_slider.value}')
    """,
    name="_"
)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
