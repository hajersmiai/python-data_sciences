from multiprocessing.sharedctypes import Value
from tkinter import Y
import matplotlib
matplotlib.use("agg")
import dash
from dash import html,dcc
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import numpy as np
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
from pathlib import Path as p




file_path = p(__file__).parent
df = pd.read_csv(p(file_path, "countries.csv"))

d= pd.DataFrame(df)
# print(d)
def create_graph(n):
        fig,ax = plt.subplots()
        x=np.linspace(0,170,170)
        ax.plot(x,d[n])
        return mpl_to_plotly(fig)

app=dash.Dash(__name__)
titles=[html.H1("Countries in the world"),
        html.H3("Statistic value"), 
        html.Div([
                html.Div([dcc.Dropdown(['GDPPC', 'Literacy','InfantMortality', 'Agriculture','Population','NetMigration'],value='GDPPC', id="demo_dropdown")],className="box1"),
                dcc.Graph(figure=create_graph('GDPPC'),id="value_graph")], className="items"
                )
]
app.layout =html.Div(titles)

@app.callback(
   Output("value_graph","figure"),[Input("demo_dropdown","value")]
)
def update_graph(dropdown_value):
    return create_graph(dropdown_value)

if __name__ == '__main__':
    app.run(port=8051,debug=True)