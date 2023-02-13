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
from sqlalchemy import text
# Connect to the database using SQLAlchemy
engine = sqlalchemy.create_engine('postgresql://postgres:tAggA67!@localhost:5432/entsoe')
# Load data from the ENTSOE table into a pandas dataframe
#df = pd.read_sql_table("load", engine)
# Display the first 5 rows of the dataframe
#print(df.head())
with engine.connect() as connection:
   df = pd.read_sql("SELECT * FROM load WHERE country = 'SE'",connection)
#print(df.columns.keys())
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(
        id='line-plot',
        figure={
            'data': [
                {'x': df['timestamp'], 'y': df['forecasted_load'], 'type': 'line', 'name': 'Forecasted Load'},
                {'x': df['timestamp'], 'y': df['actual_load'], 'type': 'line', 'name': 'Actual Load'},
            ],
            'layout': {
                'title': 'Line Plot of Forecasted Load and Actual Load'
            }
        }
    )
])
if __name__ == '__main__':
    app.run_server(debug=False)