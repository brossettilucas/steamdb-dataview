from dash import html, callback, dcc, register_page
from src.gender_analytics import get_line_year
from src.setup import choose_threshold
from dash.dependencies import Input, Output
import dash_daq as daq

register_page(
    __name__, name="Crescimento dos Gêneros", top_nav=True, path="/gender_dist_time"
)

header = html.H1("Crescimento dos gêneros", style={"textAlign": "center"})


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
                                id="log-switch", on=False, label="Log eixo y"
                            )
                        ]
                    ),
                    html.Br(),
                    html.Div(id="log-switch-result"),
                ],
                style={"margin": "5% 10% 5% 10%"},
            )
        ]
    )
    return layout


@callback(Output("log-switch-result", "children"), Input("log-switch", "on"))
def update_output(on):
    if on:
        return dcc.Graph(figure=get_line_year(choose_threshold(1), isLog=True))
    else:
        return dcc.Graph(figure=get_line_year(choose_threshold(1), isLog=False))
