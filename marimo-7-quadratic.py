import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Quadratic Analyzer
    This notebook showcases datavisualization with Marimo
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import plotly.graph_objects as go
    import math

    return go, math


@app.cell
def _(mo):
    a_number =  mo.ui.number(value=1.0)
    b_number =  mo.ui.number(value=-4.0)
    c_number =  mo.ui.number(value=4.0)
    return a_number, b_number, c_number


@app.cell
def _(a_number, b_number, c_number, mo):
    a_stack = mo.vstack([
        mo.md('a: (x<sup>2</sup> term)'),
        a_number
    ])
    b_stack = mo.vstack([
        mo.md('b: (x) term:  '),
        b_number
    ])
    c_stack = mo.vstack([
        mo.md('c: (constant)  '),
        c_number
    ])
    return a_stack, b_stack, c_stack


@app.cell
def _(a_stack, b_stack, c_stack, mo):
    mo.hstack([
         a_stack, 
         b_stack, 
         c_stack
    ])
    return


@app.cell
def _(a_number, b_number, c_number):
    a = a_number.value
    b = b_number.value
    c = c_number.value
    a_sign = 1 if a > 0 else -1 # 1 of parabola opens upward, -1 if downward
    return a, a_sign, b, c


@app.cell
def _(a, b, c):
    has_two_roots = False
    has_one_root = False
    has_no_roots = False
    if (b**2) - (4*a*c) < 0:
        has_no_roots = True
    elif (b**2) - (4*a*c) == 0: 
        has_one_root = True
    else:
        has_two_roots = True
    
    print(f'{has_two_roots = }')
    print(f'{has_one_root = }')
    print(f'{has_no_roots = }')
    
    return has_no_roots, has_one_root, has_two_roots


@app.cell
def _(a, b, c, has_no_roots, has_one_root, has_two_roots, math):
    root = None
    root1 = None
    root2 = None
    if has_one_root:
        root = -b/(2*a)
    if has_two_roots:
        discriminant = math.sqrt(b**2-(4*a*c))
        print(f'{discriminant = :.1f}')
        root1 = ((-1*b)+discriminant)/(2*a)
        root2 = ((-1*b)-discriminant)/(2*a)
        if root2 < root1: # quick swap
            root2, root1 = root1, root2

    if has_no_roots:
        print('Has no root, this curve does not intersect y = 0')
    if has_one_root:
        print(f'One root, intersects (0, {root})')
    if has_two_roots:
        print(f'Two root, intersects (0, {root1:.3f}), (0, {root2:.3f}')
    return root1, root2


@app.cell
def _(a, a_sign, b, c):
    print(f'a, b, c = {a}, {b}, {c}, {a_sign}')
    return


@app.cell
def _(mo):
    show_grid = mo.ui.radio(label = 'Gridlines',options=['Show','Hide'], value='Hide')
    show_tick_labels  = mo.ui.radio(label = 'Tick Labels',options=['Show','Hide'], value='Hide')
    show_vertex = mo.ui.radio(label = 'Vertex',options=['Show','Hide'], value='Hide')
    show_focus = mo.ui.radio(label = 'Focus',options=['Show','Hide'], value='Hide')
    show_directrix = mo.ui.radio(label = 'Directrix',options=['Show','Hide'], value='Hide')
    show_roots = mo.ui.radio(label = 'Roots',options=['Show','Hide'], value='Hide')
    return (
        show_directrix,
        show_focus,
        show_grid,
        show_roots,
        show_tick_labels,
        show_vertex,
    )


@app.cell
def _(
    mo,
    show_directrix,
    show_focus,
    show_grid,
    show_roots,
    show_tick_labels,
    show_vertex,
):
    mo.hstack([
        show_grid,
        show_tick_labels,
        show_vertex,
        show_focus,
        show_directrix,
        show_roots
    ])
    return


@app.cell
def _(show_focus, show_vertex):
    print(f'{show_vertex.value = }')
    print(f'{show_focus.value = }')
    return


@app.cell
def _(a, b, c):
    # Conventional vertex coordiates are h, k. For upward facing parabolas, the vertex
    # is the minimum point on the y-axis, or maximum for downward facing parabola
    h = -b/(2*a)
    k = c - ((b**2)/(4*a))
    print(f'vertex at  ({h}, {k})')
    return h, k


@app.cell
def _(a, b, c, h):
    # focus
    x_focus = h
    y_focus = c - ((b**2)/(4*a)) + (1/(4*a)) # k + 1/(4*a)
    print(f'focus at  ({x_focus}, {y_focus})')
    return x_focus, y_focus


@app.cell
def _(a, h, y_focus):
    # width is the distance between the sides of a parabola along a horizontal line 
    # passing through the focus. Length of this line and coordinates are calculated
    x_offset = 1/(2*a)
    x1 = h - x_offset
    x2 = h + x_offset
    x_left, x_right = sorted((x1, x2))
    width_coordinates = [
        (x_left, y_focus),
        (x_right, y_focus)
    ]
    width = x_right-x_left
    print(f'intersections at {width_coordinates[0]} and {width_coordinates[1]}')
    print(f'{width = }')
    return width, x_left, x_right


