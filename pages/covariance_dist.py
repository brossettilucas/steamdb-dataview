from dash import html, Input, Output, callback, register_page, dcc 
import dash_daq as daq

from src.data_features import build_scatter_matrix 
from src.setup import choose_threshold

datath1 = choose_threshold(1)
datath6 = choose_threshold(5)
dataCopy = choose_threshold(0)

register_page(
    __name__,
    name='Covariância dos Atributos',
    top_nav=True,
    path='/covariance_dist'
)


def layout():
    layout = html.Div([
        html.H1(
            [
                "Caracterização dos Dados"
            ]
        ),
        html.Div(
            children=[
                # CARACTERIZAÇÃO DO DATASET
                html.H2(children="Covariância dos atributos"),
                dcc.Graph(
                    figure=build_scatter_matrix(datath1),
                )
            ],
            className="view"
        )  
    ])
    return layout


# @callback(
#     Output('boolean-switch-result', 'children'),
#     Input('our-boolean-switch', 'on')
# )
def update_output(on):
    return f'The switch is {on}.'
