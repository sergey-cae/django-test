# from dash import dcc, html
# from dash.dependencies import Input, Output
# from django_plotly_dash import DjangoDash

# # Create and register the Dash app
# app = DjangoDash('SimpleDashApp')  # Ensure the name here is exactly the same as what you reference in the template

# # Define the layout of the Dash app
# app.layout = html.Div([
#     html.H1("Hello, Dash!"),
#     dcc.Dropdown(
#         id='dropdown',
#         options=[
#             {'label': 'Option 1', 'value': 'OPT1'},
#             {'label': 'Option 2', 'value': 'OPT2'},
#             {'label': 'Option 3', 'value': 'OPT3'}
#         ],
#         value='OPT1'
#     ),
#     html.Div(id='output-container')
# ])

# # Define a callback to update the output based on the selected dropdown value
# @app.callback(
#     Output('output-container', 'children'),
#     [Input('dropdown', 'value')]
# )
# def update_output(value):
#     return f"You selected: {value}"



# from dash import dcc, html
# from dash.dependencies import Input, Output
# import plotly.express as px
# from django_plotly_dash import DjangoDash
# import pandas as pd

# # Create the Dash app
# app = DjangoDash('SimpleDashApp')

# # Create some simple data
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "NYC", "NYC", "NYC"]
# })

# # Create a bar chart using Plotly Express
# bar_chart = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# # Create a line chart using Plotly Express
# line_chart = px.line(df, x="Fruit", y="Amount", color="City")

# # Define the layout of the Dash app
# app.layout = html.Div([
#     html.H1("Simple Dash App with Charts"),
#     dcc.Graph(
#         id='bar-chart',
#         figure=bar_chart
#     ),
#     dcc.Graph(
#         id='line-chart',
#         figure=line_chart
#     ),
#     dcc.Dropdown(
#         id='dropdown',
#         options=[
#             {'label': 'Option 1', 'value': 'OPT1'},
#             {'label': 'Option 2', 'value': 'OPT2'},
#             {'label': 'Option 3', 'value': 'OPT3'}
#         ],
#         value='OPT1'
#     ),
#     html.Div(id='output-container')
# ])

# # Define a callback to update the output based on the selected dropdown value
# @app.callback(
#     Output('output-container', 'children'),
#     [Input('dropdown', 'value')]
# )
# def update_output(value):
#     return f"You selected: {value}"



import dash
from dash import dcc, html

from django_plotly_dash import DjangoDash

app = DjangoDash('SimpleDashApp')   # replaces dash.Dash

app.layout = html.Div([
    dcc.RadioItems(
        id='dropdown-color',
        options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
        value='red'
    ),
    html.Div(id='output-color'),
    dcc.RadioItems(
        id='dropdown-size',
        options=[{'label': i,
                  'value': j} for i, j in [('L','large'), ('M','medium'), ('S','small')]],
        value='medium'
    ),

    html.Div(id='output-size')
])

@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value

@app.callback(
    dash.dependencies.Output('output-size', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value'),
     dash.dependencies.Input('dropdown-size', 'value')])
def callback_size(dropdown_color, dropdown_size):
    return "The chosen T-shirt is a %s %s one." %(dropdown_size,
                                                  dropdown_color)


