import pygraphviz as pgv
from grafo import *

def iterarSobreAdyacentesA(nodo, args):
    args["grafoDibujable"].add_node(nodo)
    args["G"].iterarSobreAdyacentesA(nodo, cargarArista, {"grafoDibujable": args["grafoDibujable"], "nodo": nodo})
    return args

def cargarArista(nodoAdyacente, args):
    args["grafoDibujable"].add_edge(args["nodo"], nodoAdyacente)
    return args

def grafoDibujable(G):
    grafoDibujable = pgv.AGraph(directed=G.esDirigido(), format='png', engine='sfdp')
    G.iterarSobreNodos(iterarSobreAdyacentesA, {"grafoDibujable": grafoDibujable, "G": G})
    return grafoDibujable

def dibujar(grafoDibujable):
    grafoDibujable.graph_attr['rankdir'] = "LR"
    grafoDibujable.graph_attr['center'] = True
    grafoDibujable.graph_attr['size'] = '8.5'

    grafoDibujable.node_attr['shape'] = 'circle'
    
    grafoDibujable.edge_attr['color'] = 'black'
    grafoDibujable.layout()
    grafoDibujable.draw("./grafo.png")

def dibujargrafo(G):
    dibujar(grafoDibujable(G))
