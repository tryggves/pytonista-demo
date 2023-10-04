# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H6("Change the value in the text box to see callbacks in action!"),
        html.Div(
            ["Input: ", dcc.Input(id="my-input", value="initial value", type="text")]
        ),
        html.Br(),
        html.Div(id="my-output"),
    ]
)


# Why do we use 'app.callback' and non 'callback'?
@app.callback(
    Output(component_id="my-output", component_property="children"),
    Input(component_id="my-input", component_property="value"),
)
def update_output_div(input_value):
    return f"Output: {input_value}"


if __name__ == "__main__":
    app.run_server(debug=True)
