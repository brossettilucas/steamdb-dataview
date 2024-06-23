
from dash import html
import dash_bootstrap_components as dbc


def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            # dbc.NavItem(
            #     dbc.NavLink(
            #         [
            #             html.I(className="fa-brands fa-github"),  # Font Awesome Icon
            #             " "  # Text beside icon
            #         ],
            #         href="",
            #         target="_blank"
            #     )

            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                align_end=True,
                children=[  # Add as many menu items as you need
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Caracterização dos atributos", href='/char_dist'),
                    dbc.DropdownMenuItem("Covariância dos Atributos", href='/covariance_dist'),
                    dbc.DropdownMenuItem("Mapa de calor das datas de lançamento", href='/heat_time'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Estudo dos Gêneros - top 15", href='/gender_dist'),
                    dbc.DropdownMenuItem("Timeline dos Gêneros", href='/gender_dist_time'),
                    dbc.DropdownMenuItem("Mapa de Desenvolvedores", href='/'),
                    # dbc.DropdownMenuItem("Estudo dos Gêneros", href='/gender_dist'),
                    # dbc.DropdownMenuItem("Estudo dos Gêneros", href='/gender_dist'),
                    # dbc.DropdownMenuItem("Estudo dos Gêneros", href='/gender_dist')
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
