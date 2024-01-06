from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

# incorporate data into app.
df = px.data.medals_long()

# Components
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])
title = dcc.Markdown(children=" App that analyzes Olympic Medals")
graph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['Bar Plot', 'Scatter Plot'],
                        value='Bar Plot',
                        clearable=False)

# Layout
app.layout = dbc.Container([title, graph, dropdown])

# Callback 
@app.callback( #call back decorator
    Output(graph, component_property="figure"),
    Input(dropdown, component_property="value")
)
def update_graph(arg): #call back function
    if arg == "Bar Plot":
        fig = px.bar(data_frame=df, x="nation", y="count", color="medal")
    elif arg == "Scatter Plot":
        fig = px.scatter(data_frame=df, x="nation", y="count", color="medal")
    return fig

if __name__ == "__main__":
    app.run_server(port=7685)

