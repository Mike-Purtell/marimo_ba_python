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
app = marimo.App(layout_file="layouts/mp_marimo_2026_08_27.slides.json")


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


@app.cell
def _(mo):
    mo.vstack([
        mo.md(
            '''
            ## Marimo: Next generation of python notebooks 🌊🍃
            Mike Purtell
            Bay Area Python Interest Group
            August 27, 2026
            '''
        ),
    ])
    return


@app.cell
def _(image_path, mo):
    mo.vstack([
        mo.md('''
            ## Fun Fact
            Mari (毬 まり) means "ball" and mo (藻 も) means "algae" in Japanese.
            Marimo (毬藻 or まりも) refers to algae that 
            clumps together to form a small sphere called a "marimo moss ball". 
            These beloved assemblages are greater than the sum of their parts.
            Since 1952 the marimo from Lake Akan in Hokkaidō have been designated as 
            special natural treasures of Japan because of their almost perfectly round shape, 
            large size and velvet-like surface.


            '''),
            mo.hstack([
                mo.center(mo.image(f'{image_path}Marimo_lake_akann.png', rounded=True,width=300)),
                mo.center(mo.image(f'{image_path}/Marimo.png', rounded=True,width=300)),
            ])
    ])
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md(
            """
            ## Agenda
            - Features and limitations of marimo
            - Reactivity
            - Marimo Flow
            - App examples

            Keep things interactive, questions or comments always welcome.
            """
        ),
    ])
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md("##Overview"),
        mo.hstack([
            mo.accordion(
                {
                    "jupyter": mo.md(
                        """
                        - great for exploration
                        - beware of:
                            - hidden state
                            - manual reruns
                            - hard-to-review file formats, Git Issues
                            - top down flow for run-all, arbitrary flow otherwise
                        """
                    )
                }
            ),
            mo.accordion(
                {
                    "marimo": mo.md(
                        """
                        - reactivity: change value in 1 cell updates the dependent cells
                        - think of Excel
                        - natural mechanism for callbacks
                        - great for dashboards
                        - easy to deploy on molab
                        """
                    )
                }
            ),
        ], widths="equal"),
    ])
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md(
            """
            ## Jupyter Summary/Demo
            """
        ),
        mo.hstack([
            mo.md(
                """
                - No reactivity
                - Notebook file is 10M when saved with outputs and visualizations
                - Reduced to 8M by changing float types from 64 to 32 bits
                - Reduces to 12K when outputs are cleared before saving
                - Marimo notebooks only save python, without the multiple megs of json figure representation, helpful for git
                - Jupyter support Julia, Python and R. Marimo only support python, focused support.

                #### Marimo only saves code, freeing up considerable amounts of disk space
                #### Jupyter notebook may exceed git file size limits
                #### By only saving python code, Marimo is inherently more git friendly
                """
            ),
            mo.image(src="assets/Jupyter.png"),
        ], widths="[3:1]"),
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
        mo.center(mo.md("## Inspiration Move me Brightly")),
        mo.vstack([
            _attribution_card(
                "Vincent Warmerdam (Founding Engineer)",
                "vincent.png",
                """
                 Vincent is a senior data professional with many meaningful contributions to the PyData stack, and has
                 pubished over 100 YouTube videos about marimo. I have watched most of them, best way to learn Marimo.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## UI elements

    Cells can output interactive UI elements. Interacting with a UI
    element **automatically triggers notebook execution**: when
    you interact with a UI element, its value is sent back to Python, and
    every cell that references that element is re-run.

    marimo provides a library of UI elements to choose from under
    marimo.ui.
    """)
    return


@app.cell
def _(mo):
    slider_max = 9  # 10 pets are allowed. slider max of 9 forces at least one of each type
    pet_slider = mo.ui.slider(1, slider_max, 1, label="Cats or Dogs?", value=3)

    return (pet_slider,)


@app.cell
def _(pet_slider):
    cat_num = pet_slider.value
    dog_num = 10 - cat_num
    return cat_num, dog_num


@app.cell
def _(cat_num, dog_num, mo, pet_slider):
    mo.vstack([
        mo.md("# You can have  10 pets. Use the slider to choose how many dogs and cats"),
        mo.md(
            f"""{pet_slider} {cat_num} Cats, {dog_num} Dogs """
        ),
        mo.md("#" + "🐱" * cat_num + f'  {cat_num} Cats'),
        mo.md("#" + "🐶 " *  dog_num + f' {dog_num} Dogs'),
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
    - usable as Python scripts, with UI elements taking their default
    values, and
    - importable by other modules (more on that in the future).
    """)
    return


@app.cell
def _(mo):
    mo.vstack([
        mo.md(
            """
            ## Dataframes

            polars, pandas comparison

            Pagination

            Interactive column select, row filters and other transforms

            Save csv, partquet or other formats

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
        mo.md("Single digit <b>Times Table</b><br><sup>mo.ui.table(dataframe)</sup>"),
        mo.ui.table(df_polars),
    ])
    return


@app.cell
def _(mo, pl):
    df_cal = (
        pl.read_excel("assets/california_counties_wikipedia.xlsx")
        .lazy()
        .with_columns(
            pl.concat_str(
                [
                    pl.lit("06"),
                    pl.col("FIPS").cast(pl.Int64).cast(pl.String).str.zfill(3),
                ]
            ).alias("FIPS"),
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
                "FIPS",
            ]
        )
        .collect()
    )

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
    demo_view = demo.value if demo.value else None
    print(f"display top 10 and bottom 10 charts by county {demo_view}")
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

    selected_county = get_selected_county()

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
        mo.md("California Counties - population statistics"),
        df_cal,
    ])
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


