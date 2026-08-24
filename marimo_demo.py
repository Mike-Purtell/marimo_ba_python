import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo


    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Reactivity Demo
    """)
    return


@app.cell
def _():
    x = 1
    print(f'{x = }')
    return (x,)


@app.cell
def _():
    y = 10
    print(f'{y = }')
    return (y,)


@app.cell
def _(x, y):
    z = x + y
    print(f'{z = }')
    return (z,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _(mo, z):
    mo.md(f'''# Marimo Reactivity Demo
    z = {z}
    ''')
    return


@app.cell
def _():
    _z = 778

    return


if __name__ == "__main__":
    app.run()
