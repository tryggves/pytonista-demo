# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {"background": "#111111", "text": "#7FDBFF"}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

# Instantiate a bar plot object in fig
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors["background"],
    paper_bgcolor=colors["background"],
    font_color=colors["text"],
)

# Set app.layout by creating a html object
app.layout = html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
        html.H1(
            children="Hello Dash",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        html.Div(
            children="""
            Dash: A web application framework for your data.
            Could probably write some more text here.
            <p>Is this a new paragraph?? Nope. It is taking all characters as literals and no parsing.</p>
            """,
            style={"textAlign": "center", "color": colors["text"]},
        ),
        html.P(
            "Here is another paragraph",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        html.P(
            """Here is yet another paragraph
        written over multiple lines to avoid having very long text lines clobbering
        the code.""",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        dcc.Graph(id="example-graph", figure=fig),
    ],
)

if __name__ == "__main__":
    # This probably kicks off the event loop
    app.run_server(debug=True)
