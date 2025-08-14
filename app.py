import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from navbar import create_navbar

NAVBAR = create_navbar()

FA621 = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"
APP_TITLE = "First Dash App"

external_stylesheets_supply = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.LUX, 
        FA621,  
    ],
    title=APP_TITLE,
    use_pages=True
)

app.layout = dcc.Loading(
    id='loading_page_content',
    children=[
        html.Div(
            [
                NAVBAR,
                dash.page_container
            ]
        )
    ],
    color='primary',
    fullscreen=True 
)

server = app.server

if __name__ == '__main__':
    app.run(debug=False)
