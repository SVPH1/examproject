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

# Initialise the App
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, ])
image_path = 'assets/logo.png'


#################
# 1 # Bar plot ##
#################

df = pd.read_csv('outfile.csv')
df['Unnamed: 0'] = pd.to_datetime(df['Unnamed: 0'])
df.set_index('Unnamed: 0', inplace=True)
# Data
df_ba = px.data.gapminder()
df_options = df_ba[df_ba["continent"].isin(["Europe"])]["country"].unique()
df_ba = df_ba[df_ba["country"].isin(["Spain", "United Kingdom"])]

# Figure
#fig_ba = oPlotly.line(df, x=df.index, y = 'Forecasted Load')
#fig.add_ba((=df['x'], y = df['Actual Load'], mode='lines', line=dict(width=2, color='red')
# Figure
fig_ba = px.bar(
   
    df_ba,
    x="year",
    y="lifeExp",
    color="country",
    barmode="group",
    title="Grouped Bar Chart",
    template="plotly_white",
)
fig_ba.update_yaxes(range=[60, 80])

# Dropdown
dropdown_ba = dcc.Dropdown(
    options=df_options, value=["Spain", "United Kingdom"], multi=True
)

# Slider
slider_ba = dcc.Slider(
    df_ba["year"].min(),
    df_ba["year"].max(),
    5,
    value=df_ba["year"].min() + 10,
    marks=None,
    tooltip={"placement": "bottom", "always_visible": True},
)

# Radio items
radio_items_ba = dbc.RadioItems(
    options=[
        {"label": "Day", "value": 0},
        {"label": "Week ", "value": 1},
        {"label": "Month", "value": 2},
        {"label": "Year", "value": 3}
    ],
    value=0,
    inline=True,
)

# Card content
card_content_ba_1 = dbc.Card([
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title"),
            html.P(
                "Here you might want to add some statics or further information for your dashboard",
            ),
        ])
    ])
    
card_content_ba_2 = dbc.Card([
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title"),
            html.P(
                "Here you might want to add some statics or further information for your dashboard",
            ),
        ])
    ])

card_content_ba_3 = dbc.Card([
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title"),
            html.P(
                "Here you might want to add some statics or further information for your dashboard",
            ),
        ])
    ])
##################
# 2 # Line plot ##
##################

# Data
df_li = px.data.stocks()
df_li["date"] = pd.to_datetime(df_li["date"], format="%Y-%m-%d")

# Figure
fig = px.line(
    df_li, x="date", y=["AAPL"], template="plotly_white", title="My Plotly Graph"
)

# Dropdown
dropdown = dcc.Dropdown(options=["AAPL", "GOOG", "MSFT"], value="AAPL")

# Date Picker
date_range = dcc.DatePickerRange(
    start_date_placeholder_text="start date",
    end_date_placeholder_text="end date",
    min_date_allowed=df_li.date.min(),
    max_date_allowed=df_li.date.max(),
    display_format="DD-MMM-YYYY",
    first_day_of_week=1,
)

# Checklist
checklist = dbc.Checklist(
    options=[{"label": "Dark theme", "value": 1}],
    value=[],
    switch=True,
)

# Radio items
radio_items = dbc.RadioItems(
    options=[
        {"label": "Red", "value": 0},
        {"label": "Green", "value": 1},
        {"label": "Blue", "value": 2},
    ],
    value=2,
    inline=True,
)

# Card content
card_content = [
    dbc.CardBody(
        [
            html.H5("Control Panel"),
            html.P(
                "1) Select an option of the dropdown",
            ),
            dropdown,
            html.Br(),
            html.P(
                "2) Pick a date range from the form",
            ),
            date_range,
            html.Br(),
            html.Hr(),
            html.H6("Optional input"),
            html.P(
                "3) Enable dark theme of your graph",
            ),
            checklist,
            html.Br(),
            html.P(
                "4) Change the color of the graphs line",
            ),
            radio_items,
        ]
    ),
]

#####################
# 3 # Scatter plot ##
#####################

# Data
df_sc = px.data.gapminder()
df_2007 = df_sc[df_sc.year == 2007]

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
        html.H2("Data Choice"),
        html.Hr(),
        html.P("Visualization options"),

        dbc.Button("Country comparison", color="light", n_clicks=0, id="Bar plot", style={'padding': '10px 20px','width': '180px'}),
        html.Hr(),
        dbc.Button("Energy ", color="light", n_clicks=0, id="Line plot", style={'padding': '10px 20px','width': '180px'}),
        html.Hr(),
        dbc.Button("El-områden in Sweden", color="light", n_clicks=0, id="Scatter plot", style={'padding': '10px 20px','width': '180px'}),
        html.Hr(),
        dbc.Button("Start Page", color="light", n_clicks=0, id="Start Page", style={'padding': '10px 20px', 'width': '180px'}),
        html.Hr(),
        html.Br(),  # Add a break to push the image to the bottom
        html.Br(),  # Add a break to push the image to the bottom
        html.Br(),  # Add a break to push the image to the bottom
        html.Br(),  # Add a break to push the image to the bottom
        html.Br(),  # Add a break to push the image to the bottom
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
    Input("Line plot", "n_clicks"),
    Input("Scatter plot", "n_clicks"),
    Input("Start Page", "n_clicks")
)
def update_page(n1, n2, n3, n4):
    if ctx.triggered_id == "Bar plot":
        return dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Card(
                                    dcc.Graph(id="figure1", figure=fig_ba),
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
                                dropdown_ba,
                            ]
                        ),
                        dbc.Col(
                            [
                                html.P("Select a year"),
                                slider_ba,
                            ]
                        ),
                        dbc.Col(
                            [
                                html.P("Select time period"),
                                radio_items_ba,
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
    elif ctx.triggered_id == "Line plot":
        return dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Row(dbc.Card(card_content, color="#A2BBBE")),
                            ],
                            width=4,
                        ),
                        dbc.Col(
                            dbc.Card(
                                dcc.Graph(id="figure1", figure=fig), color="light"
                            ),
                            width=8,
                        ),
                    ]
                ),
            ],
            className="bg-#A2BBBE",
            fluid=True,
            style={"height": "100vh"}, 
        )
    elif ctx.triggered_id == "Scatter plot":
        return dbc.Container(
            [
                html.H3("Analysis on Life Expectation / GDP per Capita in 2007"),
                dcc.Graph(
                    figure=px.scatter(
                        df_2007,
                        x="gdpPercap",
                        y="lifeExp",
                        color="continent",
                        size="pop",
                        size_max=60,
                    )
                ),
            ],
            className="bg-#A2BBBE",
            fluid=True,
            style={"height": "100vh"}, 
        )
    elif ctx.triggered_id == "Start Page":
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