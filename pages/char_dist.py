from dash import html, Input, Output, callback, register_page, dcc 
import dash_daq as daq

from src.data_features import build_histogram 
from src.setup import choose_threshold

datath1 = choose_threshold(1)
datath6 = choose_threshold(5)
dataCopy = choose_threshold(0)

register_page(
    __name__,
    name='Caracterização dos Atributos',
    top_nav=True,
    path='/char_dist'
)

header = html.H1('Distribuição - Atributos', style={'textAlign': 'center'})

def layout():
    layout = html.Div([
        html.Div(
            [
                header,
                html.Br(),
                html.Br(),
                # html.Div([daq.BooleanSwitch(id='outlier-switch', on=True,label='Remove Outliers')]),
                # html.Br(),
                # html.Div(id="outlier-button-result"),
                 dcc.Graph(figure=build_histogram(datath1,datath6)),
                html.Br(),   
            ],
            style={'margin': '5% 10% 5% 10%'}
        )  
    ])
    return layout


# @callback(
#     Output('boolean-switch-result', 'children'),
#     Input('our-boolean-switch', 'on')
# )
# def update_output(on):
#     return f'The switch is {on}.'