@app.cell
def _(a, b, c, width, x_focus, x_left, x_right):
    # create a dataframe, 1000 points before vertex and 1000 points after
    n = 1000
    x_step = (x_right-x_left)/(n/10)
    x_start = x_focus - (5 * width)
    x_stop = x_focus + (5 * width)

    x_vals = [x_start + i * x_step for i in range(n+1)] 
    y_vals = [a*x*x + b*x + c for x in x_vals]

    print(x_vals)
    print(y_vals)
    return x_vals, y_vals


@app.cell
def _():
    # horizontal directrix line
    return


@app.cell
def _(a, b, c):
    y_directrix = c - ((b**2)/(4*a)) - (1/(4*a)) #   k - a

    print(f'{y_directrix = }')
    return (y_directrix,)


@app.cell
def _(
    a,
    a_sign,
    b,
    c,
    go,
    h,
    has_one_root,
    has_two_roots,
    k,
    root1,
    root2,
    show_directrix,
    show_focus,
    show_grid,
    show_roots,
    show_tick_labels,
    show_vertex,
    x_vals,
    y_directrix,
    y_focus,
    y_vals,
):
    fig = go.Figure(
            data=go.Scatter(
                x=x_vals,
                y=y_vals,
                showlegend=False
        )
    )
    fig.update_layout(
        title = f'{a}x<sup>2</sup> + {b}x + {c}'
    )
    marker_size = 6
    if show_vertex.value == 'Show':
        fig.add_trace(
            go.Scatter(
                x=[h],
                y=[k],
                mode='markers',
                marker=dict(size=marker_size, color='crimson'),
                name='Vertex',
                showlegend=False,
            )
        )
        fig.add_annotation(
            x=h,
            y=k,
            text=f'Vertex ({h:.3f}, {k:.3f})',
            showarrow=True,
            arrowhead=2,
            ax=20,
            ay=a_sign *30,
        )
    if show_focus.value == 'Show':
        fig.add_trace(
            go.Scatter(
                x=[h],
                y=[y_focus],
                mode='markers',
                marker=dict(size=marker_size, color='crimson'),
                name='Focus',
                showlegend=False,
            )
        )
        fig.add_annotation(
            x=h,
            y=y_focus,
            text=f'Focus ({h:.3f}, {y_focus:.3f})',
            showarrow=True,
            arrowhead=2,
            ax=20,
            ay=-1*a_sign*30,
        )
    if show_directrix.value == 'Show':
        fig.add_hline(
            y = y_directrix, # color='green',
            line_dash="dot",
            annotation_text=f'Directrix, <br>y = {y_directrix:.3f}',
            annotation_position="right", # Positions text at right end of line
            annotation_font_size=14,
            annotation_font_color="blue"
        )
        max_y_val = max(y_vals)
        min_y_val = min(y_vals)
        span_y_vals = abs(max_y_val - min_y_val)
        if a_sign == 1:
            y_max = max_y_val + (0.1 * span_y_vals)
            y_min = min_y_val - 2* abs(y_focus - y_directrix)
        else:
            y_max = max_y_val + 2* abs(y_focus -y_directrix)
            y_min = min_y_val - (0.1 * span_y_vals)
    
        fig.update_yaxes(range = [y_min, y_max])

    if show_roots.value == 'Show':
        if has_one_root: # if only one root, it is the vertex
            pass
        
        if has_two_roots:
            fig.add_trace(
                go.Scatter(
                    x=[root1, root2],
                    y=[0, 0],
                    mode='markers',
                    marker=dict(size=marker_size, color='crimson'),
                    name='Focus',
                    showlegend=False,
                )
            )

            fig.add_annotation(
                x=root1,
                y=0,
                text=f'({root1:.1f}, {0})',
                showarrow=True,
                arrowhead=2,
                ax=-20,
                ay=a_sign*30,
            )
            fig.add_annotation(
                x=root2,
                y=0,
                text=f'({root2:.1f}, {0})',
                showarrow=True,
                arrowhead=2,
                ax=20,
                ay=a_sign*30,
            )


        # if_has_no_roots:
        #     pass   

    if show_grid.value == 'Hide':
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
    else:
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(showgrid=True)


    if show_tick_labels.value == 'Hide':
        fig.update_xaxes(visible=False)
        fig.update_yaxes(visible=False)
    else:
        fig.update_xaxes(visible=True)
        fig.update_yaxes(visible=True)
    


    return (fig,)


@app.cell
def _(fig, mo):
    fig.update_layout(
        xaxis=dict(scaleanchor="y"),  # Link x-axis scale to y-axis
        yaxis=dict(scaleanchor="x"),  # Optional: ensures bidirectional link
    )
    mo.ui.plotly(fig)
    return


@app.cell
def _():
    return


