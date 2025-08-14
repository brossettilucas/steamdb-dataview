from dash import html, callback, register_page, dcc
from dash.dependencies import Input, Output
import dash_daq as daq

from src.data_features import build_scatter_matrix
from src.setup import choose_threshold

datath1 = choose_threshold(1)
datath6 = choose_threshold(5)
dataCopy = choose_threshold(0)

register_page(
    __name__, name="Correlação dos Atributos", top_nav=True, path="/covariance_dist"
)

header = html.H1("Correlação dos Atributos", style={"textAlign": "center"})


def layout():
    layout = html.Div(
        [
            html.Div(
                [
                    header,
                    html.Br(),
                    html.Br(),
                    html.Div(
                        [
                            daq.BooleanSwitch(
                                id="outlier-switch", on=False, label="Remove Outliers"
                            )
                        ]
                    ),
                    html.Br(),
                    html.Div(id="outlier-button-result"),
                    html.Br(),
                ],
                style={"margin": "5% 10% 5% 10%"},
            )
        ]
    )
    return layout


@callback(Output("outlier-button-result", "children"), Input("outlier-switch", "on"))
def update_output(on):
    if on:
        return dcc.Graph(figure=build_scatter_matrix(datath1, outliers=False))
    else:
        return dcc.Graph(figure=build_scatter_matrix(datath1, outliers=True))
