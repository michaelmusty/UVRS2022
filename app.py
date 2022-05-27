# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import glob
import os

import dash
import pandas as pd
import plotly.express as px
import plotly.io as pio
from dash import dcc, html
from dash.dependencies import Input, Output
from loguru import logger

# pio.templates.default = "plotly_dark"

# read table with all race scores

path = os.path.abspath("output_data/tables/")
list_of_filenames = glob.glob(f"{path}/*")
filename_used = max(list_of_filenames, key=os.path.getctime)
logger.info(filename_used)
df = pd.read_csv(filename_used)
df.sort_values(by=["Race"], inplace=True)

# TODO: overall scores? participation?

# all the app stuff

available_indicators = sorted(df["Age Group"].unique())

app = dash.Dash(__name__)
app.title = "2022 UVRS Scorecard"
server = app.server

app.layout = html.Div(
    [
        html.H1("2022 Upper Valley Running Series Scorecard"),
        html.Div("Select Age Group"),
        html.Div(
            dcc.Dropdown(
                id="age-group",
                options=[{"label": i, "value": i} for i in available_indicators],
                value="Age Group",
            ),
            style={"width": "20%"},
        ),
        dcc.Graph(id="main_graph"),
    ]
)


@app.callback(Output("main_graph", "figure"), Input("age-group", "value"))
def update_graph(age_group):
    dff = df[df["Age Group"] == age_group]
    fig = px.bar(
        dff,
        y="Individual",
        x="Score",
        hover_data=["Net Time"],
        color="Race",
        orientation="h",
        barmode="stack",
    )
    fig.update_layout(barmode="stack", yaxis={"categoryorder": "total ascending"})
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
