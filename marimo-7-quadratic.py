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
def _(go):
    def annotate_point(
        fig, name, color, size, x=None, y=None, ax=None, ay=None, xanchor=None):
        my_x = x
        my_y = y
        if my_x is None:
            my_x = 0
        if my_y is None:
            my_y = 0
        if xanchor == None:
            xanchor ='center'
        my_text = ''
        if x is None:
            my_text = f'{name}: {my_y:.3f}'
        elif y is None:
            my_text = f'{name}: {my_x:.3f}'
        else:
            my_text = f'{name} ({my_x:.3f}, {my_y:.3f})'
        fig.add_trace(
            go.Scatter(
                x=[my_x], y=[my_y],
                mode='markers', marker=dict(size=size, color=color),
                name=name,
                showlegend=False,
            )
        )
        fig.add_annotation(
            x=my_x, y=my_y,
            text=f'{my_text}',
            showarrow=True,
            arrowhead=2,
            ax=ax,
            ay=ay,
            xanchor=xanchor
        )
        return fig

    return (annotate_point,)


@app.cell
def _(mo):
    a_number =  mo.ui.number(value=1.0)
    b_number =  mo.ui.number(value=-4.0)
    c_number =  mo.ui.number(value=3.0)
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
    show_grid = mo.ui.checkbox(value=False, label = 'Show Grid')
    show_vertex = mo.ui.checkbox(value=False, label = 'Vertex')
    show_focus = mo.ui.checkbox(value=False, label = 'Focus')
    show_directrix = mo.ui.checkbox(value=False,label = 'Directrix')
    show_roots = mo.ui.checkbox(value=False,label = 'Roots')
    return show_directrix, show_focus, show_grid, show_roots, show_vertex


@app.cell
def _(show_directrix, show_focus, show_grid, show_roots, show_vertex):
    print(f'{show_grid.value = }')
    print(f'{show_vertex.value = }')
    print(f'{show_focus.value = }')
    print(f'{show_directrix.value = }')
    print(f'{show_roots.value = }')

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
    # create a data with 1000 points before vertex and 1000 points after
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
    a_stack,
    annotate_point,
    b,
    b_stack,
    c,
    c_stack,
    go,
    h,
    has_one_root,
    has_two_roots,
    k,
    mo,
    root1,
    root2,
    show_directrix,
    show_focus,
    show_grid,
    show_roots,
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
    if show_vertex.value:
        fig = annotate_point(
            fig, 'Vertex', 'crimson', 4, x=h, y=k, ax=20, ay=a_sign*30)
   
    if show_focus.value:
        fig = annotate_point(
            fig, 'Focus', 'crimson', 4, x=h, y= y_focus, ax=20, ay=-a_sign*30)
   
    if show_directrix.value:
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
        y_max = y_directrix + a_sign*(3*abs(y_focus-y_directrix))
        y_min = y_directrix - abs(k - y_directrix)  
        fig.update_yaxes(range = [y_min, y_max])
    else:
        fig.update_yaxes(
            range = [
                y_directrix, 
                y_directrix + (3*(y_focus-y_directrix))
            ]
        )

    print(f'{y_directrix = }')
    print(f'{y_focus = }')

    if show_roots.value:
        if has_one_root: # if only one root, it is the vertex
            pass
        
        if has_two_roots:
            fig = annotate_point(
                fig, 'Root 1', 'crimson', 2, x=root1, ax=-50, ay=0, xanchor='right')
            fig = annotate_point(
                fig, 'Root 2', 'crimson', 2, x=root2, ax=50, ay=0, xanchor='left')

        # if_has_no_roots:
        #     pass   

    if show_grid.value:
        fig.update_xaxes(showgrid=True, visible=True)
        fig.update_yaxes(showgrid=True, visible=True)
    else:
        fig.update_xaxes(showgrid=False, visible=False)
        fig.update_yaxes(showgrid=False, visible=False)

   
    # fig.update_layout(
    #     xaxis=dict(scaleanchor="y"),  # Link x-axis scale to y-axis
    #     yaxis=dict(scaleanchor="x"),  # Optional: ensures bidirectional link
    # )

    mo.vstack([
        mo.hstack([
             a_stack, 
             b_stack, 
             c_stack
        ]),

        mo.hstack([
            mo.ui.plotly(fig),
            mo.vstack([
                show_grid,
                show_vertex,
                show_focus,
                show_directrix,
                show_roots
                ],
            ),
        ],
        widths=[3,1])
    ])
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


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
