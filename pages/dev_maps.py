from dash import html, dcc, register_page
from src.dev_analytics import make_treemap_top_devs, make_treemap_top_games
from src.setup import choose_threshold

treemap_devs = make_treemap_top_devs(choose_threshold(1), 15)

register_page(
    __name__, name="Desenvolvedoras e Gêneros", top_nav=True, path="/dev_maps"
)

header = html.H1("Desenvolvedoras e Gêneros", style={"textAlign": "center"})


def layout():
    layout = html.Div(
        [
            html.Div(
                [
                    header,
                    html.Br(),
                    html.Br(),
                    dcc.Graph(figure=make_treemap_top_devs(choose_threshold(1))),
                    html.Br(),
                    html.Br(),
                    dcc.Graph(figure=make_treemap_top_games(choose_threshold(1))),
                    html.Br(),
                ],
                style={"margin": "5% 10% 5% 10%"},
            )
        ]
    )
    return layout
