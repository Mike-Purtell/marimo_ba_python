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
    x = 22
    return (x,)


@app.cell
def _(x):
    print(f'{x = }')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _(mo, x):
    mo.md(f'''# Marimo Reactivity Demo
    x = {x}
    ''')
    return


@app.cell
def _():
    # x = 10
    return


if __name__ == "__main__":
    app.run()
