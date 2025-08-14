from dash import html, dcc, register_page
from src.gender_analytics import get_scatter_genre_blobs
from src.setup import choose_threshold

SCATTER_blobs_genres = get_scatter_genre_blobs(choose_threshold(1))

register_page(__name__, name="Bubble Chart Gêneros", top_nav=True, path="/gender_dist")

header = html.H1("Bubble chart - gêneros", style={"textAlign": "center"})
line_break = html.Div([dcc.Markdown("""___""")], style={"margin": "5% 0% 5% 0%"})


def layout():
    layout = html.Div(
        [
            html.Div(
                [
                    header,
                    html.Br(),
                    html.Br(),
                    dcc.Graph(figure=SCATTER_blobs_genres),
                ],
                style={"margin": "5% 10% 5% 10%"},
            )
        ]
    )
    return layout
