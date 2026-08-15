# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.16",
# ]
# ///

# Copyright 2024 Marimo. All rights reserved.

import marimo

__generated_with = "0.23.16"
app = marimo.App(layout_file="layouts/mp_marimo_2026_08_27.slides.json")


@app.cell
def _():

    import marimo as mo

    mo.Html('<link rel="stylesheet" href="assets/styles.css">')
    mo.vstack([
        mo.Html("<h1>Welcome to marimo! 🌊🍃</h1><br><br>"),
        mo.Html("<h2>Mike Purtell</h2>"),
        mo.Html("<h3>Bay Area Python Interest Group</h3>"),
        mo.Html("<h3>August 27,&nbsp; 2026</h3>")
    ])
    return (mo,)


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 22)
    return (slider,)


@app.cell
def _(mo):
    mo.Html('<link rel="stylesheet" href="assets/styles.css">')
    mo.vstack([
        mo.Html("<h1>Marimo Introduction and Overview</h1><br><br>"),
        mo.md("""                
        <div style="font-size: 1.25rem; line-height: 1.6;">
        marimo resembles jupyter (vertically arranged blocks, code or markup)
        </div>
        """),
        mo.hstack([
            mo.accordion(
                {
                    "<div style='font-size: 1.25rem; line-height: 1.6;'>jupyter</div>": mo.md(
                        rf"""
                    <div style="font-size: 1.25rem; line-height: 1.6;">
                    <ul>
                        <li>great for exploration</li>
                        <li>beware of:</li>
                        <ul>
                            <li>hidden state</li>
                            <li>manual reruns</li>
                            <li>hard-to-review file formats, Git Issues</li>
                            <li>top down flow for run-all, arbitrary flow otherwise</li>
                        </ul>
                    </ul>
                    </div>
                    """
                    )
                }
            ),
            mo.accordion(
                {
                    "<div style='font-size: 1.25rem; line-height: 1.6;'>marimo</div>": mo.md(
                        rf"""
                    <div style="font-size: 1.25rem; line-height: 1.6;">
                    <ul>
                        <li>reactivity: change value in 1 cell updates the dependent cells</li>
                        <li>think of Excel</li>
                        <li>Natural mechanism for call backs</li>
                        <li>great for dashboards</li>
                        <li>easy to deploy on molab</li>
  
                    </ul>
                    </div>
                    """
                    )
                }
            ),
          ], widths="equal")
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack([
        mo.Html("""
        ## 1. Marimo Introduction and Overview

        marimo notebooks resemble jupyter (vertically arranged blocks, code or markup).

        jupyter flow order is top to bottom. great for exploration, trying things out

        marimo reactivity sets order based on dependencies, keeps outputs and the code in sync.

        I will show many examples of that tonight.
        •	jupyter is great for exploration, beware of hidden state, manual re-
        runs, and hard-to-review file formats
        •	marimo notebooks are stored as Python files.
        runs, and hard-to-review file formats
        •  Outputs synchronize with code, and can run as scripts, apps, or slides<br>
        •	I will give a quick quick, compare with jupyter comparisonr, go over the marimo basics, show two app demos, two app demos before wrappging up.<br>

        Lets keep this interactive. If you have a question please ask at any time.
        """),
    ])
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md("""
        ## 1.1 important concepts
        """),
        mo.accordion(
            {
                "jupyter": mo.md(
                    rf"""
                jupyter is great for exploration, beware of hidden state, manual 
                reruns, and hard-to-review file formats.
                """
                )
            }
        ),
        mo.accordion({
                "marimo": mo.md(
                    rf"""
                        stored as python files, git friendly, code, markdown, sql, and more. Outputs synchronize with code, and can run as scripts, apps, or slides.
                        """
                    )
            }
        ),
   
    ])
    return


@app.cell
def _(mo):
    top_line = mo.Html(text='<h1>1. marimo Introduction and Overview</h1>')


    top_line
    return (top_line,)


@app.cell
def _(mo, top_line):
    mo.vstack([
        top_line
    ])
    return


@app.cell
def _(mo, slider):
    mo.md(f"""
    marimo is a **reactive** Python notebook.

    This means that unlike traditional notebooks, marimo notebooks **run
    automatically** when you modify them or
    interact with UI elements, like this slider: {slider}

    {"##" + "🍃" * slider.value}
    """)
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
    icon = mo.ui.dropdown(["🍃", "🌊", "✨"], value="🍃")
    return (icon,)


@app.cell
def _(icon, mo):
    repetitions = mo.ui.slider(1, 16, label=f"number of {icon.value}: ")
    return (repetitions,)


@app.cell
def _(icon, repetitions):
    icon, repetitions
    return


@app.cell
def _(icon, mo, repetitions):
    mo.md("# " + icon.value * repetitions.value)
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
