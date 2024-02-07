from dash import Dash, html, dcc, Input, Output, callback, dash_table, ctx
from dash.exceptions import PreventUpdate
from dash import State
import requests
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Button('Click here to see the table', id='show-secret'),
    html.Br(),
    html.Div([
        html.Label("Select object type that you want to search:"),
        dcc.Checklist(
            id='object-type',
            options=[
                {'label': 'Airplanes', 'value': 'airplanes'},
                {'label': 'Landings', 'value': 'landings'},
                {'label': 'Departures', 'value': 'departures'}
            ],
            value=['airplanes'] 
        )
    ]),
    html.Br(),
    html.Label("Search:"),
    html.Div([
        dcc.Input(id='search-input', type='text', placeholder='Enter values'),
        html.Button('Search', id='search-button'),
    ]),
    html.Div(id='search-results'),
    html.Div(id='body-div'),
    html.Br(),
    html.Div([
        html.Label("Registration Number:"),
        dcc.Input(id='registration-number', type='text', placeholder='Enter registration number'),
        html.Label("Model:"),
        dcc.Input(id='model', type='text', placeholder='Enter model'),
        html.Label("Flight Type:"),
        dcc.Input(id='flight-type', type='text', placeholder='Enter flight type'),
        html.Label("Source:"),
        dcc.Input(id='source', type='text', placeholder='Enter source'),
        html.Label("Destination:"),
        dcc.Input(id='destination', type='text', placeholder='Enter destination'),
        html.Br(),
        html.Button('Add Object', id='add-object'),
    ]),
    html.Div(id='add-object-output'),
    html.Button('Delete rows from Airplanes', id='delete-rows-button')  # Button to delete selected rows
])

def fetch_data():
    url = 'http://127.0.0.1:8000/list_all_objects/'
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        if not data: 
            print("Error: Empty response received from the server.")
            return pd.DataFrame() 
        
        df_airplanes = pd.DataFrame(data['airplanes'])
        df_landings = pd.DataFrame(data['landings'])
        df_departures = pd.DataFrame(data['departures'])
        return df_airplanes, df_landings, df_departures
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()  

def search_object(df, search_value):
    if search_value:
        search_value = str(search_value)  # Convert search value to string for comparison
        # Filter the data frame based on the values in the first two columns
        filtered_df = df[df.iloc[:, 0].astype(str).str.contains(search_value, na=False) |   #the column id from the table
                         df.iloc[:, 1].astype(str).str.contains(search_value, na=False) |
                         df['source'].astype(str).str.contains(search_value, na=False) |    # additional column "source"
                         df['destination'].astype(str).str.contains(search_value, na=False)]    #the column regisstration)
        return filtered_df
    else:
        return df

@app.callback(
    Output('body-div', 'children'),
    Input('show-secret', 'n_clicks')
)
def update_output(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        df_airplanes, df_landings, df_departures = fetch_data()
        
        # Create Dash DataTable components for airplanes, landings, and departures
        table_airplanes = dash_table.DataTable(
            id='datatable-airplanes',
            columns=[{"name": i, "id": i} for i in df_airplanes.columns],
            data=df_airplanes.to_dict('records'),
            editable=False,
            row_deletable=True,
            # filter_action="native",
            # sort_action="native",
            # sort_mode="multi",
            row_selectable="multi",
            page_action="native",
            page_current=0,
            page_size=20,
        )
        
        table_landings = dash_table.DataTable(
            id='datatable-landings',
            columns=[{"name": i, "id": i} for i in df_landings.columns],
            data=df_landings.to_dict('records'),
            editable=False,
            row_deletable=True,
            # filter_action="native",
            # sort_action="native",
            # sort_mode="multi",
            row_selectable="multi",
            page_action="native",
            page_current=0,
            page_size=20,
        )
        
        table_departures = dash_table.DataTable(
            id='datatable-departures',
            columns=[{"name": i, "id": i} for i in df_departures.columns],
            data=df_departures.to_dict('records'),
            editable=False,
            row_deletable=True,
            # filter_action="native",
            # sort_action="native",
            # sort_mode="multi",
            row_selectable="multi",
            page_action="native",
            page_current=0,
            page_size=20,
        )

        return [html.H3("Tables with all objects:"),
                html.H3("__________________________________________________________________________________________________"),
                html.H3("Airplanes"), table_airplanes,
                html.H3("Landings"), table_landings,
                html.H3("Departures"), table_departures]

@app.callback(
    Output('search-results', 'children'),
    Input('search-button', 'n_clicks'),
    Input('search-input', 'value'),
    Input('object-type', 'value'),
    prevent_initial_call=True
)
def search_object_callback(n_clicks, search_value, object_type):
    df_airplanes, df_landings, df_departures = fetch_data()
    search_results_formatted = []
    
    for obj_type in object_type:
        if obj_type == 'airplanes':
            df = df_airplanes
        elif obj_type == 'landings':
            df = df_landings
        else:
            df = df_departures
        
        search_result = search_object(df, search_value)
        
        if not search_result.empty:
            search_results_formatted.append(html.H4(f"Search Results in {obj_type.capitalize()}:"))
            search_results_formatted.append(dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in search_result.columns],
                data=search_result.to_dict('records'),
                editable=False,
                # filter_action="native",
                # sort_action="native",
                # sort_mode="multi",
                row_selectable="multi",
                page_action="native",
                page_current=0,
                page_size=20,
            ))
    
    return search_results_formatted

@app.callback(
    Output('add-object-output', 'children'),
    Input('add-object', 'n_clicks'),
    State('registration-number', 'value'),
    State('model', 'value'),
    State('flight-type', 'value'),
    State('source', 'value'),
    State('destination', 'value')
) 
def add_object(n_clicks, registration_number, model, flight_type, source, destination):
    if not n_clicks:
        raise PreventUpdate
    
    payload = {
        'registration_number': registration_number,
        'model': model,
        'flight_type': flight_type,
        'source': source,
        'destination': destination
    }
    return save_to_database(payload)

@app.callback(
    Output('output', 'children'),
    [Input('datatable-airplanes', 'selected_rows')]
)
def display_selected_row_data(selected_rows):
    if selected_rows:
        print("Selected rows indices:", selected_rows)  # Print selected rows indices in the terminal
        # You can also print the corresponding row data if needed
        # print("Selected rows data:", [df.iloc[i] for i in selected_rows])
    return ""


@app.callback(
    Output('datatable-airplanes', 'data'),
    Input('delete-rows-button', 'n_clicks'),
    State('datatable-airplanes', 'selected_rows'),
    State('datatable-airplanes', 'data'),
    prevent_initial_call=True
)
def delete_selected_rows(n_clicks, selected_rows, data):
    if not n_clicks or not selected_rows:
        raise PreventUpdate

    # Get the identification numbers of selected rows to be deleted
    identification_numbers = [data[i]['_id'] for i in selected_rows]

    # Loop through each identification number and send a delete request
    for id_number in identification_numbers:
        delete_url = f'http://127.0.0.1:8000/delete_object/?object_type=airplanes&identification_number={id_number}'
        try:
            response = requests.delete(delete_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return f"Error deleting object with ID {id_number}: {e}"

    # After successful deletion, fetch and return updated data
    return fetch_data()[0].to_dict('records')


def save_to_database(payload):
    url = 'http://127.0.0.1:8000/register_airplane/'
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return "Object added successfully"
    except requests.exceptions.RequestException as e:
        return f"Error adding object: {e}"

if __name__ == '__main__':
    app.run_server(debug=True)
