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
    this notebook was created using Marimo's built into tool that coverts jupyter to
    marimo to show advantages and limitations of reactivity
    """)
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
    # x = 3
    # print(f'x = {x}')
    x_1 = 3
    print(f'x_1 = {x_1}')
    return (x_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What is x?
    Marimo will not allow you to assign values to 'x' in 2 different cells. This breaks the reactivity. When this notebook was produced by Marimo's Jupyter converter tool, it renamed x to x_1 for the second instance of x.

    Notice the error when x is initialized in 2 different cells. No problem is x is assigned twice in the same cell.
    """)
    return


@app.cell
def _(x_1):
    print(f'x_1 = {x_1}')
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
    slider_max = 20
    best_slider = mo.ui.slider(
        1, slider_max, 1, label = 'best slider', value = 10
    )
    return best_slider, slider_max


@app.cell
def _(best_slider, mo):
    mo.md(f"""
    {best_slider} value: {best_slider.value}
    """)
    return


@app.cell
def _(best_slider, mo):
    mo.md('🐱' * best_slider.value)

    return


@app.cell
def _(best_slider, mo, slider_max):
    mo.md('🐶 ' * (1 + slider_max - best_slider.value))
    return


if __name__ == "__main__":
    app.run()
