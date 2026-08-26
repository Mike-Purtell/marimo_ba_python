# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "fastexcel==0.20.2",
#     "marimo>=0.23.16",
#     "numpy==2.5.2",
#     "plotly[express]==6.9.0",
#     "polars==1.43.2",
# ]
# ///

import marimo

__generated_with = "0.24.0"
app = marimo.App(layout_file="layouts/marimo_slides_2026_08_27.slides.json")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import numpy
    import polars as pl
    import plotly.express as px
    import plotly.graph_objects as go
    import math
    image_path = 'assets/'
    return go, image_path, math, pl, px


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Marimo: Next Generation of Python Notebooks

    Mike Purtell
    <br>
    Bay Area Python Interest Group
    <br>
    August 27, 2026<br><br><br>
    - Principal Test Engineeer for Cadence Design Systems
    - Analysis and visualization of large data sets is a passion and profession
    - User of python for data analysis since 2019 (started with jupyter, pandas, matplotlib)
    - Favorite tools today are Polars, Plotly, and leaning into Marimo
    - San Jose resident since 2004, Silicon Valley since 1981. Grew up in Albany NY
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Agenda
    <br>
    - Marimo overview
    - Reactivity
    - UI elements/widgets
    - Data Frames
    - Apps/ visualizations
    - Getting started/Getting Help
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <br>Python notebooks are interactive, this presentation is too. Comments or questions welcome anytime.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    <br>This is not a slide deck to accompany the demo. This slide deck is the demo.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Marimo - A Reactive Notebook for Python
    - Reactive Execution Model – Automatically updates outputs when inputs change
    - Lightweight & Script-Based – Stored as plain .py files, version-control friendly
    - Interactive UI – Supports widgets, forms, and live visualizations
    - Seamless Data Exploration – Ideal for analysis, prototyping, and app building
    - Export & Share – Save as HTML, present as slides, or deploy as web apps
    - Reproducible Workflows – Deterministic execution ensures consistent results
    """)
    return


@app.cell
def _(image_path, mo):
    mo.vstack([
        mo.md('''#Fun Fact  
            Mari (毬 まり) means "ball" and mo (藻 も) means "algae" in Japanese.
            Marimo (毬藻 or まりも) refers to algae that 
            clumps together to form a small sphere called a "marimo moss ball". 
            Since 1952 the marimo from Lake Akan in Hokkaidō have been designated as 
            special natural treasures of Japan because of their almost perfectly round shape, 
            large size and velvet-like surface.<br><br><br>
            '''),
            mo.hstack([
                mo.center(mo.image(f'{image_path}Marimo_lake_akann.png', rounded=True,width=300)),
                mo.center(mo.image(f'{image_path}/Marimo.png', rounded=True,width=300)),
            ])
    ])
    return


@app.cell
def _(image_path, mo):
    def _attribution_card(name, image_name, description):
        return mo.hstack(
            [
                mo.image(f"{image_path}{image_name}", width=175, rounded=True,
                         style={
                            "max-width": "100%",
                            "border-radius": "8px",
                            "box-shadow": "0 4px 8px rgba(0,0,0,0.2)",
                            "display": "block",
                            "margin": "auto"
                        },),
                mo.accordion({name: mo.md(description)}),
            ],
            widths="equal",
        )

    mo.vstack([
        mo.md("#Marimo Leadership"),
        mo.vstack([
            _attribution_card(
                "Vincent Warmerdam (Founding Engineer)",
                "vincent.png",
                """
                 Vincent is a senior data professional with many meaningful contributions to the PyData stack. He has 
                 pubished many videos on the Marimo YouTube channel. I have seen quite a few, and learned so much.
                """,
            ),
           _attribution_card(
                "Akshay Agrawal(Co-Founder, CEO)",
                "Akshay.png",
                """
                Akshay is a former engineer at Google Brain, where he helped build TensorFlow, and is a NeurIPS-published
                PhD from Stanford University, where he focused on vector embeddings and machine learning.
                """,
            ),
            _attribution_card(
                "Sarah Tsai (Developer Relations)",
                "sarah.png",
                """
                  Sarah is a former data scientist at Genentech, where she built interactive visual analytics dashboards,
                  and led campus community growth as Bumble's events manager at UC Berkeley.
                """,
            ),
        ], heights="equal"),
    ])
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md("#Jupyter/Marimo Demo"),
        mo.md("mo.accordion"),
        mo.hstack([
            mo.vstack([
                mo.accordion(
                    {
                        "Jupyter": mo.md(
                            """
                            - Classic, linear execution with hidden state
                            - Stores large .ipynb JSON files (often multiple MB with outputs)
                            - Multi-language support: Python, Julia, R
                            - Outputs and visualizations baked into the notebook, making git diffs heavy
                            """
                        )
                    }
                ).style(max_height="300px", overflow="auto").left(),
                mo.md(""),
                mo.accordion(
                    {
                        "Marimo": mo.md(
                            """
                            - Reactive execution with automatic dependency tracking, natural mechanism for callbacks
                            - Saves pure .py files—lightweight, git-friendly, no JSON output blobs
                            - Python-only, with focused and streamlined support
                            - Interactive widgets and app-like behavior without hidden state
                            """
                        )
                    }
                ).style(max_height="300px", overflow="auto").left(),
            ]),
            mo.Html(""),
            mo.image("assets/Paws.png", width=200, caption="Let's Paws for notebook demos"),
        ]),
    ])
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md('#Dependency Graph'),  
        mo.image('assets//dependency_graph.png')
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # UI elements
    <br><br>
    Cells can output interactive UI elements. Interacting with a UI
    element **automatically triggers notebook execution**: when
    you interact with a UI element, its value is sent back to Python, and
    every cell that references that element is re-run.
    <br><br>
    marimo provides a library of UI elements to choose from under
    marimo.ui.
    """)
    return


