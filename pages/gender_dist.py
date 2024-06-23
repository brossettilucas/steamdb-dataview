from dash import Dash, html, Input, Output, callback, dcc , register_page
from src.gender_dev_analytics import get_scatter_genre_blobs
from src.setup import get_json_field, choose_threshold

SCATTER_blobs_genres = get_scatter_genre_blobs(choose_threshold(1))

register_page(
    __name__,
    name='Estudo dos Gêneros',
    top_nav=True,
    path='/gender_dist'
)

def layout():
    layout = html.Div([
        html.H1(
            [
                "Análise dos Gêneros dos Jogos"
            ]
        ),
        html.Div(
            children=[
                #ANÁLISE POR GÊNEROS E DEVS
                html.H2(children="Generos com maior numero de jogos"),
                
                # dcc.Graph(
                #     figure=HISTOGRAM_dist_avg_price_genre,
                # ),
                # dcc.Graph(
                #     figure=BAR_dist_normal_avg_price_genre,
                #         ),
                # dcc.Graph(
                #     figure=BAR_dist_normal_score_genre,
                #         ),
                # dcc.Graph(
                #     figure=BAR_normal_score_genre_div,
                #         ),
                # dcc.Graph(
                #     figure=HISTOGRAM_dist_avg_price_genre_2,
                #         ),
                dcc.Graph(
                    figure=SCATTER_blobs_genres,
                        ),
                # dcc.Graph(
                #     figure=LINE_games_year,
                #         ),
                # dcc.Graph(
                #     figure=LINE_indie_year,
                # )    
            ],
            className="view"
        )  
    ])
    return layout