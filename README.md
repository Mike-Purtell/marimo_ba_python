# Learning Marimo: Interactive Python Notebooks

This folder supports a talk and hands-on demonstration of **marimo**, a reactive
Python notebook environment. The main teaching artifact is
[mp_marimo_2026_08_27.py](mp_marimo_2026_08_27.py). It is designed to show how
marimo turns ordinary Python cells into a dependency-aware, interactive
notebook that can also run as an application.

The central idea is simple: cells form a dataflow graph. When an input changes,
marimo automatically re-runs the cells that depend on it. There is no need to
manually hunt for stale outputs or remember which cells were run first.

## Main Demo: `mp_marimo_2026_08_27.py`

Open the app as a marimo notebook and follow the sections in order. The file is
stored as regular Python, so it is readable, executable, and friendly to Git.
It uses a slide layout from
[layouts/mp_marimo_2026_08_27.slides.json](layouts/mp_marimo_2026_08_27.slides.json)
and presentation images and data from the `assets/` directory.

The demo focuses on the features that make marimo different from a traditional
notebook:

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

## Run the Marimo Demo

The file includes its dependency metadata. With the project environment
active, start the editor with:

```powershell
marimo edit mp_marimo_2026_08_27.py
```

To serve it as a read-only app:

```powershell
marimo run mp_marimo_2026_08_27.py
```

Before launching the notebook, validate the slide layout JSON and speaker
notes coverage:

```powershell
./validate_slides_layout.ps1
```

To validate a different layout file:

```powershell
./validate_slides_layout.ps1 -Path layouts/your_file.slides.json
```

The declared dependencies include marimo, Polars, NumPy, Plotly, and
`fastexcel`. The app also expects the presentation images and the county Excel
data referenced by the cells to be available in the project assets.

Useful marimo commands to explore after the demo include:

```text
marimo tutorial dataflow
marimo tutorial ui
marimo tutorial for-jupyter-users
```

## Supporting Files

- [layouts/mp_marimo_2026_08_27.slides.json](layouts/mp_marimo_2026_08_27.slides.json): slide-oriented layout for the main presentation.
- [assets/styles.css](assets/styles.css): supporting presentation styles.
- [marimo.agent.md](marimo.agent.md): local notes about marimo notebook conventions.

## Jupyter Baseline

At the bottom of this project is [marimo-talk-jupyter.ipynb](marimo-talk-jupyter.ipynb),
a small Jupyter notebook used only as a comparison point. It demonstrates
Jupyter's execution-order behavior, dataframe displays, and Plotly output so
the talk can motivate why marimo's reactive model and code-only file format
matter. The goal of this project, however, is to learn and demonstrate marimo's
important features, not to maintain parallel Jupyter examples.