@app.cell
def _(mo):
    slider_max = 9  # 10 pets are allowed. slider max of 9 forces at least one of each type
    pet_slider = mo.ui.slider(1, slider_max, 1, label="Cats or Dogs?", value=5)
    return (pet_slider,)


@app.cell
def _(pet_slider):
    cat_num = pet_slider.value
    dog_num = 10 - cat_num
    return cat_num, dog_num


@app.cell
def _(cat_num, dog_num, mo, pet_slider):
    mo.vstack([
        mo.md("#Slider demo, pick dogs and cats, 10 total"),
        mo.md(
            f"""{pet_slider} {cat_num} Cats, {dog_num} Dogs """
        ),
        mo.md("##" + "🐱" * cat_num + f'  {cat_num} Cats'),
        mo.md("##" + "🐶 " *  dog_num + f' {dog_num} Dogs'),
    ])
    return


@app.cell
def _(mo):
    radio = mo.ui.radio(
        options=sorted(
            [
                "Green Day",
                "Jefferson Airplane",
                "Metallica",
                "Grateful Dead",
                "Santana",
                "Journey",
                "Petrichor",
            ]
        ),
        label="Your favorite Bay Area band (pick 1)",
    )
    multiselect = mo.ui.multiselect(
        options=["Springfield", "Chicago (tentative)", "New York (tentative)", "Los Angeles (tentative)"],
        label="Simpson reference<br>Best city to see a Rolling Stones concert?",
        max_selections=2,
    )
    checkbox = mo.ui.checkbox(label="yes I read the T's and C's", value=False)
    return checkbox, multiselect, radio


@app.cell
def _(checkbox, mo, multiselect, radio):
    mo.vstack([
        mo.md("<h1>Interactive widgets</h1>"),
        mo.hstack(
            [
                radio,
                mo.left(mo.Html(radio.value if radio.value is not None else "no selection yet")),
            ],
            widths="equal",
        ),
        mo.Html("<br>"),
        mo.hstack(
            [
                multiselect,
                mo.center(
                    mo.Html(
                        ", ".join(multiselect.value)
                        if multiselect.value is not None
                        else "no selection yet"
                    )
                ),
            ],
            widths="equal",
        ),
        mo.Html("<br>"),
        mo.hstack(
            [
                checkbox,
                mo.left(
                    mo.Html(
                        "Have read the Ts and Cs" if checkbox.value else "Have NOT read the Ts and Cs"
                    )
                ),
            ],
            widths="equal",
        ),
    ])
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md(
            """#Dataframes

            Pagination

            Interactive column select, row filters and other transforms

            Save csv, parquet or other formats

            Interactive built-in data viz, save code to python
            """
        ),
    ])
    return


