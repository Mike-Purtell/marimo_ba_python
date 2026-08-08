import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import altair as alt
    import plotly.graph_objects as go

    return alt, go, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Marimo Notebook
    This brief notebook showcases marimo dataframe displays
    """)
    return


@app.cell
def _():
    import polars as pl
    import polars.selectors as cs

    print(f'Polars version {pl.__version__}')
    return cs, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Hello World of dataframes
    Multiplication tables are often the first structured table people learn
    """)
    return


@app.cell
def _(cs, pl):
    df_times_table = (
        pl.DataFrame(
            {str(i): [j * i for j in range(10)] for i in range(10)}, 
        )
        .with_columns(cs.all().cast(pl.UInt8))
    )
    print(f'{df_times_table.shape = }')
    print(f'{df_times_table.columns = }')
    print(f'{df_times_table.dtypes = }')
    return (df_times_table,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Dataframe displays in Marimo
    Marimo dataframe displays show the dataframe shape, the datatype of each column, and include 4 useful exploration tools:
    <ol>
        <li>Columns filter</li>
        <li>Visualize - no code required, generates code</li>
        <li>Explore or filter rows or columns</li>
        <li>Export - save dataframe as csv, tsv, json or parquet, or copy to clipboard</li>
    </ol>

    Pandas DataFrame above doesn’t display its datatypes or shape. The Polars DataFrame below includes both. Each DataFrame is simply a different representation of the same experimental data.
    """)
    return


@app.cell
def _(df_times_table):
    df_times_table# .to_pandas()
    return


@app.cell
def _(alt, df_times_table):
    # replace _df with your data source
    _chart = (
        alt.Chart(df_times_table)
        .mark_point()
        .encode(
            x=alt.X(field='1', type='quantitative'),
            y=alt.Y(field='3', type='quantitative', aggregate='mean'),
            tooltip=[
                alt.Tooltip(field='1', format=',.0f'),
                alt.Tooltip(field='3', aggregate='mean', format=',.0f')
            ]
        )
        .properties(
            height=290,
            width='container',
            config={
                'axis': {
                    'grid': True
                }
            }
        )
    )
    _chart
    return


@app.cell
def _(df_times_table, go):
    x = df_times_table['1'].to_list()

    fig = go.Figure()
    for i, col in enumerate([c for c in df_times_table.columns], start=1):
        y = df_times_table[col].to_list()
        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                mode='lines+markers',
                # name=f'x{i}',
                showlegend=False,
            )
        )
        fig.add_annotation(
            x=x[-1],
            y=y[-1],
            xref="x",
            yref="y",
            text=f' x {i-1}',
            showarrow=False,
            xanchor="left",
            yanchor="middle",
        )

    fig.update_layout(
        showlegend=False,
        title='Fancier Plotly Graph',
        xaxis_title='Factor',
        yaxis_title='Product',
        margin=dict(l=20, r=80, t=40, b=20),
        xaxis=dict(tickmode='linear', tick0=0, dtick=1)
    )
    fig.update_xaxes(showgrid=False, zeroline=True)
    fig.update_yaxes(showgrid=False, zeroline=True)
    fig
    return


if __name__ == "__main__":
    app.run()
