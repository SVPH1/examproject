import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlalchemy
import pandas as pd
from dash.dependencies import Input, Output

engine = sqlalchemy.create_engine('postgresql://postgres:tAggA67!@localhost:5432/entsoe')
# Load data from the ENTSOE table into a pandas dataframe
df_load = pd.read_sql_table('load', engine)

# print (df_load)

fig_ba={
'data': [
{'x': df_load[df_load['country'] == 'DE']['timestamp'], 'y': df_load[df_load['country'] == 'DE']
['forecasted_load'], 'type': 'line', 'name': 'forecasted_load DE', 'line': {'color': 'red'}}
]
}

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
    # Generate the plots based on the selected option
    # and return them as a list of dictionaries
    if selected_option == 'option1':
        figures = fig_ba
    elif selected_option == 'option2':
        figures = [
            {'data': [{'x': [1, 5, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    elif selected_option == 'option3':
        figures = [
            {'data': [{'x': [1, 8, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
    elif selected_option == 'option4':
        figures = [
            {'data': [{'x': [1, 256, 3], 'y': [3, 6, 9], 'type': 'bar'}]}
        ]
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
    
    return figures

if __name__ == '__main__':
    app.run_server(debug=True)