@app.cell
def _(mo, pl):
    df_polars = (
        pl.DataFrame({str(i): [j * i for j in range(1, 11)] for i in range(1, 11)})
        .with_columns(pl.all().cast(pl.UInt8))
    )
    mo.vstack([
        mo.md("#Single Digit Times Table<br><sup>mo.ui.table(dataframe)</sup>"),
        mo.ui.table(df_polars),
    ])
    return


@app.cell
def _(mo, pl):
    # Load the county data once; later cells react to this dataframe.
    # The chained Polars operations clean, calculate, rank, and collect the data.
    df_cal = (
        pl.read_excel("assets/california_counties_wikipedia.xlsx")
        .lazy()
        .with_columns(
            pl.col("Established").cast(pl.UInt16),
            pl.col("Pop").cast(pl.UInt32),
            pl.col("Area_Sq_Mile").cast(pl.UInt16),
            pl.col("Area_Sq_KM").cast(pl.UInt16),
            pl.col("County").str.strip_chars(),
        )
        .with_columns(
            Pop_Density_Sq_Mile=(pl.col("Pop") / pl.col("Area_Sq_Mile")).round(1),
            Pop_Density_Sq_KM=(pl.col("Pop") / pl.col("Area_Sq_KM")).round(1),
        )
        .with_columns(
            Pop_Rank=pl.col("Pop").rank(method="min", descending=True),
            Pop_Density_Rank=pl.col("Pop_Density_Sq_Mile").rank(method="min", descending=True),
            Area_Rank=pl.col("Area_Sq_Mile").rank(method="min", descending=True),
        )
        .sort("County", descending=False)
        .select(
            [
                "County",
                "Seat",
                "Established",
                "Pop",
                "Pop_Rank",
                "Area_Sq_Mile",
                "Area_Sq_KM",
                "Area_Rank",
                "Pop_Density_Sq_Mile",
                "Pop_Density_Sq_KM",
                "Pop_Density_Rank",
                "Formation",
                "Etymology",
            ]
        )
        .collect()
    )

    # This widget is a public value owned by this cell.
    # Other cells should read demo.value rather than create another demo.
    demo = mo.ui.radio(
        options=["Population", "Population Density", "Area"],
        value="Population",
        label="",
        inline=True,
    )
    return demo, df_cal


@app.cell
def _(mo):
    get_selected_county, set_selected_county = mo.state(None)
    return get_selected_county, set_selected_county


