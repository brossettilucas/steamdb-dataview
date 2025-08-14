from dash import html, register_page, dcc
import plotly.graph_objects as go

from src.setup import choose_threshold

register_page(__name__, name="Home", top_nav=True, path="/")


def create_table(df):
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(values=df.columns, align="left"),
                cells=dict(values=df.values.T, align="left"),
            )
        ]
    )
    fig.update_layout(
        paper_bgcolor="#e5ecf6", margin={"t": 10, "l": 20, "r": 20, "b": 5}
    )
    return fig


about_data = dcc.Markdown("""Dataset construído a partir dos dados disponibilizados pelo Steam Trends 2023 
                          e da coleta do steamspy. 
                          """)

header = html.H1("Dataset", style={"textAlign": "center"})
line_break = html.Div([dcc.Markdown("""___""")], style={"margin": "5% 0% 5% 0%"})


def layout():
    layout = html.Div(
        [
            header,
            html.Br(),
            html.Br(),
            about_data,
            html.Br(),
            dcc.Graph(id="dataset", figure=create_table(choose_threshold(1))),
        ],
        style={"margin": "5% 10% 5% 10%"},
    )
    return layout
