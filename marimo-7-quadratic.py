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
    import polars as pl
    import math

    return go, math


@app.cell
def _(go):
    def annotate_point(
        fig, name, color, size, x=None, y=None, ax=None, ay=None, xanchor=None):
        my_x = x
        my_y = y
        my_ax = ax
        my_ay = ay
        if my_x is None:
            my_x = 0
        if my_y is None:
            my_y = 0
        if my_ax is None:
            my_ax = 0
        if my_ay is None:
            my_ay = 0

        if xanchor == None:
            xanchor ='center'
        my_text = ''
        if x is None:
            my_text = f'{name} {my_y:.3f}'
        elif y is None:
            my_text = f'{name} {my_x:.3f}'
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
            arrowwidth=3,
            arrowcolor='white',
            ax=my_ax,
            ay=my_ay,
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
def _(a_number, b_number, c_number):
    a = a_number.value
    a_legal = False
    if abs(a) > 0:
        a_legal = True
    a_sign = 1 if a > 0 else -1 # 1 of parabola opens upward, -1 if downward

    b = b_number.value
    c = c_number.value
    return a, a_legal, a_sign, b, c


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
    if a == 0:
        if b == 0:
            print('No root: this is not a quadratic equation and does not intersect y = 0')
        else:
            root = -c / b
            print(f'Linear equation, one root, intersects (0, {root:.3f})')


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
    return root, root1, root2


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
    scale_xy = mo.ui.checkbox(value=False,label = 'Scale_XY')
    return (
        scale_xy,
        show_directrix,
        show_focus,
        show_grid,
        show_roots,
        show_vertex,
    )


@app.cell
def _(a, a_legal, b, c):
    # Conventional vertex coordiates are h, k. For upward facing parabolas, the vertex
    # is the minimum point on the y-axis, or maximum for downward facing parabola
    print(f'{a_legal = }')
    if a_legal:
        h = -b/(2*a)
        k = c - ((b**2)/(4*a))
        x_focus = h
        y_focus = c - ((b**2)/(4*a)) + (1/(4*a))
        print(f'vertex at  ({h}, {k})')
    else:
        print('illeval value of a, cannot be 0')
    return h, k, x_focus, y_focus


@app.cell
def _(x_focus, y_focus):
    # focus

    print(f'focus at  ({x_focus}, {y_focus})')
    return


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
    return x_vals, y_vals


@app.cell
def _(a, b, c):
    y_directrix = c - ((b**2)/(4*a)) - (1/(4*a)) #   k - a
    return (y_directrix,)