@app.cell
def _():
    # df_cal = (
    #     pl.read_excel('assets/california_counties_wikipedia.xlsx')
    #     .lazy()
    #     .with_columns(
    #         # Normalize to CA county FIPS format (06001, 06013, ...)
    #         pl.concat_str([
    #             pl.lit('06'),
    #             pl.col('FIPS').cast(pl.Int64).cast(pl.String).str.zfill(3)
    #         ]).alias('FIPS'),
    #         pl.col('Established').cast(pl.UInt16),
    #         pl.col('Pop').cast(pl.UInt32),
    #         pl.col('Area_Sq_Mile').cast(pl.UInt16), 
    #         pl.col('Area_Sq_KM').cast(pl.UInt16),
    #         pl.col('County').str.strip_chars()
    #     )
    #     .with_columns(
    #         Pop_Density_Sq_Mile = 
    #             (pl.col('Pop')/pl.col('Area_Sq_Mile'))
    #             .round(1),
    #         Pop_Density_Sq_KM = (pl.col('Pop')/pl.col('Area_Sq_KM')).round(1)
    #     )
    #     .with_columns(
    #         Pop_Rank = pl.col('Pop').rank(method='min', descending=True),
    #         Pop_Density_Rank = pl.col('Pop_Density_Sq_Mile')
    #                             .rank(method='min', descending=True),
    #         Area_Rank = pl.col('Area_Sq_Mile').rank(method='min', descending=True),        
    #     )
    #     .sort('County', descending=False)
    #     .select([
    #         'County', 'Seat', 'Established', 
    #         'Pop',  'Pop_Rank', 
    #         'Area_Sq_Mile', 'Area_Sq_KM', 'Area_Rank',
    #         'Pop_Density_Sq_Mile', 'Pop_Density_Sq_KM', 'Pop_Density_Rank',   
    #         'Formation', 'Etymology', 'FIPS',
    #     ])
    #     .collect()
    # )
    # print(list(df_cal.columns))
    # df_cal
    return


@app.cell
def _():
    # print(f"{df_cal.get_column('Pop').sum() = :,}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Select a Data Viz parameter
    California has 58 Counties. Pick one of 3 demographics to be displayed in top 10 and bottom 10 horizontal bar charts
    """)
    return


@app.cell
def _():
    # demo = mo.ui.multiselect(
    #     ['Population', 'Population Density', 'Area'],
    #     max_selections=1,
    #     full_width=True,
    # )
    return


@app.cell
def _():
    # mo.center(demo)
    return


@app.cell
def _():
    # demo_view = demo.value[0] if demo.value else None
    return


@app.cell
def _():
    # demo_view
    return


@app.cell
def _():
    ### Marimo with Plotly
    return


@app.cell
def _():
    # print(f'display top 10 and bottom 10 charts by county {demo_view}')
    # fig1 = fig2 = go.Figure()

    # if demo_view == 'Population':
    #     fig1 = px.bar(
    #         df_cal.sort('Pop_Rank', descending=True).tail(10),
    #         x='Pop',
    #         y='County', 
    #         title = f'Top 10',subtitle = demo_view,
    #     )
    #     fig2 = px.bar(
    #         df_cal.sort('Pop_Rank', descending=True).head(10),
    #         x='Pop',
    #         y='County',
    #         title = f'Bottom 10', subtitle = demo_view,
    #     )

    # if demo_view == 'Population Density':
    #     fig1 = px.bar(
    #         df_cal.sort('Pop_Density_Sq_Mile', descending=False).tail(10),
    #         x='Pop_Density_Sq_Mile',
    #         y='County', 
    #         title = f'Top 10',subtitle = demo_view,
    #     )
    #     fig2 = px.bar(
    #         df_cal.sort('Pop_Density_Sq_Mile', descending=False).head(10),
    #         x='Pop_Density_Sq_Mile',
    #         y='County',
    #         title = f'Bottom 10', subtitle = demo_view,
    #     )

    # if demo_view == 'Area':
    #     fig1 = px.bar(
    #         df_cal.sort('Area_Sq_Mile', descending=False).tail(10),
    #         x='Area_Sq_Mile',
    #         y='County', 
    #         title = f'Top 10',subtitle = demo_view,
    #     )
    #     fig2 = px.bar(
    #         df_cal.sort('Area_Sq_Mile', descending=False).head(10),
    #         x='Area_Sq_Mile',
    #         y='County',
    #         title = f'Bottom 10', subtitle = demo_view,
    #     )
    # # Update layout to set custom height and width, offset y-labels from bars
    # w = 400
    # h = 400
    # fig1.update_layout(width=w, height=h, yaxis=dict(ticklabelstandoff=10))
    # fig2.update_layout(width=w, height=h, yaxis=dict(ticklabelstandoff=10))

    # # Wrap figures in mo.ui.plotly for reactive support
    # fig1_ui = mo.ui.plotly(fig1)
    # fig2_ui = mo.ui.plotly(fig2)
    # # Arrange them side‑by‑side in an HStack
    # layout = mo.hstack(
    #     [fig1_ui, fig2_ui],
    #     widths="equal"  # Equal width for both
    # )

    # # Display the layout
    # layout
    return


if __name__ == "__main__":
    app.run()
