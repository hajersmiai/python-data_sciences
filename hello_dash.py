import matplotlib
matplotlib.use("agg")
import dash
from dash import html,dcc
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import numpy as np
from dash.dependencies import Input, Output

def create_sin_graph(n=3):
        fig,ax = plt.subplots()
        x=np.linspace(0,n*np.pi,100)
        ax.plot(x,np.sin(x))
        return mpl_to_plotly(fig)

app=dash.Dash(__name__)
titles=[html.Div([html.H1("First Dash app"),
        html.H3("Bruxelles Formation 2024")],className="box"), 
        
        html.Div([html.Div([
        dcc.Slider(0,20,1,value=5,id="graph_slider")],className="box"),html.Div([
        dcc.Graph(figure=create_sin_graph(),id="sin_graph")],className="box")
        ])]
app.layout =html.Div(titles,className="border")

@app.callback(
   Output("sin_graph","figure"),[Input("graph_slider","value")]
)
def update_sin_graph(slider_value):
    return create_sin_graph(slider_value)



if __name__=="__main__":
    app.run(debug=True)
   