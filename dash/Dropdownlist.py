import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlalchemy
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:tAggA67!@localhost:5432/entsoe')
# Load data from the ENTSOE table into a pandas dataframe
df_load = pd.read_sql_table('load', engine)

# print (df_load)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'SE', 'value': 'option1'},
            {'label': 'DE', 'value': 'option2'},
            {'label': 'DK', 'value': 'option3'},
            {'label': 'FR', 'value': 'option4'},
            {'label': 'SE+DE', 'value': 'option5'},
            {'label': 'SE+DK', 'value': 'option6'},
            {'label': 'SE+FR', 'value': 'option7'},
            {'label': 'DE+DK', 'value': 'option8'},
            {'label': 'DE+FR', 'value': 'option9'},
            {'label': 'DK+FR', 'value': 'option10'},
            {'label': 'SE+DE+DK', 'value': 'option11'},
            {'label': 'SE+DK+FR', 'value': 'option12'},
            {'label': 'DE+DK+FR', 'value': 'option13'},
            {'label': 'SE+DE+FR', 'value': 'option14'},
            {'label': 'SE+DE+DK+FR', 'value': 'option15'},
           
        ],
        value='option1'
    ),
    html.Div([
        dcc.Graph(id='plot1'),
    ], className='row')
])

@app.callback(
    [Output('plot1', 'figure')],
    Input('dropdown', 'value')
)
def update_figures(selected_option):
    if selected_option == 'option1':
        # Filter the DataFrame for the selected country
        df_filtered = df_load[df_load['country'] == 'SE']
        # Create a line chart with the filtered data
        figures = {'data': [go.Scatter(x=df_filtered['timestamp'], y=df_filtered['forecasted_load'],
        mode='lines', name='forecasted_load SE', line={'color': 'red'})]}
        # Update the layout of the figure
        figures['layout'] = {'title': 'SE Forecasted Load', 'xaxis': {'title': 'Timestamp'}, 'yaxis': {'title': 'Load'}}

        return [{'data': [{'x': df_load[df_load['country'] == 'SE']['timestamp'], 'y': df_load[df_load['country'] == 'SE']
        ['forecasted_load'], 'type': 'line', 'name': 'forecasted_load SE', 'line': {'color': 'blue'}}]}]


    elif selected_option == 'option2':
        # Filter the DataFrame for the selected country
        df_filtered = df_load[df_load['country'] == 'DE']
        # Create a line chart with the filtered data
        figures = {'data': [go.Scatter(x=df_filtered['timestamp'], y=df_filtered['forecasted_load'],
        mode='lines', name='forecasted_load DE', line={'color': 'red'})]}
        # Update the layout of the figure
        figures['layout'] = {'title': 'DE Forecasted Load', 'xaxis': {'title': 'Timestamp'}, 'yaxis': {'title': 'Load'}}

        return [{'data': [{'x': df_load[df_load['country'] == 'DE']['timestamp'], 'y': df_load[df_load['country'] == 'DE']
        ['forecasted_load'], 'type': 'line', 'name': 'forecasted_load DE', 'line': {'color': 'red'}}]}]

    

    elif selected_option == 'option3':
        # Filter the DataFrame for the selected country
        df_filtered = df_load[df_load['country'] == 'DK']
        # Create a line chart with the filtered data
        figures = {'data': [go.Scatter(x=df_filtered['timestamp'], y=df_filtered['forecasted_load'],
        mode='lines', name='forecasted_load DK', line={'color': 'yellow'})]}
        # Update the layout of the figure
        figures['layout'] = {'title': 'DK Forecasted Load', 'xaxis': {'title': 'Timestamp'}, 'yaxis': {'title': 'Load'}}

        return [{'data': [{'x': df_load[df_load['country'] == 'DK']['timestamp'], 'y': df_load[df_load['country'] == 'DK']
        ['forecasted_load'], 'type': 'line', 'name': 'forecasted_load DK', 'line': {'color': 'yellow'}}]}]

    elif selected_option == 'option4':
         # Filter the DataFrame for the selected country
        df_filtered = df_load[df_load['country'] == 'FR']
        # Create a line chart with the filtered data
        figures = {'data': [go.Scatter(x=df_filtered['timestamp'], y=df_filtered['forecasted_load'],
        mode='lines', name='forecasted_load FR', line={'color': 'green'})]}
        # Update the layout of the figure
        figures['layout'] = {'title': 'FR Forecasted Load', 'xaxis': {'title': 'Timestamp'}, 'yaxis': {'title': 'Load'}}

        return [{'data': [{'x': df_load[df_load['country'] == 'FR']['timestamp'], 'y': df_load[df_load['country'] == 'FR']
        ['forecasted_load'], 'type': 'line', 'name': 'forecasted_load FR', 'line': {'color': 'green'}}]}]

       
    elif selected_option == 'option5':
        figures = [
            {'data': [{'x': [1, 232, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    elif selected_option == 'option6':
        figures = [
            {'data': [{'x': [1, 21, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    elif selected_option == 'option7':
        figures = [
            {'data': [{'x': [1, 2, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    elif selected_option == 'option8':
        figures = [
            {'data': [{'x': [1, 62, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    elif selected_option == 'option9':
        figures = [
            {'data': [{'x': [1, 2, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    elif selected_option == 'option10':
        figures = [
            {'data': [{'x': [1, 2, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    elif selected_option == 'option11':
        figures = [
            {'data': [{'x': [1, 2, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    elif selected_option == 'option12':
        figures = [
            {'data': [{'x': [1, 2, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    elif selected_option == 'option13':
        figures = [
            {'data': [{'x': [1, 2, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    elif selected_option == 'option14':
        figures = [
            {'data': [{'x': [1, 2, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    elif selected_option == 'option15':
        figures = [
            {'data': [{'x': [1, 2, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    else:
        figures = [
            {'data': [{'x': [1, 2, 3], 'y': [2, 4, 8], 'type': 'bar'}]}
        ]
    
    # return figures

if __name__ == '__main__':
    app.run_server(debug=True)