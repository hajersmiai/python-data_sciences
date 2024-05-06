import matplotlib
matplotlib.use("agg")
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly

folder_path = Path(__file__).parent
df = pd.read_csv(Path(folder_path, "countries.csv"), sep=",")

def create_graph(xcol="GDPPC",ycol="GDPPC"):
    fig, ax = plt.subplots()

    x = df[xcol]
    y = df[ycol]
    ax.scatter(x, y)

    return mpl_to_plotly(fig)


app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(figure=create_graph(), id="country-graph"),
    dcc.Dropdown(["GDPPC","Literacy","InfantMortality",
                  "Agriculture","Population","NetMigration"], value="GDPPC", id="x-axis"),
    dcc.Dropdown(["GDPPC","Literacy","InfantMortality",
                  "Agriculture","Population","NetMigration"], value="GDPPC", id="y-axis")

])


@app.callback(
    Output("country-graph", "figure"),
    [Input("x-axis", "value"),Input("y-axis","value")]
)
def update_graph(x_column,y_column):
    return create_graph(x_column,y_column)


if __name__ == "__main__":
    app.run(debug=True,port=8052)

