
from dash import html
import dash_bootstrap_components as dbc


def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                align_end=True,
                children=[  # Add as many menu items as you need
                    dbc.DropdownMenuItem("Home", href='/'),
                    
                    dbc.DropdownMenuItem(divider=True),
                    #Caracterização dos Atributos
                    dbc.DropdownMenuItem("Caracterização dos Atributos", href='/char_dist'),
                    dbc.DropdownMenuItem("Correlação dos Atributos", href='/covariance_dist'),
                    dbc.DropdownMenuItem("Mapa de calor dos lançamentos", href='/heat_time'),
                    
                    dbc.DropdownMenuItem(divider=True),
                    #Estudos dos Gêneros e Desenvolvedoras
                    dbc.DropdownMenuItem("Bubble Chart Gêneros", href='/gender_dist'),
                    dbc.DropdownMenuItem("Crescimento dos Gêneros", href='/gender_dist_time'),
                    dbc.DropdownMenuItem("Desenvolvedoras e Gêneros", href='/dev_maps'),
                    # dbc.DropdownMenuItem("Estudo dos Gêneros", href='/gender_dist'),
                ],
            ),
        ],
        brand='Steam Trends 2023',
        brand_href="/",
        # sticky="top",  # Uncomment if you want the navbar to always appear at the top on scroll.
        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

    return navbar