@app.cell
def _(county_info, demo, description, fig1_ui, fig2_ui, mo):
    layout = mo.vstack([
        mo.Html("<br>"),
        mo.left(mo.md(f" <h2>California County {demo.value}</h2>")),
        mo.hstack([
            description,
            county_info,
        ]),
        mo.left(demo),
        mo.hstack([fig1_ui, fig2_ui], widths="equal"),
    ])
    return (layout,)


@app.cell
def _(layout):
    layout
    return


@app.cell
def _(fig1_ui, fig2_ui, set_selected_county):
    selected_points = fig1_ui.points + fig2_ui.points
    if selected_points:
        set_selected_county(selected_points[0].get("y"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Quadratic Analyzer
    This notebook showcases datavisualization with Marimo.
    """)
    return


@app.cell
def _(go):
    def q_annotate_point(fig, name, color, size, x=None, y=None, textposition=None):
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

    return (q_annotate_point,)


@app.cell
def _(mo):
    q_a_number = mo.ui.number(value=1.0)
    q_b_number = mo.ui.number(value=-4.0)
    q_c_number = mo.ui.number(value=3.0)
    return q_a_number, q_b_number, q_c_number


@app.cell
def _(q_a_number, q_b_number, q_c_number):
    q_a = q_a_number.value
    q_a_legal = abs(q_a) > 0
    q_a_sign = 1 if q_a > 0 else -1
    q_b = q_b_number.value
    q_c = q_c_number.value
    return q_a, q_a_legal, q_a_sign, q_b, q_c


@app.cell
def _(mo, q_a_number, q_b_number, q_c_number):
    q_a_stack = mo.vstack([mo.md("a: (x<sup>2</sup> term)"), q_a_number])
    q_b_stack = mo.vstack([mo.md("b: (x) term:"), q_b_number])
    q_c_stack = mo.vstack([mo.md("c: (constant)"), q_c_number])
    return q_a_stack, q_b_stack, q_c_stack


@app.cell
def _(q_a, q_b, q_c):
    q_has_two_roots = False
    q_has_one_root = False
    q_has_no_roots = False
    if q_a != 0:
        q_discriminant = (q_b ** 2) - (4 * q_a * q_c)
        q_has_no_roots = q_discriminant < 0
        q_has_one_root = q_discriminant == 0
        q_has_two_roots = q_discriminant > 0
    else:
        q_has_one_root = q_b != 0
    return q_has_one_root, q_has_two_roots


@app.cell
def _(math, q_a, q_b, q_c, q_has_one_root, q_has_two_roots):
    q_root = None
    q_root1 = None
    q_root2 = None

    if q_a == 0:
        if q_b == 0:
            print("No root: this is not a quadratic equation and does not intersect y = 0")
        else:
            q_root = -q_c / q_b
            print(f"Linear equation, one root, intersects (0, {q_root:.3f})")
    elif q_has_one_root:
        q_root = -q_b / (2 * q_a)
    elif q_has_two_roots:
        q_root_discriminant = math.sqrt(q_b ** 2 - (4 * q_a * q_c))
        q_root1 = ((-q_b) + q_root_discriminant) / (2 * q_a)
        q_root2 = ((-q_b) - q_root_discriminant) / (2 * q_a)
        q_root1, q_root2 = sorted((q_root1, q_root2))

    if q_has_one_root and q_a != 0:
        print(f"One root, intersects (0, {q_root:.3f})")
    elif q_has_two_roots:
        print(f"Two roots, intersects (0, {q_root1:.3f}), (0, {q_root2:.3f})")
    return q_root, q_root1, q_root2


@app.cell
def _(mo):
    q_show_grid = mo.ui.checkbox(value=False, label="Show Grid")
    q_show_vertex = mo.ui.checkbox(value=False, label="Vertex")
    q_show_focus = mo.ui.checkbox(value=False, label="Focus")
    q_show_directrix = mo.ui.checkbox(value=False, label="Directrix")
    q_show_roots = mo.ui.checkbox(value=False, label="Roots")
    q_scale_xy = mo.ui.checkbox(value=False, label="Scale XY")
    return (
        q_scale_xy,
        q_show_directrix,
        q_show_focus,
        q_show_grid,
        q_show_roots,
        q_show_vertex,
    )


@app.cell
def _(q_a, q_a_legal, q_b, q_c):
    if q_a_legal:
        q_h = -q_b / (2 * q_a)
        q_k = q_c - (q_b ** 2) / (4 * q_a)
        q_x_focus = q_h
        q_y_focus = q_k + (1 / (4 * q_a))
    else:
        q_h = q_k = q_x_focus = q_y_focus = 0.0
        print("Invalid value of a: it cannot be 0 for a parabola")
    return q_h, q_k, q_x_focus, q_y_focus


@app.cell
def _(q_a, q_a_legal, q_b, q_c, q_h, q_x_focus):
    if q_a_legal:
        q_x_offset = 1 / (2 * q_a)
        q_x_left, q_x_right = sorted((q_h - q_x_offset, q_h + q_x_offset))
        q_width = q_x_right - q_x_left
        q_x_start = q_x_focus - (5 * q_width)
        q_x_stop = q_x_focus + (5 * q_width)
        q_x_vals = [q_x_start + i * (q_x_stop - q_x_start) / 1000 for i in range(1001)]
        q_y_vals = [q_a * x * x + q_b * x + q_c for x in q_x_vals]
    else:
        q_x_left = q_x_right = q_width = 1.0
        q_x_vals = [-5 + i / 100 for i in range(1001)]
        q_y_vals = [q_b * x + q_c for x in q_x_vals]
    return q_width, q_x_vals, q_y_vals


@app.cell
def _(q_a, q_a_legal, q_k):
    q_y_directrix = q_k - (1 / (4 * q_a)) if q_a_legal else None
    return (q_y_directrix,)


@app.cell
def _(
    go,
    mo,
    q_a,
    q_a_legal,
    q_a_number,
    q_a_sign,
    q_a_stack,
    q_annotate_point,
    q_b,
    q_b_number,
    q_b_stack,
    q_c,
    q_c_number,
    q_c_stack,
    q_h,
    q_has_one_root,
    q_has_two_roots,
    q_k,
    q_root,
    q_root1,
    q_root2,
    q_scale_xy,
    q_show_directrix,
    q_show_focus,
    q_show_grid,
    q_show_roots,
    q_show_vertex,
    q_width,
    q_x_focus,
    q_x_vals,
    q_y_directrix,
    q_y_focus,
    q_y_vals,
):
    q_fig = go.Figure(data=go.Scatter(x=q_x_vals, y=q_y_vals, showlegend=False))

    if q_has_one_root and q_a != 0:
        q_subtitle = f"One Root at x = {q_root:.6f}".rstrip("0").rstrip(".")
    elif q_has_two_roots:
        q_subtitle = f"Two Roots at x = {q_root1:.6f}, {q_root2:.6f}"
    else:
        q_subtitle = "No Real Roots" if q_a != 0 else "Linear Equation"

    if q_a_number.value == -1:
        q_a_expression = "y = -x<sup>2</sup>"
    elif q_a_number.value == 1:
        q_a_expression = "y = x<sup>2</sup>"
    elif q_a_number.value == 0:
        q_a_expression = "y = "
    else:
        q_a_expression = f"y = {q_a}x<sup>2</sup>"

    if q_b_number.value == -1:
        q_b_expression = " - x"
    elif q_b_number.value == 1:
        q_b_expression = " + x"
    elif q_b_number.value == 0:
        q_b_expression = ""
    elif q_b_number.value > 0:
        q_b_expression = f" + {q_b}x"
    else:
        q_b_expression = f" - {abs(q_b)}x"

    if q_c_number.value == 0:
        q_c_expression = ""
    elif q_c_number.value > 0:
        q_c_expression = f" + {q_c}"
    else:
        q_c_expression = f" - {abs(q_c)}"

    q_title = f"{q_a_expression}{q_b_expression}{q_c_expression}"
    q_fig.update_layout(
        title=dict(
            text=q_title,
            x=0.5,
            xanchor="center",
            font=dict(family="Arial, sans-serif", size=26, color="white"),
            subtitle=dict(
                text=q_subtitle,
                font=dict(family="Arial, sans-serif", size=15, color="dimgray"),
            ),
        )
    )
    q_marker_size = 6

    if q_show_vertex.value and q_a_legal:
        textposition = "bottom center" if q_a_sign > 0 else "top center"
        q_fig = q_annotate_point(
            q_fig,
            "Vertex",
            "crimson",
            q_marker_size,
            x=q_h,
            y=q_k,
            textposition=textposition,
        )

    if q_show_focus.value and q_a_legal:
        textposition = "bottom center" if q_a_sign < 0 else "top center"
        q_fig = q_annotate_point(
            q_fig,
            "Focus",
            "crimson",
            q_marker_size,
            x=q_h,
            y=q_y_focus,
            textposition=textposition,
        )

    if q_show_directrix.value and q_y_directrix is not None:
        q_fig.add_hline(y=q_y_directrix, line_dash="dot")

    if q_show_roots.value:
        if q_has_one_root and q_a != 0:
            textposition = "bottom center" if q_a_sign < 0 else "top center"
            q_fig = q_annotate_point(
                q_fig,
                "Root",
                "crimson",
                q_marker_size,
                x=q_root,
                textposition=textposition,
            )
        elif q_has_two_roots:
            q_fig = q_annotate_point(
                q_fig,
                "Root 1",
                "crimson",
                q_marker_size,
                x=q_root1,
                textposition="middle left",
            )
            q_fig = q_annotate_point(
                q_fig,
                "Root 2",
                "crimson",
                q_marker_size,
                x=q_root2,
                textposition="middle right",
            )

    if q_show_grid.value:
        q_fig.update_xaxes(showgrid=True, visible=True)
        q_fig.update_yaxes(showgrid=True, visible=True)
    else:
        q_fig.update_xaxes(showgrid=False, visible=False)
        q_fig.update_yaxes(showgrid=False, visible=False)

    if q_a_legal:
        q_y_range_max = q_y_directrix + q_a_sign * (3 * abs(q_y_focus - q_y_directrix))
        q_y_range_min = q_y_directrix - (q_a_sign * 0.1 * abs(q_k - q_y_directrix))
        q_x_range_max = q_x_focus + (2 * q_width)
        q_x_range_min = q_x_focus - (2 * q_width)
        q_x_range = [q_x_range_min, q_x_range_max]
        q_y_range = sorted([q_y_range_min, q_y_range_max])
        if q_scale_xy.value:
            q_fig.update_layout(xaxis=dict(scaleanchor="y"), yaxis=dict(scaleanchor="x"))
        else:
            q_fig.update_yaxes(range=q_y_range)
        q_fig.update_xaxes(range=q_x_range)

    q_fig.update_layout(template="plotly_dark")

    mo.vstack([
        mo.md("## Quadratic Analyzer"),
        mo.hstack([q_a_stack, q_b_stack, q_c_stack]),
        mo.hstack(
            [
                mo.ui.plotly(q_fig),
                mo.vstack([
                    q_show_grid,
                    q_show_vertex,
                    q_show_focus,
                    q_show_directrix,
                    q_show_roots,
                    q_scale_xy,
                ]),
            ],
            widths=[3, 1],
        ),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 5. The  marimo command-line tool

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


@app.cell
def _(mo):
    mo.accordion(
        {
            "Tip: execution order": (
                """
                The order of cells on the page has no bearing on
                the order in which cells are executed: marimo knows that a cell
                reading a variable must run after the cell that defines it. This
                frees you to organize your code in the way that makes the most
                sense for you.
                """
            )
        }
    )
    return


@app.cell
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


@app.cell
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
    **Global names must be unique.** To enable reactivity, marimo imposes a
    constraint on how names appear in cells: no two cells may define the same
    variable.
    """)
    return


@app.cell
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

            2. _Run a stale cell_ by clicking the yellow run button on the
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
    return


if __name__ == "__main__":
    app.run()