@app.cell
def _(demo, df_cal, get_selected_county, go, mo, pl, px):
    # Reading demo.value creates a reactive dependency on the radio widget.
    # When the selection changes, marimo reruns this cell and its dependents.
    demo_view = demo.value if demo.value else None
    print(f"display top 10 and bottom 10 charts by county {demo_view}")
    # Start with empty figures so both chart variables are defined for every choice.
    fig1 = fig2 = go.Figure()

    if demo_view == "Population":
        fig1 = px.bar(
            df_cal.sort("Pop_Rank", descending=True).tail(10),
            x="Pop",
            y="County",
            title="Top 10",
            subtitle=demo_view,
            labels={"Pop": "Population"},
        )
        fig2 = px.bar(
            df_cal.sort("Pop_Rank", descending=True).head(10),
            x="Pop",
            y="County",
            title="Bottom 10",
            subtitle=demo_view,
            labels={"Pop": "Population"},
        )

    if demo_view == "Population Density":
        fig1 = px.bar(
            df_cal.sort("Pop_Density_Sq_Mile", descending=False).tail(10),
            x="Pop_Density_Sq_Mile",
            y="County",
            title="Top 10",
            subtitle=demo_view,
            labels={"Pop_Density_Sq_Mile": "Population per Square Mile"},
        )
        fig2 = px.bar(
            df_cal.sort("Pop_Density_Sq_Mile", descending=False).head(10),
            x="Pop_Density_Sq_Mile",
            y="County",
            title="Bottom 10",
            subtitle=demo_view,
            labels={"Pop_Density_Sq_Mile": "Population per Square Mile"},
        )

    if demo_view == "Area":
        fig1 = px.bar(
            df_cal.sort("Area_Sq_Mile", descending=False).tail(10),
            x="Area_Sq_Mile",
            y="County",
            title="Top 10",
            subtitle=demo_view,
            labels={"Area_Sq_Mile": "Area (Square Miles)"},
        )
        fig2 = px.bar(
            df_cal.sort("Area_Sq_Mile", descending=False).head(10),
            x="Area_Sq_Mile",
            y="County",
            title="Bottom 10",
            subtitle=demo_view,
            labels={"Area_Sq_Mile": "Area (Square Miles)"},
        )

    # The selected county comes from another cell through marimo state.
    selected_county = get_selected_county()

    # These names belong to this cell. Marimo requires each public name to
    # have one owner, so another cell must not define h or w again.
    h = 400
    w = 400
    fig1.update_layout(
        width=w,
        height=h,
        template="plotly_dark",
        yaxis=dict(ticklabelstandoff=10),
    )
    fig2.update_layout(
        width=w,
        height=h,
        template="plotly_dark",
        yaxis=dict(ticklabelstandoff=10),
    )
    # Apply the same click and selection styling to both charts.
    for fig in (fig1, fig2):
        fig.update_layout(clickmode="event+select")
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
            selected=dict(marker=dict(color="green")),
            unselected=dict(marker=dict(color="lightgray", opacity=0.65)),
        )

    fig1_ui = mo.ui.plotly(fig1)
    fig2_ui = mo.ui.plotly(fig2)

    description = ""
    if demo_view == "Population":
        description = mo.Html(
            """
            <div style='padding: 0.75rem 1rem; border: 1px solid var(--border-color);'>
            Los Angeles County with nearly 10 million has a larger population than
            40 other US States. Alpine County at the bottom has slightly more than 1,000 people.
            </div>
            """
        )
    elif demo_view == "Population Density":
        description = mo.Html(
            """
            <div style='padding: 0.75rem 1rem; border: 1px solid var(--border-color);'>
            San Francisco dominates the
            population density metric with 18K per square mile, 4x more than the second highest Orange County.
            Inyo, Alpine, and Modoc each have about 2 people per square mile.
            </div>
            """
        )
    elif demo_view == "Area":
        description = mo.Html(
            """
            <div style='padding: 0.75rem 1rem; border: 1px solid var(--border-color);'>
            San Bernardino, the largest county in the United States, is larger than
            9 other states, including New Jersey and Massachusetts. The Bay Area dominates the small county list,
            with the 4 smallest counties, and 6 of the 10 smallest counties.
            </div>
            """
        )

    selected_county_row = (
        df_cal.filter(pl.col("County") == selected_county).row(0, named=True)
        if selected_county
        else None
    )
    if selected_county_row:
        county_info = mo.Html(
            f"""
            <div style='padding: 0.75rem 1rem; border: 1px solid var(--border-color);'>
                <strong>{selected_county_row['County']} County</strong><br>
                Formation: {selected_county_row['Formation']}<br>
                Etymology: {selected_county_row['Etymology']}
            </div>
            """
        )
    else:
        county_info = mo.Html("")

    dataframe_info = """
    SHOW ME: This polars dataframe is used for all visualizations in this
    notebook. Use the Transform block to interactively process a dataframe with a GUI,
    no coding required. When you're done, you can copy the code that the GUI
    generated for you and paste it into your notebook.
    """
    return county_info, description, fig1_ui, fig2_ui


@app.cell
def _(df_cal, mo):
    mo.vstack([
        mo.md("#California Counties - population statistics"),
        mo.md('df_cal'),
       df_cal
    ])
    return


