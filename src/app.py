# Librerías:
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from sklearn.datasets import load_iris

# Creación de la app de Dash:

app=dash.Dash()

server=app.server

# Carga de datos:
df_iris = pd.DataFrame(load_iris().data, columns=load_iris().feature_names)

# Objetos plotly.graph:

data1 = [go.Scatter(x=df_iris["sepal length (cm)"],
                    y=df_iris["sepal width (cm)"],
                    mode="markers",
                    marker=dict(
                        size=8,
                        symbol="circle",
                        line={"width":1} # línea del marcador
                    ))]

layout1 = go.Layout(title="Iris Scatter Plot Sépalo",
                    xaxis=dict(title="Longitud del Sépalo"),
                    yaxis=dict(title="Anchura del Sépalo"))


data2 = [go.Scatter(x=df_iris["petal length (cm)"],
                    y=df_iris["petal width (cm)"],
                    mode="markers",
                    marker=dict(
                        size=8,
                        symbol="circle",
                        line={"width":1} # línea del marcador
                    ))]

layout2 = go.Layout(title="Iris Scatter Plot Pétalo",
                    xaxis=dict(title="Longitud del Pétalo"),
                    yaxis=dict(title="Anchura del Pétalo"))

# Definición de un diccionario de colores utilizados en la app

colors = {
    "background":"#8ecae6",
    "text":"#023047",
    "font-family":"sans-serif"
}

# Creación del layout de la app a partir de dcc y html (components de dash):
app.layout = html.Div(children=[
    
    html.H1(children="Primer Dashboard con Dash",
            style={# Estilos del componente H1:
                   "textAlign":"center",
                   "color":colors["text"],
                   "font-family":colors["font-family"]                   
            }
            
            ),
    
    html.Div([dcc.Graph(id="scatterplot",
                        figure={"data":data1,
                                "layout":layout1}),
              dcc.Graph(id="scatterplot2",
                        figure={"data":data2,
                                "layout":layout2})
              ]),
    
    html.Div(children="Dash es un Framework Web para Visualización de Datos con Python",
             style={# Estilos del Div interno:
                 "textAlign":"center",
                 "color":colors["text"],
                 "font-family":colors["font-family"]
             }
             ),
    
    
    dcc.Graph(
        id="ejemplo",
        figure={
            "data":[{"x":[1,2,3], "y":[4,8,2], "type":"bar", "name":"Guayaquil"},
                    {"x":[1,2,3], "y":[3,4,5], "type":"bar", "name":"Quito"},                    
                   ],
            "layout":{
                "title":"Comparativa Guayaquil - Quito",
                "plot_bgcolor":colors["background"],
                "paper_bgcolor":colors["background"],
                "font":{"color":colors["text"], "family": colors["font-family"]}
            }
        }
        
    )
    
],
    
    # style={"backgroundColor":colors["background"]}
                      
)

if __name__ == "__main__":
    app.run_server(port=8090, debug=True)