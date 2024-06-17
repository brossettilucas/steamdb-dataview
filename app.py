from data_features import build_histogram , build_scatter_matrix , build_heat_plot
from gender_dev_analytics import get_avg_dists
from dash import Dash, dcc, html

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

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app = Dash(__name__ , external_stylesheets=external_stylesheets)
app.title = "Steam Trends 2023: Uma Análise Exploratória"
app.layout = html.Div(
    children=[
        html.H1(children="Análise da Base de Dados da Steam - Outubro/2023"),
        html.P(
            children=(
                "Aqui iremos analisar sob diversos aspectos a base de dados da plataforma de jogos Steam. "
                "Procuramos responder perguntas relacionadas a diferentes características de cada jogo publicado na plataforma, "
                "como popularidade , preço de lançamento , lucro total e até período de lançamento. "
            ),
        ),
        
        # CARACTERIZAÇÃO DO DATASET
        html.H2(children="Descrição dos Atributos"),
        html.P(
            children=(
                "As distribuições apresentadas fornecem uma visão dos atributos quantificáveis do conjunto de dados."
            )
        ),
        dcc.Graph(
            figure=build_histogram(),
        ),
        dcc.Graph(
            figure=build_scatter_matrix(),
        ),
        dcc.Graph(
            figure=build_heat_plot()
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
        #         ),
        # dcc.Graph(
        #     figure=SCATTER_blobs_genres,
        #         ),
        # dcc.Graph(
        #     figure=LINE_games_year,
        #         ),
        # dcc.Graph(
        #     figure=LINE_indie_year,
        #         ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)