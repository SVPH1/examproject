import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import psycopg2
import pandas as pd

app = dash.Dash(__name__)

connection = psycopg2.connect(dbname="ENTSOE", user="postgres", password="5731", host="localhost", port="5432")

cursor = connection.cursor()
df_load = cursor.execute("SELECT * FROM load")

data = cursor.fetchall()
cols = []
for elt in cursor.description:
    cols.append(elt[0])

df_load = pd.DataFrame(data, columns=cols)


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
['actual_load'], name='FR_AL',line=dict(color='#85E085'),opacity=0.5)
# Define the layout of your app


dcc.Checklist(
        id='graph-checkboxes',
        options=[
            {'label': 'SE Forecasted Load', 'value': 'graph_1'},
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
    ),

dcc.Graph(
        id='graph'
    )


# Define the callback function that updates the graph based on the checkbox values
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('graph-checkboxes', 'value')])
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

    return {'data': data, 'layout': go.Layout(title='Multiple Graphs')}

if __name__ == '__main__':
    app.run_server(debug=True)