@app.cell
def _(county_info, demo, description, fig1_ui, fig2_ui, mo):
    mo.vstack([
        mo.Html("<br>"),
        mo.left(mo.md(f"#California County {demo.value}")),
        mo.left(mo.md('Tip #1: hover over bar to see county statistics')),
        mo.left(mo.md('Tip #2: click on an bar for more information about that county')),
        mo.hstack([
            description,
            county_info,
        ]),
        mo.left(demo),
        mo.hstack([fig1_ui, fig2_ui], widths="equal"),
    ])
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md(
            """#Marimo Notebooks as Apps

        - Reactivity makes callbacks a breeze

        -  Run apps on local machine, deploy to Molab, or run from GitHub

        - Share with colleagues who don't want to see code

            """
        ),
    ])
    return


@app.cell
def _():
    return


@app.cell
def _(fig1_ui, fig2_ui, set_selected_county):
    # Plotly reports clicked points through the UI objects.
    # Updating marimo state causes the county-information cells to rerun.
    selected_points = fig1_ui.points + fig2_ui.points
    if selected_points:
        set_selected_county(selected_points[0].get("y"))
    return


@app.cell
def _(go):
    def annotate_point(fig, name, color, size, x=None, y=None, textposition=None):
        point_x = 0 if x is None else x
        point_y = 0 if y is None else y
        textposition = "below" if textposition is None else textposition
        fig.add_trace(
            go.Scatter(
                x=[point_x],
                y=[point_y],
                mode="markers+text",
                text=name,
                textposition=textposition,
                marker=dict(size=size, color=color),
                showlegend=False,
            )
        )
        return fig

    return (annotate_point,)


@app.cell
def _(mo):
    a_number = mo.ui.number(value=1.0)
    b_number = mo.ui.number(value=-4.0)
    c_number = mo.ui.number(value=3.0)
    return a_number, b_number, c_number


@app.cell
def _(a_number, b_number, c_number):
    # Widget values are read here and become reactive inputs for the math cells.
    a = a_number.value
    a_legal = abs(a) > 0
    a_sign = 1 if a > 0 else -1
    b = b_number.value
    c = c_number.value
    return a, a_legal, a_sign, b, c


@app.cell
def _(a_number, b_number, c_number, mo):
    a_stack = mo.vstack([mo.md("a: (x<sup>2</sup> term)"), a_number])
    b_stack = mo.vstack([mo.md("b: (x) term:"), b_number])
    c_stack = mo.vstack([mo.md("c: (constant)"), c_number])
    return a_stack, b_stack, c_stack


@app.cell
def _(a, b, c):
    # The discriminant tells us how many real roots the quadratic has:
    # positive means two, zero means one, and negative means none.
    has_two_roots = False
    has_one_root = False
    has_no_roots = False
    if a != 0:
        discriminant = (b ** 2) - (4 * a * c)
        has_no_roots = discriminant < 0
        has_one_root = discriminant == 0
        has_two_roots = discriminant > 0
    else:
        has_one_root = b != 0
    return has_one_root, has_two_roots


@app.cell
def _(a, b, c, has_one_root, has_two_roots, math):
    # Keep separate names for the possible roots because later cells display them.
    # This cell owns these names; dependent cells only read them.
    root = None
    root1 = None
    root2 = None

    # If a is zero, the equation is linear rather than quadratic.
    if a == 0:
        if b == 0:
            print("No root: this is not a quadratic equation and does not intersect y = 0")
        else:
            root = -c / b
            print(f"Linear equation, one root, intersects (0, {root:.3f})")
    elif has_one_root:
        root = -b / (2 * a)
    elif has_two_roots:
        root_discriminant = math.sqrt(b ** 2 - (4 * a * c))
        root1 = ((-b) + root_discriminant) / (2 * a)
        root2 = ((-b) - root_discriminant) / (2 * a)
        root1, root2 = sorted((root1, root2))

    if has_one_root and a != 0:
        print(f"One root, intersects (0, {root:.3f})")
    elif has_two_roots:
        print(f"Two roots, intersects (0, {root1:.3f}), (0, {root2:.3f})")
    return root, root1, root2


