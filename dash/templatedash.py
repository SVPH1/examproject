# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:20:32 2023

@author: Åsa Ericsson
"""

from dash import Dash, html, dcc
#import dash_core_components as dcc
#import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
#import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

fig2 = px.scatter(df, x="year", y="lifeExp",
                 size="pop", color="continent", hover_name="country",
                 log_x=True, size_max=60)

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.Div([
            html.H1(children='Graph1',
            style={
        'textAlign': 'center',
    }),

            html.Div(children='''
         Long long descreption
        ''', style={
        'textAlign': 'center',
    }),

            dcc.Graph(
                id='graph1',
                style={'width': '100vh', 'height': '90vh'},
                figure=fig2
            ),  
        ], className='six columns'),
        html.Div([
            html.H1(children='', 
            style={
        'textAlign': 'center',
    }),


    html.H1(children='Graph1',
            style={
        'textAlign': 'center',
        'padding-top': '45%',
    }),

     html.Div(children='''
         Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        ''', style={
        'textAlign': 'center',
    }),

    
        ], className='six columns'),
    ], className='row'),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Graph3', 
        style={
        'textAlign': 'center',
    }),

        html.Div(children='''
         Long long descreption
        ''', style={
        'textAlign': 'center',
    }),

    html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    )
]),
html.H1(children='Graph4',
        style={
        'text-align': 'center',
        'color': 'red',
    }),

    html.Div(children='''
         Long long descreption
        ''', style={
        'padding-top': '1%',
        'text-align': 'center',
        
    }),

        dcc.Graph(
            id='graph3',
            figure=fig2
        ),  
    ], className='row'),
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=75)

    fig.update_layout(transition_duration=500)

    return fig



if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)