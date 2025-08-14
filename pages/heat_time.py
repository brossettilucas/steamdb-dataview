from dash import html, register_page, dcc

from src.data_features import build_heat_plot
from src.setup import choose_threshold

datath1 = choose_threshold(1)
datath6 = choose_threshold(5)
dataCopy = choose_threshold(0)

register_page(
    __name__, name="Mapa de calor dos lançamentos", top_nav=True, path="/heat_time"
)

about_data = dcc.Markdown("""Dataset construído a partir dos dados disponibilizados pelo Steam Trends 2023 
                          e da coleta do steamspy. 
                          """)

header = html.H1("Heatmap - lançamentos", style={"textAlign": "center"})
line_break = html.Div([dcc.Markdown("""___""")], style={"margin": "5% 0% 5% 0%"})


def layout():
    layout = html.Div(
        [
            html.Div(
                [
                    header,
                    html.Br(),
                    html.Br(),
                    dcc.Graph(figure=build_heat_plot(dataCopy)),
                ],
                style={"margin": "5% 10% 5% 10%"},
            )
        ]
    )
    return layout
