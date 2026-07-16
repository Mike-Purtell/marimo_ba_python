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
    This notebook showcases datavisualization with Marimo
    """)
    return


@app.cell
def _():
    import polars as pl
    print(f'Polars version {pl.__version__}')
    return (pl,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Hello World of dataframes
    Multiplication tables are often the first structured table people learn
    """)
    return


@app.cell
def _(pl):
    df_polars = (
        pl.DataFrame({str(i): [j * i for j in range(11)] for i in range(11)})
        .with_columns(pl.all().cast(pl.UInt8))
    )
    df_polars  # no index with polars. display has columns,  data types or shape
    return (df_polars,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Marimo with Plotly
    Jupyter does not provide built-in data visualization tools.
    Libraries like Plotly, Matplotlib, Altair or others are required.
    """)
    return


@app.cell
def _(df_polars, mo):
    import plotly 
    import plotly.graph_objects as go
    print(f'Plotly version {plotly.__version__}')

    x_values = df_polars['1'].to_list()
    fig = go.Figure([
            go.Scatter(
            x=x_values,
            y=df_polars[c].to_list(),
            mode='lines',
            name=c + '*X')
        for c in df_polars.columns
    ])
    fig.update_layout(
        title="3rd Grade Times Table - 0's included for STEM students",
        xaxis_title='Factor',
        yaxis_title='Product',
        template='simple_white',
        hovermode='x unified',
        showlegend=False,
        width=(w:=600),
        height=w,
        margin=dict(r=90))
    fig.update_xaxes(
        range=[min(x_values), max(x_values) + 1],
        tickmode='array',
        tickvals=x_values,
        ticktext=[str(value) for value in x_values],
        showgrid=True,
        gridcolor='lightgray',
        griddash='dash')
    fig.update_yaxes(
        tickmode='array',
        tickvals=list(range(0, 101, 10)),
        showgrid=True,
        gridcolor='lightgray',
        griddash='dash')
    fig.update_traces(cliponaxis=False)

    for column in df_polars.columns:
        fig.add_annotation(
            x=x_values[-1],
            y=df_polars[column].to_list()[-1],
            text=column + ' X',
            showarrow=False,
            xanchor='left',
            xshift=10,
            yanchor='middle')

    mo.ui.plotly(fig) # required for display of Plotly figure in Marimo app
    return


@app.cell
def _(df_polars):
    # replace _df with your data source
    import altair as alt
    _chart = (
        alt.Chart(df_polars)
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
            title='Time Table',
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
    return (alt,)


@app.cell
def _(alt, df_polars, pl):
    # Use df_polars directly and reshape to long format for Altair
    trace_columns = [c for c in df_polars.columns if c != '0']
    alt_df = (
        df_polars
        .with_row_index('factor')
        .unpivot(index='factor', on=trace_columns, variable_name='trace', value_name='product')
        .with_columns(pl.format('{} X', pl.col('trace')).alias('trace'))
    )

    end_labels = alt_df.filter(pl.col('factor') == 10)

    lines = (
        alt.Chart(alt_df)
        .mark_line()
        .encode(
            x=alt.X('factor:Q', title='Factor', scale=alt.Scale(domain=[0, 11])),
            y=alt.Y('product:Q', title='Product', scale=alt.Scale(domain=[0, 100])),
            color=alt.Color('trace:N', legend=None),
            tooltip=[
                alt.Tooltip('trace:N', title='Table'),
                alt.Tooltip('factor:Q', title='Factor', format='.0f'),
                alt.Tooltip('product:Q', title='Product', format='.0f'),
            ],
        )
    )

    labels = (
        alt.Chart(end_labels)
        .mark_text(align='left', dx=8, baseline='middle')
        .encode(
            x='factor:Q',
            y='product:Q',
            text='trace:N',
            color=alt.Color('trace:N', legend=None),
        )
    )

    alt_chart = (
        (lines + labels)
        .properties(
            title="Marimo with user/AI generated altair code</sup>"
            ),
            # width=600,
            # height=600,
        )

    alt_chart
    return


if __name__ == "__main__":
    app.run()
