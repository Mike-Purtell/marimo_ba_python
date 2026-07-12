# Notebook Comparison: Jupyter vs Marimo

This folder contains one Jupyter notebook and several Marimo notebook variants used to compare workflow, reactivity, dataframe display behavior, and visualization patterns.

## Purpose

The materials are designed for a talk/demo that contrasts:
- Jupyter execution-order flexibility (and its pitfalls)
- Marimo reactive execution model
- Dataframe display differences with Pandas and Polars
- Data visualization setup using Plotly

## Files In This Folder

### Jupyter Baseline

- [jupyter-1.ipynb](jupyter-1.ipynb)
  - Main baseline notebook.
  - Sections include:
    - Variable state and execution-order behavior (the x example)
    - Dataframe creation and display (Pandas vs Polars)
    - Plotly line-chart visualization of multiplication tables

### Marimo Comparison Notebooks

- [marimo-1-reactivity.py](marimo-1-reactivity.py)
  - Marimo conversion artifact focused on reactivity concepts.
  - Shows how variables can be renamed or rewritten to preserve a valid reactive graph.

- [marimo-2-dataframes.py](marimo-2-dataframes.py)
  - Marimo app focused on dataframe examples.
  - Compares dataframe representation and output style in a Marimo workflow.

- [marimo-3-dataviz.py](marimo-3-dataviz.py)
  - Marimo app focused on plotting.
  - Recreates the multiplication-table Plotly visualization in Marimo.

### Additional Artifacts

- [marimo-1.reactivity.py](marimo-1.reactivity.py)
  - Present in the workspace as an additional file variant.
  - Currently empty.

- [jupyter_1.ipynb_json.txt](jupyter_1.ipynb_json.txt)
  - Text export/representation of notebook JSON.

## Suggested Comparison Flow

1. Start with [jupyter-1.ipynb](jupyter-1.ipynb) to show execution order effects.
2. Move to [marimo-1-reactivity.py](marimo-1-reactivity.py) for reactive-graph constraints.
3. Use [marimo-2-dataframes.py](marimo-2-dataframes.py) for dataframe display comparison.
4. Finish with [marimo-3-dataviz.py](marimo-3-dataviz.py) for the Plotly visualization equivalent.

## Running The Marimo Apps

From this folder, run:

marimo edit marimo-2-dataframes.py
marimo edit marimo-3-dataviz.py

If needed, install dependencies first:

pip install marimo pandas polars plotly
