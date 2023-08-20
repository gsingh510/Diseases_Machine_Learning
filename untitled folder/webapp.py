#Dropdown
from dash import Dash, dcc, html, Input, Output, callback, State
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
            ),
            html.Br(),
        ]
        + [
            html.Div(id="out-all-types"),
            html.Br()
        ]
    ),
    html.Div(
    [
        # Add a button to call ml_model_func
        html.Button("Run ML Model", id="run-button"),
        html.Div(id="ml-output"),
    ]
    )
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
def cb_render(value):
    age = value
    return f'You have entered {value}'

# Create a callback function for the button
@app.callback(
    Output("ml-output", "children"),
    Input("run-button", "n_clicks"),
    [
        Input("demo-dropdown-1", "value"),
        Input("demo-dropdown-2", "value"),
        Input("demo-dropdown-3", "value"),
        Input("demo-dropdown-4", "value"),
        Input("demo-dropdown-5", "value"),
        Input("demo-dropdown-6", "value"),
        Input("demo-dropdown-7", "value"),
    ],
    [
        State("input_number", "value"),
    ]
)
def ml_model_callback(n_clicks, fever, cough, fatigue, breathing, gender, bp, cl, age):
    if n_clicks is None:
        return ""

    # normalize user input to  0s and 1s
    fever_num = 1 if fever == "Yes" else 0
    cough_num = 1 if cough == "Yes" else 0
    fatigue_num = 1 if fatigue == "Yes" else 0
    breathing_num = 1 if breathing == "Yes" else 0
    gender_num = 0 if gender == "Female" else 1
    bp_num = 1 if bp == "Low" else (2 if bp == "Normal" else 0)
    cl_num = 1 if cl == "Low" else (2 if cl == "Normal" else 0)

    # Call the ml_model_func with user inputs
    prediction, accuracy_score = ml_model_func(fever_num, cough_num, fatigue_num, breathing_num, gender_num, bp_num, cl_num, age)

    # format the accuracy 
    # 0.9455445454 -> %age
    percentage_value = accuracy_score * 100

    percentage_string = f'{percentage_value:.2f}%'

    display_msg = "low" if prediction == 0 else "high"
    return f"The likelihood you have a disease is {display_msg}. \n It was predicted with {percentage_string} accuracy. \n Consult a physician for further diagnosis."


# Remove the @callback decorator from ml_model_func
def ml_model_func(fever, cough, fatigue, breathing, gender, bp, cl, age):
    output = recommendation(fever, cough, fatigue, breathing, age, gender, bp, cl)
    return output

if __name__ == '__main__':
    app.run(debug=True)






