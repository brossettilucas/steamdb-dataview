# from dash import Dash, html, Input, Output, callback, dcc , dash_table
# from src.gender_dev_analytics import get_avg_dists
# import dash
# import dash_daq as daq
# import os


# genres = ['a' , 'b' ,'c' , 'd' , 'banana']
# years = [i for i in range(1990,2024)]

# (
#     HISTOGRAM_dist_avg_price_genre, 
#     BAR_dist_normal_avg_price_genre , 
#     BAR_dist_normal_score_genre,
#     BAR_normal_score_genre_div,
#     HISTOGRAM_dist_avg_price_genre_2,
#     # gráfico de top 15 generos em matplotlib deve ser refeito em plotly,
#     SCATTER_blobs_genres,
#     LINE_games_year,            
#     LINE_indie_year            
# ) = get_avg_dists(dev_spy=False)


# dash.register_page(__name__)

# layout = html.Div(
#     children=[
#         html.Div(
#             children=[
#                 html.A(
#                     html.Div([
#                         html.Div(
#                             dcc.Link(f"Home", href=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app.py')))
#                         )
#                     ]),
#                     dash.page_container
#                 ),
#                 html.A(
#                     html.Div([
#                         html.Div(
#                             dcc.Link(f"Caracterização dos Dados", href=os.chdir("char_dists.py"))
#                         )
#                     ]),
#                     dash.page_container
#                 ),
#                 html.A(
#                     html.Div([
#                         html.Div(
#                             dcc.Link(f"Distribuições por Gêneros", href=os.chdir("gender_dists.py"))
#                         )
#                     ]),
#                     dash.page_container,
#                     className="active"
#                 ),
#             ],
#             className="topnav"
            
#         ),
#         html.Div(
#             children=[
#                 html.H3(children="Análise Exploratória do Steam Trends 2023",className="header-title"),
#                 html.P(
#                     children=(
#                         "teste"
#                     ),
#                     className="header-description"
#                 ),
#             ],
#             className="header",
#         ),
#         html.Div(
#             children=[
#                 html.Div(
#                     children=[
#                         html.Div(children="Genre", className="menu-title"),
#                         dcc.Dropdown(
#                             id="region-filter",
#                             options=[
#                                 {"label": genre, "value": genre}
#                                 for genre in genres
#                             ],
#                             value="a",
#                             clearable=False,
#                             className="dropdown",
#                         ),
#                     ]
#                 ),
#                 html.Div(
#                     children=[
#                         html.Div(children="Year", className="menu-title"),
#                         dcc.Dropdown(
#                             id="type-filter",
#                             options=[
#                                 {
#                                     "label": year,
#                                     "value": year,
#                                 }
#                                 for year in years
#                             ],
#                             value="2023",
#                             clearable=False,
#                             searchable=False,
#                             className="dropdown",
#                         ),
#                     ],
#                 ),
#                 html.Div(
#                     children=[
#                         html.Div(
#                             children="Date Range", className="menu-title"
#                         ),
#                         dcc.DatePickerRange(
#                             id="date-range",
#                             min_date_allowed='1990-12-01',
#                             max_date_allowed='2023-12-01',
#                             start_date='1990-12-01',
#                             end_date='2023-12-01',
#                         ),
#                     ]
#                 ),
#                 html.Div(
#                     children=[
#                         html.Div(
#                             children="Ignore outliers",className="menu-title"
#                         ),
#                         daq.BooleanSwitch(id='our-boolean-switch', on=False),
#                         html.Div(id='boolean-switch-result')
#                 ])
#             ],
#             className="menu",
#         ),
        
#         html.Div(
#             children=[
#                 #ANÁLISE POR GÊNEROS E DEVS
#                 html.H2(children="Gêneros e Popularidade2"),
#                 html.P(
#                     children=(
#                         "Aqui avaliamos como os genêros catalogados dos jogos na plataforma influenciam o seu sucesso comercial."
#                         "Terminamos por verificar a tendência de lançamentos anuais."
#                     )
#                 ),
#                 dcc.Graph(
#                     figure=HISTOGRAM_dist_avg_price_genre,
#                 ),
#                 dcc.Graph(
#                     figure=BAR_dist_normal_avg_price_genre,
#                         ),
#                 dcc.Graph(
#                     figure=BAR_dist_normal_score_genre,
#                         ),
#                 dcc.Graph(
#                     figure=BAR_normal_score_genre_div,
#                         ),
#                 dcc.Graph(
#                     figure=HISTOGRAM_dist_avg_price_genre_2,
#                         ),
#                 dcc.Graph(
#                     figure=SCATTER_blobs_genres,
#                         ),
#                 dcc.Graph(
#                     figure=LINE_games_year,
#                         ),
#                 dcc.Graph(
#                     figure=LINE_indie_year,
#                 )    
#             ],
#             className="view"
#         )   
#     ]
# )

# @callback(
#     Output('boolean-switch-result', 'children'),
#     Input('our-boolean-switch', 'on')
# )
# def update_output(on):
#     return f'The switch is {on}.'
