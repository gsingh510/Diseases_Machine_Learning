#Dropdown
from dash import Dash, dcc, html, Input, Output, State, callback
from collab_function import recommendation # backend api 

app = Dash(__name__)

ALLOWED_TYPES = (
    "number",
)

age = 0
fever = ""
cough = ""
fatigue = ""
breathing = ""
gender = ""
bp = ""
cl = ""



app.layout = html.Div([
    html.Div([
        html.H4('Fever?'),
        dcc.Dropdown(['Yes', 'No'], 'No', id='demo-dropdown-1'),
        html.Br(),
        html.Div(id='dd-output-container-1'),
    ]),
        # html.Br(),
    html.Div([
        html.H4('Cough?'),
        dcc.Dropdown(['Yes', 'No'], 'No', id='demo-dropdown-2'),
        html.Br(),
        html.Div(id='dd-output-container-2'),
    ]),
        # html.Br(),
    html.Div([
        html.H4('Fatigue?'),
        dcc.Dropdown(['Yes', 'No'], 'No', id='demo-dropdown-3'),
        html.Br(),
        html.Div(id='dd-output-container-3'),
    ]),
        # html.Br(),
    html.Div([
        html.H4('Difficulty Breathing?'),
        dcc.Dropdown(['Yes', 'No'], 'No', id='demo-dropdown-4'),
        html.Br(),
        html.Div(id='dd-output-container-4'),
    ]),
        # html.Br(),
    html.Div([
        html.H4('Gender?'),
        dcc.Dropdown(['Male', 'Female'], 'Female', id='demo-dropdown-5'),
        html.Br(),
        html.Div(id='dd-output-container-5'),
    ]),
        # html.Br(),
     html.Div([
        html.H4('Blood Pressure?'),
        dcc.Dropdown(['Low', 'Normal', 'High'], 'Low', id='demo-dropdown-6'),
        html.Br(),
        html.Div(id='dd-output-container-6'),
    ]),
        # html.Br(),
    html.Div([
        html.H4('Cholesterol Level?'),
        dcc.Dropdown(['Low', 'Normal', 'High'], 'Low', id='demo-dropdown-7'),
        html.Br(),
        html.Div(id='dd-output-container-7'),
    ]),
        # html.Br(),
    #Input
    html.Div(
        [
            html.H4('Age?'),
            dcc.Input(
                id="input_number",
                type="number",
                placeholder="input type number",
            )
        ]
        + [html.Div(id="out-all-types")]
    ),
    html.Div([
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])

])


@callback(
    Output('dd-output-container-1', 'children'),
    Input('demo-dropdown-1', 'value')
)
def update_output_1(value):
    fever = value 
    return f'You have selected {value}', 

@callback(
    Output('dd-output-container-2', 'children'),
    Input('demo-dropdown-2', 'value')
)
def update_output_2(value):
    cough = value
    return f'You have selected {value}'

@callback(
    Output('dd-output-container-3', 'children'),
    Input('demo-dropdown-3', 'value')
)
def update_output_3(value):
    fatigue = value
    return f'You have selected {value}'

@callback(
    Output('dd-output-container-4', 'children'),
    Input('demo-dropdown-4', 'value')
)
def update_output_4(value):
    breathing = value
    return f'You have selected {value}'

@callback(
    Output('dd-output-container-5', 'children'),
    Input('demo-dropdown-5', 'value')
)
def update_output_5(value):
    gender = value
    return f'You have selected {value}'

@callback(
    Output('dd-output-container-6', 'children'),
    Input('demo-dropdown-6', 'value')
)
def update_output_6(value):
    bp = value
    return f'You have selected {value}'

@callback(
    Output('dd-output-container-7', 'children'),
    Input('demo-dropdown-7', 'value')
)
def update_output_7(value):
    cl = value
    return f'You have selected {value}'

@callback(
    Output("out-all-types", "children"),
    Input("input_number", "value"),
)

@callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)


def cb_render(value):
    age = value
    return f'You have entered {value}'

@callback(
    Output('dd-output-container-8', 'children'),
    Input('demo-dropdown-1', 'fever'),
    Input('demo-dropdown-2', 'cough'),
    Input('demo-dropdown-3', 'fatigue'),
    Input('demo-dropdown-4', 'fever'),
    Input('demo-dropdown-5', 'fever'),
    Input('demo-dropdown-6', 'fever'),
    Input('demo-dropdown-7', 'fever')
)
def ml_model_func(fever, cough, fatigue):
    output = recommendation(fever, cough, fatigue, cl, cb)
    return f'The likelihood you have a disease is {output}'

if __name__ == '__main__':
    app.run(debug=True)





