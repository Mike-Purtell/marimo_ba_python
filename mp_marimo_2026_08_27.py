# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastexcel==0.20.2",
#     "marimo>=0.23.16",
#     "numpy==2.5.2",
#     "plotly[express]==6.9.0",
#     "polars==1.43.2",
# ]
# ///

# Copyright 2024 Marimo. All rights reserved.

import marimo

__generated_with = "0.23.16"
app = marimo.App(layout_file="layouts/mp_marimo_2026_08_27.slides.json")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import numpy

    return


@app.cell
def _():
    import polars as pl
    import plotly.express as px
    import plotly.graph_objects as go

    return go, pl, px


@app.cell
def _(mo):
    mo.vstack([
        mo.Html("""
        <style>
            html, body, body * {
                font-family: Arial, Helvetica, sans-serif !important;
            }

            button, input, select, textarea {
                font-family: Arial, Helvetica, sans-serif !important;
            }
        </style>
        """),
        mo.md("# Welcome to marimo! 🌊🍃"),
        mo.md("## Mike Purtell"),
        mo.md("### Bay Area Python Interest Group"),
        mo.md("### August 27, 2026")
    ])
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md("# Introduction and Overview"),
        mo.md("marimo resembles jupyter (vertically arranged blocks, code or markup)"),
        mo.hstack([
            mo.accordion(
                {
                    "jupyter": mo.md(
                        """
                        - great for exploration
                        - beware of:
                            - hidden state
                            - manual reruns
                            - hard-to-review file formats, Git Issues
                            - top down flow for run-all, arbitrary flow otherwise
                        """
                    )
                }
            ),
            mo.accordion(
                {
                    "marimo": mo.md(
                        """
                        - reactivity: change value in 1 cell updates the dependent cells
                        - think of Excel
                        - natural mechanism for callbacks
                        - great for dashboards
                        - easy to deploy on molab
                        """
                    )
                }
            ),
        ], widths="equal")
    ])
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 22)
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(f"""
    marimo is a **reactive** Python notebook.

    This means that unlike traditional notebooks, marimo notebooks **run
    automatically** when you modify them or
    interact with UI elements, like this slider: {slider}

    {"##" + "🍃" * slider.value}
    """)

    from pathlib import Path as _Path


    def _attribution_card(name, image_name, description):
        image_path = _Path('assets') / image_name
        image = mo.image(str(image_path)) if image_path.exists() else mo.md(
            f"_Image not found: `{image_path}`_"
        )
        return mo.vstack([
            image,
            mo.accordion({name: mo.md(description)}),
        ])


    mo.vstack([
        mo.md("## Attribution"),
        mo.hstack([
            _attribution_card(
                "Vincent Warmerdam",
                "Vincent.png",
                """
                - Works for Marimo
                - Has at least 100 youtube videos 
                """,
            ),
            _attribution_card(
                "Akshay Agrawal",
                "Akshay.png",
                """
                - Founder, CEO, and inventor of Marimo
                - Stanford Ph.D., worked at Google on Tensorflow
                """,
            ),
        ], widths="equal"),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack([
        mo.md(
            """
            ## 1. Marimo Introduction and Overview

            marimo notebooks resemble jupyter (vertically arranged blocks, code or markup).

            jupyter flow order is top to bottom. Great for exploration and trying things out.

            marimo reactivity sets order based on dependencies and keeps outputs and code in sync.

            I will show many examples of that tonight.

            - jupyter is great for exploration, but beware of hidden state, manual reruns,
              and hard-to-review file formats
            - marimo notebooks are stored as Python files
            - outputs synchronize with code, and can run as scripts, apps, or slides
            - I will give a quick comparison with jupyter, go over the marimo basics,
              show two app demos, and wrap up

            Lets keep this interactive. If you have a question please ask at any time.
            """
        ),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Tip: disabling automatic execution": mo.md(
                rf"""
            marimo lets you disable automatic execution: in the notebook
            footer, change "On Cell Change" to "lazy".

            When the runtime is lazy, after running a cell, marimo marks its
            descendants as stale instead of automatically running them. The
            lazy runtime puts you in control over when cells are run, while
            still giving guarantees about the notebook state.
            """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Tip: This is a tutorial notebook. You can create your own notebooks
        by entering `marimo edit` at the command line.
        """
    ).callout()
    return


@app.cell(hide_code=True)
def _(changed, mo):
    (
        mo.md(
            f"""
            **✨ Nice!** The value of `changed` is now {changed}.

            When you updated the value of the variable `changed`, marimo
            **reacted** by running this cell automatically, because this cell
            references the global variable `changed`.

            Reactivity ensures that your notebook state is always
            consistent, which is crucial for doing good science; it's also what
            enables marimo notebooks to double as tools and  apps.
            """
        )
        if changed
        else mo.md(
            """
            **🌊 See it in action.** In the next cell, change the value of the
            variable  `changed` to `True`, then click the run button.
            """
        )
    )
    return


@app.cell
def _():
    changed = False
    return (changed,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Tip: execution order": (
                """
                The order of cells on the page has no bearing on
                the order in which cells are executed: marimo knows that a cell
                reading a variable must run after the cell that  defines it. This
                frees you to organize your code in the way that makes the most
                sense for you.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Global names must be unique.** To enable reactivity, marimo imposes a
    constraint on how names appear in cells: no two cells may define the same
    variable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Tip: encapsulation": (
                """
                By encapsulating logic in functions, classes, or Python modules,
                you can minimize the number of global variables in your notebook.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Tip: private variables": (
                """
                Variables prefixed with an underscore are "private" to a cell, so
                they can be defined by multiple cells.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 2. UI elements

    Cells can output interactive UI elements. Interacting with a UI
    element **automatically triggers notebook execution**: when
    you interact with a UI element, its value is sent back to Python, and
    every cell that references that element is re-run.

    marimo provides a library of UI elements to choose from under
    `marimo.ui`.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    **🌊 Some UI elements.** Try interacting with the below elements.
    """)
    return


@app.cell
def _(mo):
    icons = mo.ui.dropdown(["🐶", "🐱"], value="🐶")
    return (icons,)


@app.cell
def _(icons, mo):
    repetitions = mo.ui.slider(1, 16, label=f"number of {icons.value}: ")
    return (repetitions,)


@app.cell
def _(icons, mo, repetitions):
    mo.vstack([
        mo.vstack([icons, mo.left(repetitions)]),
        mo.md("# " + icons.value * repetitions.value)
    ])
    return


@app.cell
def _(mo):
    slider_max = 6
    best_slider = mo.ui.slider(
        1, slider_max, 1, label = 'best slider', value = 3
    )
    return best_slider, slider_max


@app.cell
def _(best_slider, mo, slider_max):
    mo.vstack([
        mo.md(f"""{best_slider} value: {best_slider.value}"""),
        mo.md('#' + '🐱' *  best_slider.value),
        mo.md('#' +'🐶 ' * (1 + slider_max - best_slider.value))
    ])
    return


@app.cell
def _(mo):
    radio = mo.ui.radio(
        options=sorted([
                'Green Day', 'Jefferson Airplane',  'Metallica', 'Grateful Dead', 
                'Santana','Journey', 'Petrichor'
        ]),
        label='Your favorite Bay Area band (pick 1)'
    )
    multiselect = mo.ui.multiselect(
            options=['Springfield', 'Chicago', 'New York', 'Los Angeles'], 
            label='pick your favorite town',
            max_selections=2 # Optional, None for no limit, integer for specific limit'
    )
    checkbox = mo.ui.checkbox(label="yes I read the T's and C's")
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
def _():
    return


@app.cell
def _(marimo_ui_dictionary):
    marimo_ui_dictionary.value
    return


@app.cell
def _(pl):
    df_polars = (
        pl.DataFrame({str(i): [j * i for j in range(11)] for i in range(11)})
        .with_columns(pl.all().cast(pl.UInt8))
    )
    df_polars
    return


@app.cell
def _(mo, pl):
    ## California Counties
    df_cal = (
        pl.read_excel('assets/california_counties_wikipedia.xlsx')
        .lazy()
        .with_columns(
            # Normalize to CA county FIPS format (06001, 06013, ...)
            pl.concat_str([
                pl.lit('06'),
                pl.col('FIPS').cast(pl.Int64).cast(pl.String).str.zfill(3)
            ]).alias('FIPS'),
            pl.col('Established').cast(pl.UInt16),
            pl.col('Pop').cast(pl.UInt32),
            pl.col('Area_Sq_Mile').cast(pl.UInt16), 
            pl.col('Area_Sq_KM').cast(pl.UInt16),
            pl.col('County').str.strip_chars()
        )
        .with_columns(
            Pop_Density_Sq_Mile = 
                (pl.col('Pop')/pl.col('Area_Sq_Mile'))
                .round(1),
            Pop_Density_Sq_KM = (pl.col('Pop')/pl.col('Area_Sq_KM')).round(1)
        )
        .with_columns(
            Pop_Rank = pl.col('Pop').rank(method='min', descending=True),
            Pop_Density_Rank = pl.col('Pop_Density_Sq_Mile')
                                .rank(method='min', descending=True),
            Area_Rank = pl.col('Area_Sq_Mile').rank(method='min', descending=True),        
        )
        .sort('County', descending=False)
        .select([
            'County', 'Seat', 'Established', 
            'Pop',  'Pop_Rank', 
            'Area_Sq_Mile', 'Area_Sq_KM', 'Area_Rank',
            'Pop_Density_Sq_Mile', 'Pop_Density_Sq_KM', 'Pop_Density_Rank',   
            'Formation', 'Etymology', 'FIPS',
        ])
        .collect()
    )

    demo = mo.ui.radio(
            options=['Population', 'Population Density', 'Area'], 
            value="Population", 
            label='',  # choose a statistic:',
            inline =  True   # Make them appear side-by-side
        )
    return demo, df_cal


@app.cell
def _(df_cal):
    df_cal
    return


@app.cell
def _(mo):
    get_selected_county, set_selected_county = mo.state(None)
    return get_selected_county, set_selected_county


@app.cell
def _(demo, df_cal, get_selected_county, go, mo, pl, px):
    demo_view = demo.value if demo.value else None
    print(f'display top 10 and bottom 10 charts by county {demo_view}')
    fig1 = fig2 = go.Figure()

    if demo_view == 'Population':
        fig1 = px.bar(
            df_cal.sort('Pop_Rank', descending=True).tail(10),
            x='Pop',
            y='County', 
            title = f'Top 10',subtitle = demo_view,
            labels={'Pop': 'Population'}
        )
        fig2 = px.bar(
            df_cal.sort('Pop_Rank', descending=True).head(10),
            x='Pop',
            y='County',
            title = f'Bottom 10', subtitle = demo_view,
            labels={'Pop': 'Population'}
        )

    if demo_view == 'Population Density':
        fig1 = px.bar(
            df_cal.sort('Pop_Density_Sq_Mile', descending=False).tail(10),
            x='Pop_Density_Sq_Mile',
            y='County', 
            title = f'Top 10',subtitle = demo_view,
            labels={'Pop_Density_Sq_Mile': 'Population per Square Mile'}
        )
        fig2 = px.bar(
            df_cal.sort('Pop_Density_Sq_Mile', descending=False).head(10),
            x='Pop_Density_Sq_Mile',
            y='County',
            title = f'Bottom 10', subtitle = demo_view,
            labels={'Pop_Density_Sq_Mile': 'Population per Square Mile'}
        )

    if demo_view == 'Area':
        fig1 = px.bar(
            df_cal.sort('Area_Sq_Mile', descending=False).tail(10),
            x='Area_Sq_Mile',
            y='County', 
            title = f'Top 10',subtitle = demo_view,
            labels={'Area_Sq_Mile': 'Area (Square Miles)'}
        )
        fig2 = px.bar(
            df_cal.sort('Area_Sq_Mile', descending=False).head(10),
            x='Area_Sq_Mile',
            y='County',
            title = f'Bottom 10', subtitle = demo_view,
            labels={'Area_Sq_Mile': 'Area (Square Miles)'}
        )

    selected_county = get_selected_county()

    # Update layout to set custom height and width, offset y-labels from bars
    h = 400
    w = 400
    fig1.update_layout(width=w, height=h, yaxis=dict(ticklabelstandoff=10))
    fig2.update_layout(width=w, height=h, yaxis=dict(ticklabelstandoff=10))
    for fig in (fig1, fig2):
        fig.update_layout(clickmode='event+select')
        selected_indices = (
            [
                index
                for index, county in enumerate(fig.data[0].y)
                if county == selected_county
            ]
            if selected_county
            else []
        )
        fig.update_traces(
            selectedpoints=selected_indices,
            selected=dict(marker=dict(color='green')),
            unselected=dict(marker=dict(color='lightgray', opacity=0.65)),
        )

    # Wrap figures in mo.ui.plotly so a selected bar can update the info block.
    fig1_ui = mo.ui.plotly(fig1)
    fig2_ui = mo.ui.plotly(fig2)

    description = ''
    if demo_view == 'Population':
        description = (
            '''
            California’s 58 counties span the widest population extremes of any 
            state in the country. Los Angeles County dominates the high end, while 
            Alpine County anchors the low end, and the spread between them is 
            nearly 10 million people.
            '''
            )
    elif demo_view == 'Population Density':
        description = (
            '''
            California’s county population density ranges from hyper‑urban to 
            frontier‑level sparse, with a spread of nearly 18,000 people per square mile 
            between the top and bottom. The single most important fact: San Francisco 
            County is by far the densest, while Inyo, Alpine, and Modoc anchor the lowest 
            end at ~2 people per square mile.
            '''
            )
    elif demo_view == 'Area':
        description = (
            '''
            California’s counties span one of the widest area ranges of any state. The
            largest county in the contiguos United States (San Bernardino) is larger than
            9 other states, including New Jersey and Massachusetts. The smallest county in
            California is San Francisco, which also has the largest population density in
            our state.  California’s county areas reflect our mix of
            vast deserts, mountain regions, and compact urban cores.
            '''
            )
    selected_county_row = (
        df_cal.filter(pl.col('County') == selected_county).row(0, named=True)
        if selected_county
        else None
    )
    if selected_county_row:
        county_info = mo.Html(
            f"""
            <div style='padding: 0.75rem 1rem; border: 1px solid var(--border-color);'>
                <strong>{selected_county_row['County']}</strong><br>
                Formation: {selected_county_row['Formation']}<br>
                Etymology: {selected_county_row['Etymology']}
            </div>
            """
        )
    else:
        county_info = mo.Html('')

    dataframe_info = '''
        SHOW ME: This polars dataframe is used for all visualizations in this 
        notebook. Use the Transform block to interactively process a dataframe with a GUI, 
        no coding required. When you're done, you can copy the code that the GUI 
        generated for you and paste it into your notebook.
    '''
    layout = mo.vstack([
        mo.Html(dataframe_info),
        mo.ui.dataframe(df_cal),
        mo.Html('<br>'),
        mo.left(demo),
        mo.Html('<br>'),
        mo.left(mo.Html(f' <h1>California County {demo_view}</h1>')),
        mo.Html('<br>'),
        mo.Html(description),
        county_info,
        mo.hstack([fig1_ui, fig2_ui], widths='equal'),
    ])
    return fig1_ui, fig2_ui, layout


@app.cell
def _(layout):
    layout
    return


@app.cell
def _(fig1_ui, fig2_ui, set_selected_county):
    selected_points = fig1_ui.points + fig2_ui.points
    if selected_points:
        set_selected_county(selected_points[0].get('y'))
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 3. marimo is just Python

    marimo cells parse Python (and only Python), and marimo notebooks are
    stored as pure Python files — outputs are _not_ included. There's no
    magical syntax.

    The Python files generated by marimo are:

    - easily versioned with git, yielding minimal diffs
    - legible for both humans and machines
    - formattable using your tool of choice,
    - usable as Python  scripts, with UI  elements taking their default
    values, and
    - importable by other modules (more on that in the future).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 4. Running notebooks as apps

    marimo notebooks can double as apps. Click the app window icon in the
    bottom-right to see this notebook in "app view."

    Serve a notebook as an app with `marimo run` at the command-line.
    Of course, you can use marimo just to level-up your
    notebooking, without ever making apps.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 5. The `marimo` command-line tool

    **Creating and editing notebooks.** Use

    ```
    marimo edit
    ```

    in a terminal to start the marimo notebook server. From here
    you can create a new notebook or edit existing ones.


    **Running as apps.** Use

    ```
    marimo run notebook.py
    ```

    to start a webserver that serves your notebook as an app in read-only mode,
    with code cells hidden.

    **Convert a Jupyter notebook.** Convert a Jupyter notebook to a marimo
    notebook using `marimo convert`:

    ```
    marimo convert your_notebook.ipynb > your_app.py
    ```

    **Tutorials.** marimo comes packaged with tutorials:

    - `dataflow`: more on marimo's automatic execution
    - `ui`: how to use UI elements
    - `markdown`: how to write markdown, with interpolated values and
       LaTeX
    - `plots`: how plotting works in marimo
    - `sql`: how to use SQL
    - `layout`: layout elements in marimo
    - `fileformat`: how marimo's file format works
    - `markdown-format`: for using `.md` files in marimo
    - `for-jupyter-users`: if you are coming from Jupyter

    Start a tutorial with `marimo tutorial`; for example,

    ```
    marimo tutorial dataflow
    ```

    In addition to tutorials, we have examples in our
    [our GitHub repo](https://www.github.com/marimo-team/marimo/tree/main/examples).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 6. The marimo editor

    Here are some tips to help you get started with the marimo editor.
    """)
    return


@app.cell
def _(mo, tips):
    mo.accordion(tips)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Finally, a fun fact
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    The name "marimo" is a reference to a type of algae that, under
    the right conditions, clumps together to form a small sphere
    called a "marimo moss ball". Made of just strands of algae, these
    beloved assemblages are greater than the sum of their parts.
    """)
    return


@app.cell(hide_code=True)
def _():
    tips = {
        "Saving": (
            """
            **Saving**

            - _Name_ your app using the box at the top of the screen, or
              with `Ctrl/Cmd+s`. You can also create a named app at the
              command line, e.g., `marimo edit app_name.py`.

            - _Save_ by clicking the save icon on the bottom right, or by
              inputting `Ctrl/Cmd+s`. By default marimo is configured
              to autosave.
            """
        ),
        "Running": (
            """
            1. _Run a cell_ by clicking the play ( ▷ ) button on the top
            right of a cell, or by inputting `Ctrl/Cmd+Enter`.

            2. _Run a stale cell_  by clicking the yellow run button on the
            right of the cell, or by inputting `Ctrl/Cmd+Enter`. A cell is
            stale when its code has been modified but not run.

            3. _Run all stale cells_ by clicking the play ( ▷ ) button on
            the bottom right of the screen, or input `Ctrl/Cmd+Shift+r`.
            """
        ),
        "Console Output": (
            """
            Console output (e.g., `print()` statements) is shown below a
            cell.
            """
        ),
        "Creating, Moving, and Deleting Cells": (
            """
            1. _Create_ a new cell above or below a given one by clicking
                the plus button to the left of the cell, which appears on
                mouse hover.

            2. _Move_ a cell up or down by dragging on the handle to the
                right of the cell, which appears on mouse hover.

            3. _Delete_ a cell by clicking the trash bin icon. Bring it
                back by clicking the undo button on the bottom right of the
                screen, or with `Ctrl/Cmd+Shift+z`.
            """
        ),
        "Disabling Automatic Execution": (
            """
            Via the notebook settings (gear icon) or footer panel, you
            can disable automatic execution. This is helpful when
            working with expensive notebooks or notebooks that have
            side-effects like database transactions.
            """
        ),
        "Disabling Cells": (
            """
            You can disable a cell via the cell context menu.
            marimo will never run a disabled cell or any cells that depend on it.
            This can help prevent accidental execution of expensive computations
            when editing a notebook.
            """
        ),
        "Code Folding": (
            """
            You can collapse or fold the code in a cell by clicking the arrow
            icons in the line number column to the left, or by using keyboard
            shortcuts.

            Use the command palette (`Ctrl/Cmd+k`) or a keyboard shortcut to
            quickly fold or unfold all cells.
            """
        ),
        "Code Formatting": (
            """
            If you have [ruff](https://github.com/astral-sh/ruff) installed,
            you can format a cell with the keyboard shortcut `Ctrl/Cmd+b`.
            """
        ),
        "Command Palette": (
            """
            Use `Ctrl/Cmd+k` to open the command palette.
            """
        ),
        "Keyboard Shortcuts": (
            """
            Open the notebook menu (top-right) or input `Ctrl/Cmd+Shift+h` to
            view a list of all keyboard shortcuts.
            """
        ),
        "Configuration": (
            """
           Configure the editor by clicking the gears icon near the top-right
           of the screen.
           """
        ),
        "Exit & Shutdown": (
            """
           You can leave Marimo & shut down the server by clicking the
           circled X at the top right of the screen and responding
           to the prompt.

           :floppy_disk: _Be sure to save your work first!_
           """
        ),
    }
    return (tips,)


if __name__ == "__main__":
    app.run()