@app.cell
def _(mo):
    show_grid = mo.ui.checkbox(value=False, label="Show Grid")
    show_vertex = mo.ui.checkbox(value=False, label="Vertex")
    show_focus = mo.ui.checkbox(value=False, label="Focus")
    show_directrix = mo.ui.checkbox(value=False, label="Directrix")
    show_roots = mo.ui.checkbox(value=False, label="Roots")
    scale_xy = mo.ui.checkbox(value=False, label="Scale XY")
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
    # Calculate the vertex (parabola_h, k), focus, and focus height.
    # parabola_h is intentionally unique: marimo does not allow a public name
    # to be defined by more than one cell.
    if a_legal:
        parabola_h = -b / (2 * a)
        k = c - (b ** 2) / (4 * a)
        x_focus = parabola_h
        y_focus = k + (1 / (4 * a))
    else:
        parabola_h = 0
        k = 0
        x_focus = 0
        y_focus = 0
        print("Invalid value of a: it cannot be 0 for a parabola")
    return k, parabola_h, x_focus, y_focus


@app.cell
def _(a, a_legal, b, c, parabola_h, x_focus):
    # Build x-values around the vertex, then calculate y = ax^2 + bx + c.
    # This cell reads parabola_h from the previous cell; it does not redefine it.
    if a_legal:
        x_offset = 1 / (2 * a)
        x_left, x_right = sorted((parabola_h - x_offset, parabola_h + x_offset))
        width = x_right - x_left
        x_start = x_focus - (5 * width)
        x_stop = x_focus + (5 * width)
        x_vals = [x_start + i * (x_stop - x_start) / 1000 for i in range(1001)]
        y_vals = [a * x * x + b * x + c for x in x_vals]
    else:
        x_left = x_right = width = 1.0
        x_vals = [-5 + i / 100 for i in range(1001)]
        y_vals = [b * x + c for x in x_vals]
    return width, x_vals, y_vals


@app.cell
def _(a, a_legal, k):
    # The directrix is horizontal and lies opposite the focus from the vertex.
    # This cell owns y_directrix so the plotting cell can react to it.
    y_directrix = k - (1 / (4 * a)) if a_legal else None
    return (y_directrix,)


