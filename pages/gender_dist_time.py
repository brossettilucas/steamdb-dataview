from dash import Dash, html, Input, Output, callback, dcc , register_page
from src.gender_dev_analytics import get_line_year
from src.setup import get_json_field, choose_threshold

LINE_games_year = get_line_year(choose_threshold(1))

register_page(
    __name__,
    name='Timeline',
    top_nav=True,
    path='/gender_dist_time'
)

def layout():
    layout = html.Div([
        html.H1(
            [
                "Linha do tempo de lançamentos"
            ]
        ),
        html.Div(
            children=[
                #ANÁLISE POR GÊNEROS E DEVS
                html.H2(children="Timeline generos"),
                dcc.Graph(
                    figure=LINE_games_year,
                        )   
            ],
            className="view"
        )  
    ])
    return layout