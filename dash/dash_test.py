# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:58:01 2023
@author: Åsa Ericsson
"""
# Import packages
import dash
#import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, ctx
import pandas as pd
import plotly.express as px
import sqlalchemy
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Option 1', 'value': 'option1'},
            {'label': 'Option 2', 'value': 'option2'},
            {'label': 'Option 3', 'value': 'option3'}
        ],
        value='option1'
    ),
    dcc.Checklist(
        id='checkbox',
        options=[
            {'label': 'Plot 1', 'value': 'plot1'},
            {'label': 'Plot 2', 'value': 'plot2'}
        ],
        value=['plot1']
    ),
    html.Div([
        dcc.Graph(id='plot1', style={'display': 'inline-block'}),
        dcc.Graph(id='plot2', style={'display': 'none'})
    ], className='row')
])

@app.callback(
    [Output('plot1', 'style'), Output('plot2', 'style')],
    Input('checkbox', 'value')
)
def toggle_plots(checked_values):
    plot1_style = {'display': 'none'}
    plot2_style = {'display': 'none'}
    if 'plot1' in checked_values:
        plot1_style = {'display': 'inline-block'}
    if 'plot2' in checked_values:
        plot2_style = {'display': 'inline-block'}
    return plot1_style, plot2_style

@app.callback(
    [Output('plot1', 'figure'), Output('plot2', 'figure')],
    Input('dropdown', 'value')
)
def update_figures(selected_option):
    # Generate the plots based on the selected option
    # and return them as a list of dictionaries
    if selected_option == 'option1':
        figures = [
            {'data': [{'x': [1, 2, 3], 'y': [4, 5, 6], 'type': 'bar'}]},
            {'data': [{'x': [1, 2, 3], 'y': [10, 20, 30], 'type': 'line'}]}
        ]
    elif selected_option == 'option2':
        figures = [
            {'data': [{'x': [1, 2, 3], 'y': [3, 6, 9], 'type': 'bar'}]},
            {'data': [{'x': [1, 2, 3], 'y': [5, 15, 25], 'type': 'line'}]}
        ]
    else:
        figures = [
            {'data': [{'x': [1, 2, 3], 'y': [2, 4, 8], 'type': 'bar'}]},
            {'data': [{'x': [1, 2, 3], 'y': [7, 14, 21], 'type': 'line'}]}
        ]
    
    return figures

if __name__ == '__main__':
    app.run_server(debug=True)