@app.cell
def _(
    a,
    a_legal,
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
    has_one_root,
    has_two_roots,
    k,
    mo,
    parabola_h,
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
    # Create the graph from the x/y points calculated in the earlier cell.
    # parabola_fig has a unique name because marimo gives each public variable one owner.
    parabola_fig = go.Figure(data=go.Scatter(x=x_vals, y=y_vals, showlegend=False))

    # The subtitle explains which root case is currently displayed.
    if has_one_root and a != 0:
        subtitle = f"One Root at x = {root:.6f}".rstrip("0").rstrip(".")
    elif has_two_roots:
        subtitle = f"Two Roots at x = {root1:.6f}, {root2:.6f}"
    else:
        subtitle = "No Real Roots" if a != 0 else "Linear Equation"

    if a_number.value == -1:
        a_expression = "y = -x<sup>2</sup>"
    elif a_number.value == 1:
        a_expression = "y = x<sup>2</sup>"
    elif a_number.value == 0:
        a_expression = "y = "
    else:
        a_expression = f"y = {a}x<sup>2</sup>"

    if b_number.value == -1:
        b_expression = " - x"
    elif b_number.value == 1:
        b_expression = " + x"
    elif b_number.value == 0:
        b_expression = ""
    elif b_number.value > 0:
        b_expression = f" + {b}x"
    else:
        b_expression = f" - {abs(b)}x"

    if c_number.value == 0:
        c_expression = ""
    elif c_number.value > 0:
        c_expression = f" + {c}"
    else:
        c_expression = f" - {abs(c)}"

    title = f"{a_expression}{b_expression}{c_expression}"
    parabola_fig.update_layout(
        title=dict(
            text=title,
            x=0.5,
            xanchor="center",
            font=dict(family="Arial, sans-serif", size=26, color="white"),
            subtitle=dict(
                text=subtitle,
                font=dict(family="Arial, sans-serif", size=15, color="dimgray"),
            ),
        )
    )
    # Add optional markers for the vertex, focus, directrix, and roots.
    marker_size = 6

    # Each checkbox is another reactive input, so changing one reruns this cell.
    if show_vertex.value and a_legal:
        textposition = "bottom center" if a_sign > 0 else "top center"
        parabola_fig = annotate_point(
            parabola_fig,
            "Vertex",
            "crimson",
            marker_size,
            x=parabola_h,
            y=k,
            textposition=textposition,
        )

    if show_focus.value and a_legal:
        textposition = "bottom center" if a_sign < 0 else "top center"
        parabola_fig = annotate_point(
            parabola_fig,
            "Focus",
            "crimson",
            marker_size,
            x=parabola_h,
            y=y_focus,
            textposition=textposition,
        )

    if show_directrix.value and y_directrix is not None:
        parabola_fig.add_hline(y=y_directrix, line_dash="dot")

    if show_roots.value:
        if has_one_root and a != 0:
            textposition = "bottom center" if a_sign < 0 else "top center"
            parabola_fig = annotate_point(
                parabola_fig,
                "Root",
                "crimson",
                marker_size,
                x=root,
                textposition=textposition,
            )
        elif has_two_roots:
            parabola_fig = annotate_point(
                parabola_fig,
                "Root 1",
                "crimson",
                marker_size,
                x=root1,
                textposition="middle left",
            )
            parabola_fig = annotate_point(
                parabola_fig,
                "Root 2",
                "crimson",
                marker_size,
                x=root2,
                textposition="middle right",
            )

    # Show or hide the grid without rebuilding the underlying data.
    if show_grid.value:
        parabola_fig.update_xaxes(showgrid=True, visible=True)
        parabola_fig.update_yaxes(showgrid=True, visible=True)
    else:
        parabola_fig.update_xaxes(showgrid=False, visible=False)
        parabola_fig.update_yaxes(showgrid=False, visible=False)

    # Choose plot ranges that keep the important parabola geometry visible.
    if a_legal:
        y_range_max = y_directrix + a_sign * (3 * abs(y_focus - y_directrix))
        y_range_min = y_directrix - (a_sign * 0.1 * abs(k - y_directrix))
        x_range_max = x_focus + (2 * width)
        x_range_min = x_focus - (2 * width)
        x_range = [x_range_min, x_range_max]
        y_range = sorted([y_range_min, y_range_max])
        if scale_xy.value:
            parabola_fig.update_layout(xaxis=dict(scaleanchor="y"), yaxis=dict(scaleanchor="x"))
        else:
            parabola_fig.update_yaxes(range=y_range)
        parabola_fig.update_xaxes(range=x_range)

    parabola_fig.update_layout(template="plotly_dark")

    mo.vstack([
        mo.md("#Quadratic Analyzer"),
        mo.hstack([a_stack, b_stack, c_stack]),
        mo.hstack(
            [
                mo.ui.plotly(parabola_fig),
                mo.vstack([
                    show_grid,
                    show_vertex,
                    show_focus,
                    show_directrix,
                    show_roots,
                    scale_xy,
                ]),
            ],
            widths=[3, 1],
        ),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Getting Started, Getting Help
    1. https://docs.marimo.io/getting_started/
    2. Pair with AI: marimo-pair, marimo-agent
    3. Get VS Code Marimo add-on
    4. GitHub: https://www.github.com/marimo-team/marimo/tree/main/examples
    5. Marimo Discord Channel
    6. Marimo YouTube Channel
    """)
    return


@app.cell
def _(image_path, mo):
    mo.vstack([
        mo.md('''#Molab  
             https://molab.marimo.io/notebooks'''),
        mo.image(f'{image_path}MoLab.png')
    ])
    return


@app.cell
def _(image_path, mo):
    mo.vstack([
        mo.md('''#Git Repo for this Presentation - Thank you for coming
        https://github.com/Mike-Purtell/marimo_ba_python<br>'''),
        mo.image(f'{image_path}GitHub.png')
    ])
    return


if __name__ == "__main__":
    app.run()
