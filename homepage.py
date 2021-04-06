import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from plots import *
from wrangle import *
from dash.dependencies import Input, Output, State
from navbar import *

header = header()
nav = Navbar(page = 'tracker')

def get_graph(class_name, **kwargs):
    return html.Div(
        className=class_name + ' plotz-container',
        children=[
            dcc.Graph(**kwargs),
            html.I(className='fa fa-expand'),
        ],
    )

def dropdown_options(col):
    return [{'label': name, 'value': name} for name in col]

about_app = html.Div(
    children=[
        html.Ul([
            html.Li(
                html.A('Our World in Data - COVID-19 Data Explorer', href="https://ourworldindata.org/explorers/coronavirus-data-explorer?zoomToSelection=true&time=2020-03-01..latest&country=USA~GBR~CAN~DEU~ITA~IND&region=World&pickerMetric=location&pickerSort=asc&Metric=Confirmed+cases&Interval=7-day+rolling+average&Align+outbreaks=false&Relative+to+Population=true", style={'font_family':'Arial'})
            ),
            html.Li(
                html.A('John Hopkins - Coronavirus Resource Center', href="https://coronavirus.jhu.edu/", style={'font_family':'Arial'})
            )
        ]),
        html.P('''
        All plots in this dashboard are interactive. Just hit play on the map, hover over bubbles, lines & points 
        for a more detailed look at the data.''',style = {'font_family':'Arial'}),
        html.P('''
        To filter the bottom middle timeline to a country, hover over a horizontal bar displayed
        in the rightmost bottom plot.
        ''',style = {'font_family':'Arial'}),
        html.P('''
        To switch between Confirmed, Active, Recovered, Deaths, Hospitalizations Vaccinations and Per Capita/Actual,
         use the radio buttons in the control panel, top right.''',style = {'font_family':'Arial'}),
        html.P('''
        The data used in this dashboard comes from John Hopkins University and Our World in Data.
        ''',style = {'font_family':'Arial'}),
        html.P('''
        Per Capita numbers are number / Population * 100,000 
        ''', style = {'font_family':'Arial'}),
    ],
)

def Homepage():
    layout = html.Div([
        header,
        nav,
        modal,
        body
    ])
    return layout
