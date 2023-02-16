# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:00:28 2023

@author: Åsa Ericsson
"""

# Import packages
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, ctx
import pandas as pd
import plotly.express as px
from sqlalchemy import text
import sqlalchemy
import plotly.graph_objects as go
import psycopg2

# Initialise the App
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, ])
image_path = 'assets/logo.png'

# Connect to the database using SQLAlchemy
engine = sqlalchemy.create_engine('postgresql://postgres:5731@localhost:5432/ENTSOE')

# Load data from the ENTSOE table into a pandas dataframe

df_load = pd.read_sql_table("load", engine)
#with engine.connect() as connection:
   #df_load= pd.read_sql("SELECT * FROM load",connection)
# Slider


#################
# 1 # Line plot ##
#################
# Line plot
graph_1 = go.Scatter(x=df_load[df_load['country'] == 'SE']['timestamp'], y=df_load[df_load['country'] == 'SE']
['forecasted_load'], name='SE_FL',line=dict(color='#990000'))
graph_2 = go.Scatter(x=df_load[df_load['country'] == 'SE']['timestamp'], y=df_load[df_load['country'] == 'SE']
['actual_load'], name='SE_AL',line=dict(color='#FF9999'),opacity=0.5)
graph_3 = go.Scatter(x=df_load[df_load['country'] == 'DE']['timestamp'], y=df_load[df_load['country'] == 'DE']
['forecasted_load'], name='DE_FL',line=dict(color='#520052'))
graph_4 = go.Scatter(x=df_load[df_load['country'] == 'DE']['timestamp'], y=df_load[df_load['country'] == 'DE']
['actual_load'], name='DE_AL',line=dict(color='#E680E6'),opacity=0.5)
graph_5 = go.Scatter(x=df_load[df_load['country'] == 'DK']['timestamp'], y=df_load[df_load['country'] == 'DK']
['forecasted_load'], name='DK_FL',line=dict(color='#1F3D99'))
graph_6 = go.Scatter(x=df_load[df_load['country'] == 'DK']['timestamp'], y=df_load[df_load['country'] == 'DK']
['actual_load'], name='DK_AL',line=dict(color='#85A3FF'),opacity=0.5)
graph_7 = go.Scatter(x=df_load[df_load['country'] == 'FR']['timestamp'], y=df_load[df_load['country'] == 'FR']
['forecasted_load'], name='FR_FL',line=dict(color='#1A661A'))
graph_8 = go.Scatter(x=df_load[df_load['country'] == 'FR']['timestamp'], y=df_load[df_load['country'] == 'FR']
['actual_load'], name='FR_AL',line=dict(color='#85E085'),opacity=0.5),



"""
# Slider
slider_ba = dcc.Slider(
    df_load["year"].min(),
    df_load["year"].max(),
    5,
    value=df_load["year"].min() + 10,
    marks=None,
    tooltip={"placement": "bottom", "always_visible": True},
)
"""

checklist = dcc.Checklist(
        id='graph-checkboxes',
        options=[
            {'label': 'SVERIGEEEEE', 'value': 'graph_1'},
            {'label': 'SE Actual Load', 'value': 'graph_2'},
            {'label': 'DE Forecasted Load', 'value': 'graph_3'},
            {'label': 'DE Actual Load', 'value': 'graph_4'},
            {'label': 'DK Forecasted Load', 'value': 'graph_5'},
            {'label': 'DK Actual Load', 'value': 'graph_6'},
            {'label': 'FR Forecasted Load', 'value': 'graph_7'},
            {'label': 'FR Actual Load', 'value': 'graph_8'},
            
        ],
        value=['graph_1'],
        labelStyle={'display': 'inline-block'}
    )

@app.callback(
    Output('graph', 'figure'),
    Input('graph-checkboxes', 'value'))
def checkbox(checkbox_values):
    data = []
    if 'graph_1' in checkbox_values:
        data.append(graph_1)
    if 'graph_2' in checkbox_values:
        data.append(graph_2)
    if 'graph_3' in checkbox_values:
        data.append(graph_3)
    if 'graph_4' in checkbox_values:
        data.append(graph_4)
    if 'graph_5' in checkbox_values:
        data.append(graph_5)
    if 'graph_6' in checkbox_values:
        data.append(graph_6)
    if 'graph_7' in checkbox_values:
        data.append(graph_7)
    if 'graph_8' in checkbox_values:
        data.append(graph_8)
    fig = {'data': data, 'layout': go.Layout(title='Multiple Graphs')}

    return fig

    
# Card content
card_content_ba_1 = dbc.Card([
    dbc.CardHeader("Covid-19"),
    dbc.CardBody(
        [
            html.H5("Important dates:"),
            html.P(
                "2020-01-31 - First confirmed case of COVID-19 in Sweden",
            ),
        ])
    ])
    
card_content_ba_2 = dbc.Card([
    dbc.CardHeader("Ukraine War"),
    dbc.CardBody(
        [
            html.H5("Important dates:"),
            html.P(
                "2022-02-24 - Russia invades Ukraine",
            ),
        ])
    ])

card_content_ba_3 = dbc.Card([
    dbc.CardHeader("This is also important"),
    dbc.CardBody(
        [
            html.H5("But not as important as the other two"),
            html.P(
                "",
            ),
        ])
    ])
##################
# 2 # Generation ##
##################

# SQL goes brrrrrr
###### GERMANY ######
query_de_2017 = "SELECT * FROM generation WHERE country = 'DE' and timestamp >= '2017-01-01' and timestamp <= '2017-12-31'"
query_de_2018 = "SELECT * FROM generation WHERE country = 'DE' and timestamp >= '2018-01-01' and timestamp <= '2018-12-31'"
query_de_2019 = "SELECT * FROM generation WHERE country = 'DE' and timestamp >= '2019-01-01' and timestamp <= '2019-12-31'"
query_de_2020 = "SELECT * FROM generation WHERE country = 'DE' and timestamp >= '2020-01-01' and timestamp <= '2020-12-31'"
query_de_2021 = "SELECT * FROM generation WHERE country = 'DE' and timestamp >= '2021-01-01' and timestamp <= '2021-12-31'"
query_de_2022 = "SELECT * FROM generation WHERE country = 'DE' and timestamp >= '2022-01-01' and timestamp <= '2022-12-31'"
df_generation_de_2017 = pd.read_sql_query(query_de_2017, engine)
df_generation_de_2018 = pd.read_sql_query(query_de_2018, engine)
df_generation_de_2019 = pd.read_sql_query(query_de_2019, engine)
df_generation_de_2020 = pd.read_sql_query(query_de_2020, engine)
df_generation_de_2021 = pd.read_sql_query(query_de_2021, engine)
df_generation_de_2022 = pd.read_sql_query(query_de_2022, engine)
###### DENMARK ######
query_dk_2017 = "SELECT * FROM generation WHERE country = 'DK' and timestamp >= '2017-01-01' and timestamp <= '2017-12-31'"
query_dk_2018 = "SELECT * FROM generation WHERE country = 'DK' and timestamp >= '2018-01-01' and timestamp <= '2018-12-31'"
query_dk_2019 = "SELECT * FROM generation WHERE country = 'DK' and timestamp >= '2019-01-01' and timestamp <= '2019-12-31'"
query_dk_2020 = "SELECT * FROM generation WHERE country = 'DK' and timestamp >= '2020-01-01' and timestamp <= '2020-12-31'"
query_dk_2021 = "SELECT * FROM generation WHERE country = 'DK' and timestamp >= '2021-01-01' and timestamp <= '2021-12-31'"
query_dk_2022 = "SELECT * FROM generation WHERE country = 'DK' and timestamp >= '2022-01-01' and timestamp <= '2022-12-31'"
df_generation_dk_2017 = pd.read_sql_query(query_dk_2017, engine)
df_generation_dk_2018 = pd.read_sql_query(query_dk_2018, engine)
df_generation_dk_2019 = pd.read_sql_query(query_dk_2019, engine)
df_generation_dk_2020 = pd.read_sql_query(query_dk_2020, engine)
df_generation_dk_2021 = pd.read_sql_query(query_dk_2021, engine)
df_generation_dk_2022 = pd.read_sql_query(query_dk_2022, engine)
###### FRANCE ######
query_fr_2017 = "SELECT * FROM generation WHERE country = 'FR' and timestamp >= '2017-01-01' and timestamp <= '2017-12-31'"
query_fr_2018 = "SELECT * FROM generation WHERE country = 'FR' and timestamp >= '2018-01-01' and timestamp <= '2018-12-31'"
query_fr_2019 = "SELECT * FROM generation WHERE country = 'FR' and timestamp >= '2019-01-01' and timestamp <= '2019-12-31'"
query_fr_2020 = "SELECT * FROM generation WHERE country = 'FR' and timestamp >= '2020-01-01' and timestamp <= '2020-12-31'"
query_fr_2021 = "SELECT * FROM generation WHERE country = 'FR' and timestamp >= '2021-01-01' and timestamp <= '2021-12-31'"
query_fr_2022 = "SELECT * FROM generation WHERE country = 'FR' and timestamp >= '2022-01-01' and timestamp <= '2022-12-31'"
df_generation_fr_2017 = pd.read_sql_query(query_fr_2017, engine)
df_generation_fr_2018 = pd.read_sql_query(query_fr_2018, engine)
df_generation_fr_2019 = pd.read_sql_query(query_fr_2019, engine)
df_generation_fr_2020 = pd.read_sql_query(query_fr_2020, engine)
df_generation_fr_2021 = pd.read_sql_query(query_fr_2021, engine)
df_generation_fr_2022 = pd.read_sql_query(query_fr_2022, engine)
###### SWEDEN ######
query_se_2017 = "SELECT * FROM generation WHERE country = 'SE' and timestamp >= '2017-01-01' and timestamp <= '2017-12-31'"
query_se_2018 = "SELECT * FROM generation WHERE country = 'SE' and timestamp >= '2018-01-01' and timestamp <= '2018-12-31'"
query_se_2019 = "SELECT * FROM generation WHERE country = 'SE' and timestamp >= '2019-01-01' and timestamp <= '2019-12-31'"
query_se_2020 = "SELECT * FROM generation WHERE country = 'SE' and timestamp >= '2020-01-01' and timestamp <= '2020-12-31'"
query_se_2021 = "SELECT * FROM generation WHERE country = 'SE' and timestamp >= '2021-01-01' and timestamp <= '2021-12-31'"
query_se_2022 = "SELECT * FROM generation WHERE country = 'SE' and timestamp >= '2022-01-01' and timestamp <= '2022-12-31'"
df_generation_se_2017 = pd.read_sql_query(query_se_2017, engine)
df_generation_se_2018 = pd.read_sql_query(query_se_2018, engine)
df_generation_se_2019 = pd.read_sql_query(query_se_2019, engine)
df_generation_se_2020 = pd.read_sql_query(query_se_2020, engine)
df_generation_se_2021 = pd.read_sql_query(query_se_2021, engine)
df_generation_se_2022 = pd.read_sql_query(query_se_2022, engine)


# Dropdown
radio_country = dbc.RadioItems(
    id='country_selector',
    options=[
        {"label": "Germany", "value": "DE"},
        {"label": "Denmark", "value": "DK"},
        {"label": "France", "value": "FR"},
        {"label": "Sweden", "value": "SE"}
    ],
    value="DE"
)

radio_time_period = dbc.RadioItems(
    id='year_selector',
    options=[
        {"label": "2017", "value": 0},
        {"label": "2018", "value": 1},
        {"label": "2019", "value": 2},
        {"label": "2020", "value": 3},
        {"label": "2021", "value": 4},
        {"label": "2022", "value": 5}
    ],
    value=0,
    inline=True
)

# Define the callback
@app.callback(
    Output('generation_graph', 'figure'),
    Input('year_selector', 'value'),
    Input('country_selector', 'value')

    #Hahahaha, ja du, går det så går det...
)
def generation_graph(year, country):
    if year == 0 and country == 'DE':
        df = df_generation_de_2017
    elif year == 1 and country == 'DE':
        df = df_generation_de_2018
    elif year == 2 and country == 'DE':
        df = df_generation_de_2019
    elif year == 3 and country == 'DE':
        df = df_generation_de_2020
    elif year == 4 and country == 'DE':
        df = df_generation_de_2021
    elif year == 5 and country == 'DE':
        df = df_generation_de_2022
    elif year == 0 and country == 'DK':
        df = df_generation_dk_2017
    elif year == 1 and country == 'DK':
        df = df_generation_dk_2018
    elif year == 2 and country == 'DK':
        df = df_generation_dk_2019
    elif year == 3 and country == 'DK':
        df = df_generation_dk_2020
    elif year == 4 and country == 'DK':
        df = df_generation_dk_2021
    elif year == 5 and country == 'DK':
        df = df_generation_dk_2022
    elif year == 0 and country == 'FR':
        df = df_generation_fr_2017
    elif year == 1 and country == 'FR':
        df = df_generation_fr_2018
    elif year == 2 and country == 'FR':
        df = df_generation_fr_2019
    elif year == 3 and country == 'FR':
        df = df_generation_fr_2020
    elif year == 4 and country == 'FR':
        df = df_generation_fr_2021
    elif year == 5 and country == 'FR':
        df = df_generation_fr_2022
    elif year == 0 and country == 'SE':
        df = df_generation_se_2017
    elif year == 1 and country == 'SE':
        df = df_generation_se_2018
    elif year == 2 and country == 'SE':
        df = df_generation_se_2019
    elif year == 3 and country == 'SE':
        df = df_generation_se_2020
    elif year == 4 and country == 'SE':
        df = df_generation_se_2021
    elif year == 5 and country == 'SE':
        df = df_generation_se_2022

    df_sum = df.groupby('country').sum()

    fig = px.bar(df_sum, x=df_sum.index, y=df_sum.columns,
                 barmode='group',
                 title='Total Generation by Source and Country')
    fig.update_layout(legend_title_text="Energy Source")
    return fig


# Card content
card_content_generation = [
    dbc.CardBody(
        [
            html.H4("This graph shows a country's total generation by source, for a given year"),
            html.Br(),
            html.H5(
                "1) Select a country",
            ),
            radio_country,
            html.Br(),
            html.Br(),
            html.H5(
                "2) Choose a year",
            ),
            radio_time_period,
            html.Br(),
            html.Hr(),
            
            
        ]
    ),
]

card_content_generation_tip = dbc.Card([
    dbc.CardBody(
        [
            html.H5("Tip:"),
            html.H6(
                "You can click on a title under energy source on the legend to remove it from the graph or double click it to view it on its own"),

        ]
        
        )
    ])

#####################################################3
#MAP
#####################################################3

# Setting up connection - DO NOT FORGET TO FEED CONNECTION INFO
connection = psycopg2.connect(
    host = "localhost",
    database = "ENTSOE",
    user = "postgres",
    password = "5731"
    )

# Create a cursor to perform database operations
cursor = connection.cursor()

# Executing a SQL query
# FROM "... load_table ..."


cursor.execute("SELECT * FROM se_zones_load WHERE timestamp >= '2017-01-01' AND timestamp < '2018-01-01';")

# Fetch result
data = cursor.fetchall()
cols = []
for elt in cursor.description:
    cols.append(elt[0])

# DataFrame from Database
df_map = pd.DataFrame(
    data = data,
    columns = cols
)
df_map = df_map.drop_duplicates()
df_map = df_map.groupby(df_map['se_zone'], as_index = False).sum()
print(df_map)

fig_map = go.Figure()

fig_map.add_trace(
    go.Choroplethmapbox(
        geojson = 'new_map.geojson', #Assign geojson file
        featureidkey = 'properties.se_zone', #Assign feature key
        locations = df_map['se_zone'], #Assign location data
        z = df_map['actual_load'], #Assign information data
        zauto = True,
        colorscale = 'orrd',
        showscale = True,
                ))
                
fig_map.update_layout( # Add the layout here
    mapbox_style="carto-positron",
    mapbox_zoom=6,
    mapbox_center={'lat': 57.43, 'lon': 11.60},
    title="Mapppy",
    
    )

#########################################################################################################
# 3 GENERATION SE ZONES ##
#########################################################################################################

query_se_1 = "SELECT se_zone, fossil_gas, hydro_water_reservoir, nuclear, other, solar, wind_onshore FROM se_zones_generation WHERE se_zone = 'SE_1';"
query_se_2 = "SELECT se_zone, fossil_gas, hydro_water_reservoir, nuclear, other, solar, wind_onshore FROM se_zones_generation WHERE se_zone = 'SE_2';"
query_se_3 = "SELECT se_zone, fossil_gas, hydro_water_reservoir, nuclear, other, solar, wind_onshore FROM se_zones_generation WHERE se_zone = 'SE_3';"
query_se_4 = "SELECT se_zone, fossil_gas, hydro_water_reservoir, nuclear, other, solar, wind_onshore FROM se_zones_generation WHERE se_zone = 'SE_4';"


df_generation_se_1 = pd.read_sql_query(query_se_1, engine)
df_generation_se_2 = pd.read_sql_query(query_se_2, engine)
df_generation_se_3 = pd.read_sql_query(query_se_3, engine)
df_generation_se_4 = pd.read_sql_query(query_se_4, engine)

radio_zone = dbc.RadioItems(
    id='zone_selector',
    options=[
        {"label": "Zone 1", "value": "SE_1"},
        {"label": "Zone 2", "value": "SE_2"},
        {"label": "Zone 3", "value": "SE_3"},
        {"label": "Zone 4", "value": "SE_4"},
    ],
    value="SE_1"
)

@app.callback(
    Output('se_zones_generation_graph', 'figure'),
    Input('zone_selector', 'value'))

def se_zones_generation_graph(zone):
    if zone == 'SE_1':
        df = df_generation_se_1
    elif zone == 'SE_2':
        df = df_generation_se_2
    elif zone == 'SE_3':
        df = df_generation_se_3
    elif zone == 'SE_4':
        df = df_generation_se_4

    df_sum = df.groupby('se_zone').sum()

    fig = px.bar(df_sum, x=df_sum.index, y=df_sum.columns,
                 barmode='group',
                 title='Total Generation by Source and Zone')
    fig.update_layout(legend_title_text="Energy Source")
    return fig

card_content_se_zones_generation =[
    dbc.CardBody(
        [
            html.H4("This graph shows Sweden's four different electrical zones and their total generation by source, for the year 2022"),
            html.Br(),
            html.H5(
                "Select a zone",
            ),
            radio_zone,
            html.Br(),
            html.Hr()
            
            
        ]
    ),
]


#########################################################################################################

# Styling
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#A2BBBE",
}
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "6rem 1rem",
    "background-color": "#A2BBBE"
}

# Sidebar
SIDEBAR_STYLE = {
    "background-color": "#A2BBBE",
    "padding": "20px 10px 20px 10px",
    "position": "fixed",
    "top": "0",
    "bottom": "0",
    "left": "0",
    "width": "200px",
}
sidebar = html.Div(
    [
        html.H2("Visualization options", style={"text-align": "center", "margin": "auto"}),
        html.Hr(),
        
        dbc.Button("Start Page", color="light", n_clicks=0, id="Start Page", style={'padding': '10px 20px', 'width': '180px'}),
        html.Hr(),
        dbc.Button("Country comparison", color="light", n_clicks=0, id="Bar plot", style={'padding': '10px 20px','width': '180px'}),
        html.Hr(),
        dbc.Button("Generation per country ", color="light", n_clicks=0, id="Generation per country", style={'padding': '10px 20px','width': '180px'}),
        html.Hr(),
        dbc.Button("Energy consumption for SE zones", color="light", n_clicks=0, id="Chloroplethmapbox", style={'padding': '10px 20px','width': '180px'}),
        html.Hr(),
        dbc.Button("Generation per SE zones", color="light", n_clicks=0, id="Generation per SE_zone", style={'padding': '10px 20px','width': '180px'}),
        html.Hr(),
        html.Br(),  # Add a break to push the image to the bottom
        html.Br(),  # Add a break to push the image to the bottom
        html.Br(),  # Add a break to push the image to the bottom
        html.Br(),  # Add a break to push the image to the bottom
        html.Br(),  # Add a break to push the image to the bottom
        

        html.Img(src=image_path, height=200, width=180), 
    ],
    style=SIDEBAR_STYLE,
)

# Title
title = dcc.Markdown("VIDA - Visualization of Entsoe data", className="bg-#235359", style={"font-size": 50 })

# Content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#A2BBBE"
}

content = html.Div(id="page-content", style=CONTENT_STYLE)

# App Layout
layout_style = {
    "background-color": "#A2BBBE",
    "padding": "40px",
    "color": "#235359"
}
app.layout = html.Div(
    [
        dbc.Row([dbc.Col([title], style={"text-align": "center", "margin": "auto"})]),
        sidebar,
        content,
    ],
    style=layout_style,
)

# Configure callbacks
@app.callback(
    Output("page-content", "children"),
    Input("Bar plot", "n_clicks"),
    Input("Generation per country", "n_clicks"),
    Input("Chloroplethmapbox", "n_clicks"),
    Input("Generation per SE_zone", "n_clicks"),
    Input("Start Page", "n_clicks")
    
)
def update_page(n1, n2, n3, n4, n5):
    if ctx.triggered_id == "Bar plot":
        return dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Card(
                                    dcc.Graph(id='graph'),
                                    color="light",
                                )
                            ]
                        ),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P("Select the countries to display"),
                                checklist,
                            ]
                        ),
                        dbc.Col(
                            [
                                #html.P("Select a year"),
                               # slider_ba,
                            ]
                        ),
                        dbc.Col(
                            [
                            
                                
                            ]
                        ),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Card(card_content_ba_1, color="light")]),
                        dbc.Col([dbc.Card(card_content_ba_2, color="light")]),
                        dbc.Col([dbc.Card(card_content_ba_3, color="light")]),
                    ]
                ),
            ],
            className="bg-#A2BBBE",
            fluid=True,
            style={"height": "100vh"},  
        )
    elif ctx.triggered_id == "Generation per country":
        return dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Row(dbc.Card(card_content_generation, color="#A2BBBE")),
                            ],
                            width=4,
                        ),
                        dbc.Col(
                            dbc.Card(
                                dcc.Graph(id='generation_graph'), color="light"
                            ),
                            width=8,
                        ),
                        dbc.Col( [dbc.Card(card_content_generation_tip, color="light", style={'padding': '0px 0px', 'width': '475px'} )]),
                    ]
                ),
            ],
            className="bg-#A2BBBE",
            fluid=True,
            style={"height": "100vh"}, 
        )
    elif ctx.triggered_id == "Chloroplethmapbox":
                return dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                dcc.Graph(id='nisse', figure=fig_map), color="light"
                            ),
                            width=8,
                        ),
                        
                    ]
                )
        
        ],
            className="bg-#A2BBBE",
            fluid=True,
            style={"height": "100vh"}, 
        )    
    elif ctx.triggered_id == "Generation per SE_zone":
        return dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Row(dbc.Card(card_content_se_zones_generation, color="#A2BBBE")),
                            ],
                            width=4,
                        ),
                        dbc.Col(
                            dbc.Card(
                                dcc.Graph(id='se_zones_generation_graph'), color="light"
                            ),
                            width=8,
                        ),
                        # dbc.Col([dbc.Card(card_content_se_zones_generation, color="light")]),
                    ]
                ),
            ],
            className="bg-#A2BBBE",
            fluid=True,
            style={"height": "100vh"}, 
        )
    elif ctx.triggered_id == "Start Page":
        return dbc.Container(
            [   html.H2("Welcome to VIDA",
            className="text-center"),
                html.Br(),
                html.H5(
                    "Please navigate to an analysed data set with the navigation on the left.",
                    className="text-center"
                ),
            ],
            
            className="bg-#A2BBBE",
            fluid=True,
            style={"height": "100vh"},
        )
    else:
        return dbc.Container(
            [
                html.H5(
                    "Please navigate to an analysed data set with the navigation on the left.",
                    className="text-center"
                ),
            ],
            
            className="bg-#A2BBBE",
            fluid=True,
            style={"height": "100vh"},
        )



# Run the App
if __name__ == "__main__":
    app.run_server(debug=False)