@app.cell
def _(
    a,
    a_number,
    a_sign,
    a_stack,
    annotate_point,
    b,
    b_number,
    b_stack,
    c,
    c_number,
    c_stack,
    go,
    h,
    has_one_root,
    has_two_roots,
    k,
    mo,
    root,
    root1,
    root2,
    scale_xy,
    show_directrix,
    show_focus,
    show_grid,
    show_roots,
    show_vertex,
    width,
    x_focus,
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
    if has_one_root:
        my_subtitle = f'One Root at x = {root:.1f}'
    elif has_two_roots:
        my_subtitle = f'Two Roots at x = {root1:.1f}, {root2:.1f}'
    else:
        my_subtitle = 'No Real Roots'

    a_expression = f'x<sup>2</sup>' if a == 1 else f'{a}x<sup>2</sup>'

    a_expression = ''
    if a_number.value == -1:
        a_expression = f'-x<sup>2</sup>'
    elif a_number.value == 1:
        a_expression = f'x<sup>2</sup>'
    else:
        a_expression = f'{a}x<sup>2</sup>'
    

    b_expression = '' # intialize
    if b_number.value == -1:
        b_expression = f' - x'
    elif b_number.value == 1:
        b_expression = f' + x'
    elif b_number.value == 0:
        b_expression = ''
    elif b_number.value  > 0.0:
        b_expression = f' + {b}x'
    else:
        b_expression = f' - {abs(b)}x'
    
    c_expression = ''
    if c_number.value == 0:
        c_expression = ''
    elif c_number.value > 0:
        c_expression = f' + {c}'
    elif c_number.value < 0:
        c_expression = f' - {abs(c)}'

    my_title = f'{a_expression} {b_expression} {c_expression}'
    print(f'{a_expression = }')
    print(f'{b_expression = }')
    print(f'{c_expression = }')
    print(f'{my_title = }')

    fig.update_layout(
        title=dict(
            text=my_title,
            x=0.5,
            xanchor='center',
            font=dict(family='Arial, sans-serif', size=26, color='white'),
            subtitle=dict(
                text=my_subtitle,
                font=dict(family='Arial, sans-serif', size=15, color='dimgray'),
            ),
        ),
    )
    marker_size = 6
    if show_vertex.value:
        fig = annotate_point(
            fig, 'Vertex', 'crimson', 4, x=h, y=k, ax=50, ay=a_sign*30)
   
    if show_focus.value:
        fig = annotate_point(
            fig, 'Focus', 'crimson', 4, x=h, y=y_focus, ax=50, ay=-a_sign*30)
   
    if show_directrix.value:
        fig.add_hline(
            y = y_directrix, # color='green',
            line_dash="dot",
            annotation_text=f'Directrix, <br>y = {y_directrix:.3f}',
            annotation_position="right", # Positions text at right end of line
            annotation_font_size=14,
            annotation_font_color="blue"
        )

    print(f'{show_grid.value = }')
    print(f'{show_vertex.value = }')
    print(f'{show_focus.value = }')
    print(f'{show_directrix.value = }')
    print(f'{show_roots.value = }')
    print(f'{y_directrix = }')
    print(f'{y_focus = }')

    if show_roots.value:
        if has_one_root: # if only one root, it is the vertex
            fig = annotate_point(
                fig, 'Root 1', 'crimson', 2, x=root, ax=-50, ay=0, xanchor='right')

        if has_two_roots:
            fig = annotate_point(
                fig, 'Root 1<br>', 'crimson', 2, x=root1, 
                ax=-50, ay=0, xanchor='right')
            fig = annotate_point(
                fig, 'Root 2<br>', 'crimson', 2, x=root2, 
                ax=50, ay=0, xanchor='left')

        # if_has_no_roots:
        #     pass   

    if show_grid.value:
        fig.update_xaxes(showgrid=True, visible=True)
        fig.update_yaxes(showgrid=True, visible=True)
    else:
        fig.update_xaxes(showgrid=False, visible=False)
        fig.update_yaxes(showgrid=False, visible=False)



    max_y_val = max(y_vals)
    min_y_val = min(y_vals)
    span_y_vals = abs(max_y_val - min_y_val)
    y_range_max = y_directrix + a_sign*(3*abs(y_focus-y_directrix))
    y_range_min = y_directrix - (a_sign*0.1*abs(k - y_directrix))
    x_range_max = x_focus + (2 * width)
    x_range_min = x_focus - (2 * width)

    print(f'{y_range_min = }')
    print(f'{y_range_max = }')
    print(f'{x_range_min = }')
    print(f'{x_range_max = }')


    if scale_xy.value:
        fig.update_layout(
            xaxis=dict(scaleanchor="y"),  # Link x-axis scale to y-axis
            yaxis=dict(scaleanchor="x"),  # Optional: ensures bidirectional link
        )
        fig.update_xaxes(range = [x_range_min, x_range_max])
    else:  
        fig.update_yaxes(range = sorted([y_range_min, y_range_max],reverse=False))
        fig.update_xaxes(range = [x_range_min, x_range_max])

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
                show_roots,
                scale_xy
                ],
            ),
        ],
        widths=[3,1])
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    _df = mo.sql(
        f"""

        """
    )
    return


if __name__ == "__main__":
    app.run()
