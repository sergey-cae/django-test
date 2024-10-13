from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from django_plotly_dash import DjangoDash
import pandas as pd

# Create the Dash app
app = DjangoDash('TestDashApp')

# Create some simple data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "NYC", "NYC"]
})

# Create a bar chart using Plotly Express
bar_chart = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Create a line chart using Plotly Express
line_chart = px.line(df, x="Fruit", y="Amount", color="City")

# Define the layout of the Dash app
app.layout = html.Div([
    html.H1("Simple Dash App with Charts"),

    # Wrap both charts in a flexbox container
    html.Div([
        dcc.Graph(
            id='bar-chart',
            figure=bar_chart,
            style={'height': '400px', 'width': '50%'}  # Set each chart to take 50% width
        ),
        dcc.Graph(
            id='line-chart',
            figure=line_chart,
            style={'height': '400px', 'width': '50%'}  # Set each chart to take 50% width
        ),
    ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-between'}),  # Flexbox properties

    # Dropdown for selecting options
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Option 1', 'value': 'OPT1'},
            {'label': 'Option 2', 'value': 'OPT2'},
            {'label': 'Option 3', 'value': 'OPT3'}
        ],
        value='OPT1'
    ),
    html.Div(id='output-container')
])

# Define a callback to update the output based on the selected dropdown value
@app.callback(
    Output('output-container', 'children'),
    [Input('dropdown', 'value')]
)
def update_output(value):
    return f"You selected: {value}"
