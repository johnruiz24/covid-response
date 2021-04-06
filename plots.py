import os
import pandas as pd
import numpy as np
import plotly
import plotly.io as pio
import plotly.graph_objects as go
from plotly import express as px
from wrangle import *
plot_config = {
    'modeBarButtonsToRemove': [
        'lasso2d',
        'hoverClosestCartesian',
        'hoverCompareCartesian',
        'toImage',
        'sendDataToCloud',
        'hoverClosestGl2d',
        'hoverClosestPie',
        'toggleHover',
        'resetViews',
        'toggleSpikelines',
        'resetViewMapbox'
    ]
}

plot_palette = [
    '#185d6a',
    '#385e4c',
    '#597043',
    '#7a8339',
    '#9b9530',
    '#bca727',
    '#ddb91e',
    '#ffcc14',
]
# Plotly mapbox public token
mapbox_token = "pk.eyJ1IjoicjIwMTY3MjciLCJhIjoiY2s1Y2N4N2hoMDBrNzNtczBjN3M4d3N4diJ9.OrgK7MnbQyOJIu6d60j_iQ"
mapbox_cofig = dict(accesstoken=mapbox_token, style='light')

bggolor = '#24252A'
# bggolor ='#FFFFFF'
default_layout = {
    'font_family': 'Arial Black',
    'font_color':'#24252A',
    'margin': {'r': 5, 't': 20, 'l': 5, 'b': 30},
    'paper_bgcolor': 'rgb(221, 237, 234)',#'rgb(62, 64, 76)',
    'plot_bgcolor':'rgb(221, 237, 234)',
    'xaxis':{'autorange':True},
    'yaxis':{'autorange':True}
}

plot_threshold = 35
empty_plot = px.line(template='plotly_dark')


def get_sunburst(df, policy = 'Stay-at-Home Requirements'):
    sunburst_data = df[[policy, policy +'_Day','continent', 'Entity']]
    fig = px.sunburst(sunburst_data, path=[policy, 'continent', 'Entity'], hover_data=[policy +'_Day'])
    fig.update_layout(
        **default_layout
    )
    return fig

def get_line_plot(trends, country_name = 'World'):
    df = trends[trends['Entity']==country_name].copy()
    fig = px.line(
        data_frame = df, 
        x="Day", 
        y=["retail_and_recreation", "grocery_and_pharmacy", "residential", "transit_stations", "parks", "workplaces"])
    fig.update_layout(
        **default_layout
    )
    return fig
