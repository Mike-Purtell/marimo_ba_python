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


@app.cell
def _():
    return


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Here are a few more Marimo widgets (out of many)
    """)
    return


@app.cell
def _(mo):
    form = (
        mo.md(
            '''
        **Enter your prompt.**

        {prompt}

        **Choose a random seed.**

        {seed}
        '''
        )
        .batch(
            prompt=mo.ui.text_area(),
            seed=mo.ui.number(),
        )
        .form()
    )
    return (form,)


@app.cell
def _(form):
    form
    return


@app.cell
def _(form):
    form.value
    return


@app.cell
def _(mo):
    checkbox = mo.ui.checkbox(label="yes I read the T's and C's")
    return (checkbox,)


@app.cell
def _(checkbox):
    checkbox.value
    return


@app.cell
def _(checkbox):
    checkbox
    return


@app.cell
def _(mo):
    multiselect = mo.ui.multiselect(
        options=['Chicago', 'New York', 'Detroit', 'Springfield'], 
        label='pick your favorite town',
        max_selections=2 # Optional, None for no limit, integer for specific limit'
    )
    return (multiselect,)


@app.cell
def _(multiselect):
    multiselect.value
    return


@app.cell
def _(multiselect):
    multiselect
    return


@app.cell
def _(mo):
    radio = mo.ui.radio(
        options=sorted([
                'Green Day', 'Jefferson Airplane',  'Metallica', 'Grateful Dead', 
                'Santana','Journey', 'Petrichor'
        ]),
        label='Your favorite bay area band'
    )
    return (radio,)


@app.cell
def _(radio):
    radio
    return


@app.cell
def _(radio):
    radio.value
    return


@app.cell
def _(checkbox, mo, multiselect, radio):
    marimo_ui_dictionary = mo.ui.dictionary(
        {
            'checkbox': checkbox,
            'multiselect': multiselect,
            'radio': radio,
        }
    )
    return (marimo_ui_dictionary,)


@app.cell
def _(marimo_ui_dictionary):
    marimo_ui_dictionary
    return


@app.cell
def _(mo):
    diagram = '''
    graph LR
        A[Square Rect] -- Link text --> B((Circle))
        A --> C(Round Rect)
        B --> D{Rhombus}
        C --> D
    '''
    mo.mermaid(diagram)

    mo.mermaid(
        diagram,
        theme="base",
        theme_variables={
            "primaryColor": "#E8EEF5",
            "primaryTextColor": "#1F2937",
            "primaryBorderColor": "#64748B",
            "lineColor": "#475569",
            "tertiaryColor": "#F8FAFC",
        },
    )
    return


@app.cell
def _(mo):
    mo.mermaid(
    	"graph TD\n" +
    	"A[Christmas] -->|Get money| B(Go shopping)\n" +
    	"B --> C{Think}\n" + 
    	"C -->|One| D[Laptop]\n" +   
    	"C -->|Two| E[iPhone]\n" +
    	"C -->|Three| F[Car]"
    )
    return


if __name__ == "__main__":
    app.run()
