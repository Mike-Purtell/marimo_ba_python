# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.16",
# ]
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.Html(
        '''
        <span><p style="font-size: 24px;">Marimo Notebook</p></span><br>
        This notebook was created with Marimo's tool to convert jupyter to marimo. Will 
        show advantages and limitations of reactivity. 
        <br>
        the syntax for converting jupyter notebook to a marimo notebook is:
        <br><br>
        <span><i><p style="text-align: center;">marimo convert your_notebook.ipynb -o your_notebook.py</p></i></span><br>
        '''
    )
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.Html(
        '''
        <span><p style="font-size: 24px;">Reactivity has restrictions</p></span><br>
        </p>The jupyter notebook had two cells that initialized x. This it not 
        allowed in marimo. If two cells both define the same global variable (in this case 
        x), marimo cannot guarantee which definition will be used when a third cell reads 
        it — the output would depend on the order in which the defining cells run. This 
        could lead to:<br>
    <h2>My Ordered List</h2>
    <ol type="1">
    <li>Hidden state (unknown which value is active)</li>
    <li>Hidden bugs (unexpected behavior when rerunning)</li>
    <li>Non-reproducible results (over 96% of Jupyter notebooks on GitHub fail reproducibility tests) docs.marimo.io.</li>
    </ol>
    '''
    )
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
