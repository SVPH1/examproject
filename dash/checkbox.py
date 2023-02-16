import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import psycopg2
import pandas as pd

app = dash.Dash(__name__)

connection = psycopg2.connect(dbname="entsoe", user="postgres", password="tAggA67!", host="localhost", port="5432")

cursor = connection.cursor()
df_load = cursor.execute("SELECT * FROM load")

data = cursor.fetchall()
cols = []
for elt in cursor.description:
    cols.append(elt[0])

df_load = pd.DataFrame(data, columns=cols)

df_load['timestamp'] = pd.to_datetime(df_load['timestamp'])

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
# Define the layout of your app
app.layout = html.Div(children=[
    html.H1(children='Multiple Graphs with Checkboxes'),

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

    dcc.RangeSlider(
        id='year-slider',
        min=df_load['timestamp'].min().year,
        max=df_load['timestamp'].max().year,
        value=[df_load['timestamp'].min().year, df_load['timestamp'].max().year],
        marks={str(year): str(year) for year in range(df_load['timestamp'].min().year, df_load['timestamp'].max().year + 1)},
        step=None
    ),

    dcc.Graph(
        id='graph'
    )
])

# Define the callback function that updates the graph based on the checkbox values and the year slider
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('graph-checkboxes', 'value'),
     dash.dependencies.Input('year-slider', 'value')])
def update_graph(checkbox_values, selected_years):
    # Filter the data based on the selected years
    filtered_df = df_load[(df_load['timestamp'] >= pd.to_datetime(str(selected_years[0]))) & (df_load['timestamp'] <= pd.to_datetime(str(selected_years[1])))]

    data = []
    for checkbox_value in checkbox_values:
        if checkbox_value == 'graph_1':
            data.append(go.Scatter(x=filtered_df[filtered_df['country'] == 'SE']['timestamp'], y=filtered_df[filtered_df['country'] == 'SE']['forecasted_load'], name='SE_FL', line=dict(color='#990000')))
        elif checkbox_value == 'graph_2':
            data.append(go.Scatter(x=filtered_df[filtered_df['country'] == 'SE']['timestamp'], y=filtered_df[filtered_df['country'] == 'SE']['actual_load'], name='SE_AL', line=dict(color='#FF9999'), opacity=0.5))
        elif checkbox_value == 'graph_3':
            data.append(go.Scatter(x=filtered_df[filtered_df['country'] == 'DE']['timestamp'], y=filtered_df[filtered_df['country'] == 'DE']['forecasted_load'], name='DE_FL', line=dict(color='#520052')))
        elif checkbox_value == 'graph_4':
            data.append(go.Scatter(x=filtered_df[filtered_df['country'] == 'DE']['timestamp'], y=filtered_df[filtered_df['country'] == 'DE']['actual_load'], name='DE_AL', line=dict(color='#E680E6'), opacity=0.5))
        elif checkbox_value == 'graph_5':
            data.append(go.Scatter(x=filtered_df[filtered_df['country'] == 'DK']['timestamp'], y=filtered_df[filtered_df['country'] == 'DK']['forecasted_load'], name='DK_FL', line=dict(color='#1F3D99')))
        elif checkbox_value == 'graph_6':
            data.append(go.Scatter(x=filtered_df[filtered_df['country'] == 'DK']['timestamp'], y=filtered_df[filtered_df['country'] == 'DK']['actual_load'], name='DK_AL', line=dict(color='#85A3FF'), opacity=0.5))
        elif checkbox_value == 'graph_7':
            data.append(go.Scatter(x=filtered_df[filtered_df['country'] == 'FR']['timestamp'], y=filtered_df[filtered_df['country'] == 'FR']['forecasted_load'], name='FR_FL', line=dict(color='#1A661A')))
        elif checkbox_value == 'graph_8':
            data.append(go.Scatter(x=filtered_df[filtered_df['country'] == 'FR']['timestamp'], y=filtered_df[filtered_df['country'] == 'FR']['actual_load'], name='FR_AL', line=dict(color='#85E085'), opacity=0.5))

    layout = go.Layout(title='Load Profiles', xaxis=dict(title='Time'), yaxis=dict(title='Load (MW)'))

    return go.Figure(data=data, layout=layout)

if __name__ == '__main__':
    app.run_server(debug=True)