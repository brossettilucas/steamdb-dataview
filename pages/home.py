from dash import html, register_page, dcc, html, Input, Output, callback  
import dash_daq as daq
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from src.setup import build_dictionaries, choose_threshold

register_page(
    __name__,
    name='Home',
    top_nav=True,
    path='/'
)



genres = ['a' , 'b' ,'c' , 'd' , 'banana']
years = [i for i in range(1990,2024)]


def layout():
    layout = html.Div([
        html.H1(
            [
                "Home Page"
            ]
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Genre", className="menu-title"),
                        dcc.Dropdown(
                            id="region-filter",
                            options=[
                                {"label": genre, "value": genre}
                                for genre in genres
                            ],
                            value="a",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Year", className="menu-title"),
                        dcc.Dropdown(
                            id="type-filter",
                            options=[
                                {
                                    "label": year,
                                    "value": year,
                                }
                                for year in years
                            ],
                            value="2023",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range", className="menu-title"
                        ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed='1990-12-01',
                            max_date_allowed='2023-12-01',
                            start_date='1990-12-01',
                            end_date='2023-12-01',
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Ignore outliers",className="menu-title"
                        ),
                        daq.BooleanSwitch(id='our-boolean-switch', on=False),
                        html.Div(id='boolean-switch-result')
                ])
            ],
            className="menu",
        ),
        
        

        #ANÁLISE POR GÊNEROS E DEVS
        html.H2(children="Gêneros e Popularidade"),
        html.P(
            children=(
                "Aqui avaliamos como os genêros catalogados dos jogos na plataforma influenciam o seu sucesso comercial."
                "Terminamos por verificar a tendência de lançamentos anuais."
            )
        ),
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
        #         ),s
        # dcc.Graph(
        #     figure=SCATTER_blobs_genres,
        #         ),
        # dcc.Graph(
        #     figure=LINE_games_year,
        #         ),
        # dcc.Graph(
        #     figure=LINE_indie_year,
        #         ),

    ])
    return layout



