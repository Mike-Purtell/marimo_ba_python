# Learning Marimo: Interactive Python Notebooks

This folder contains the materials for the Bay Area Python Interest Group
presentation on August 27, 2026. The main topic is **marimo**, a reactive
Python notebook environment. The examples are arranged to introduce the
problems with traditional notebook workflows, then show how marimo addresses
them.

## Presentation Files

### Interactive slide deck: `marimo_slides_2026_08_27.py`

Open [marimo_slides_2026_08_27.py](marimo_slides_2026_08_27.py) as a marimo
notebook to run the interactive slide deck. It uses the slide layout in
[layouts/marimo_slides_2026_08_27.slides.json](layouts/marimo_slides_2026_08_27.slides.json)
and presentation assets from the `assets/` directory.

### Jupyter comparison: `jupyter_demo.ipynb`

[jupyter_demo.ipynb](jupyter_demo.ipynb) demonstrates Jupyter notebook
attributes that marimo is designed to solve, including execution-order issues,
hidden state, and stale or out-of-sync outputs. It provides the baseline for
understanding why marimo's reactive model is useful.

### Reactivity demonstration: `marimo_demo.py`

[marimo_demo.py](marimo_demo.py) focuses on marimo reactivity. Its cells show
how changing an input automatically updates dependent values, tables, charts,
and other UI elements. The file is stored as regular Python, so it is readable,
executable, and friendly to Git.

The central idea is simple: cells form a dataflow graph. When an input changes,
marimo automatically re-runs the cells that depend on it. There is no need to
manually hunt for stale outputs or remember which cells were run first.

## What the marimo examples show

The marimo files focus on the features that make marimo different from a
traditional notebook:

### Reactive execution

The cells demonstrate explicit dependencies between values and their consumers.
Changing a value updates the relevant downstream cells automatically. This is
the foundation for reproducible notebooks and interactive applications.

### Interactive UI elements

The app uses marimo controls such as sliders, radio buttons, multiselects,
checkboxes, and number inputs. Their `.value` properties are ordinary Python
values, and changing a control triggers dependent cells to run again. Examples
include the cats-versus-dogs slider, a Bay Area music selection, and controls
for the quadratic analyzer.

### Layout and presentation

`mo.vstack`, `mo.hstack`, `mo.accordion`, `mo.md`, `mo.Html`, and `mo.image`
are used to build a presentation directly from Python. The same cells provide
the computation and the user-facing interface, without a separate frontend.

### Tables and data exploration

The app displays a Polars multiplication table with `mo.ui.table` and works
with California county data. The county example calculates population,
density, and area rankings, then presents the resulting dataframe for further
inspection and transformation.

### Reactive visualizations

Plotly charts are embedded with `mo.ui.plotly`. The county view lets the user
switch metrics and select a county on a chart; the selected county then drives
the related information shown elsewhere in the layout. This is a useful
example of interactive chart events flowing back into Python.

### State and reusable Python logic

`mo.state` is used to carry the selected county between cells. The quadratic
analyzer separates inputs, calculations, and rendering into dependent cells,
including roots, the vertex, focus, directrix, grid, and axis scaling. The
result is a small interactive application built from ordinary Python
functions and values.

### Notebook-to-app workflow

The final sections introduce marimo's command-line workflow and the fact that
a notebook can be served as an app. The same source can be edited as a
notebook, run as a script with default UI values, or served with code hidden
for an application-style experience.

## Run the Marimo Files

With the project environment active, start the interactive slide deck with:

```
marimo edit --sandbox marimo_slides_2026_08_27.py
```
The declared dependencies include marimo, Polars, NumPy, Plotly, and
`fastexcel`. The examples also expect the presentation images and county Excel
data referenced by the cells to be available in this project.

Useful marimo commands to explore after the demo include:

```text
marimo tutorial dataflow
marimo tutorial ui
marimo tutorial for-jupyter-users
```

## Supporting Files
- [assets/styles.css](assets/styles.css): supporting presentation styles.
- [marimo.agent.md](marimo.agent.md): local notes about marimo notebook conventions.
