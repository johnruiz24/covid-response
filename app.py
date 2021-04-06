import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from plots import *
from wrangle import *
from dash.dependencies import Input, Output, State
from navbar import Navbar
from policyresponse import *

template = 'plotly_light'
default_layout = {
    'autosize': True,
    'xaxis': {'title': None},
    'yaxis': {'title': None},
    'margin': {'l': 40, 'r': 20, 't': 40, 'b': 10},
    'paper_bgcolor': '#B1B1B1', 
    'plot_bgcolor': '#B1B1B1', 
    'hovermode': 'x',
}

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.1/css/all.min.css',
]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED],)
server = app.server
app.config.suppress_callback_exceptions = True
app.index_string = open('index.html', 'r').read()

app.layout = html.Div([
    PolResponse()
])

## Policy response tab
@app.callback(
    Output('modal_policy', 'is_open'),
    [Input('policy_button', 'n_clicks'), Input('close_policy', 'n_clicks')],
    [State('modal_policy', 'is_open')],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output('sunburst', 'figure'),
    [
        Input('policy', 'value'),
    ])
def update_sunburst(policy):
    return get_sunburst(policy_response_df, policy=policy)

@app.callback(
    Output('trends_plot', 'figure'),
    [
        Input('country_trends', 'value')
    ])
def update_mobility_trends(country_trends):
    return get_line_plot(trends_final, country_name = country_trends)

if __name__ == '__main__':
    app.run_server(host='127.0.0.1',port=8050,debug=True)
