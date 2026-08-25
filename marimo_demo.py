# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.24.0",
# ]
# ///

import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", layout_file="layouts/marimo_demo.slides.json")


@app.cell
def _():
    import marimo as mo
    from math import sqrt


    return mo, sqrt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### quadratic coefficients
    """)
    return


@app.cell
def _():
    a = 1
    b = -4
    c = 4
    return a, b, c


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Discriminant
    """)
    return


@app.cell
def _(a, b, c):
    d = b**2 - (4 * a * c)
    return (d,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Count the roots
    """)
    return


@app.cell
def _(d):
    has_no_roots = (d < 0)
    has_one_root = (d == 0)
    has_two_roots = (d > 0)
    return has_no_roots, has_one_root, has_two_roots


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Show the results
    """)
    return


@app.cell
def _(a, b, c, d, has_no_roots, has_one_root, has_two_roots, mo, sqrt):
    result_string = ''
    root = 0
    root1 = 0
    root2 = 0

    if has_no_roots:
        result_string = 'No Roots'

    if has_one_root:
        root = -b / (2 * a)
        result_string = f'One root, x = {root:.3f}'
    elif has_two_roots:
        root1 = (-b + sqrt(d)) / (2 * a)
        root2 = (-b - sqrt(d)) / (2 * a)
        if root1 > root2:
            root1, root2 = root2, root1
        result_string = f'Two roots:<br> x1 = {root1:.3f}<br> x2 = {root2:.3f}'

    mo.md(
        f'{a = }<br>'
        f'{b = }<br>'
        f'{c = }<br>'
        f'{d = }<br>'
        f'{result_string}<br>'
    )
    return


if __name__ == "__main__":
    app.run()
