from grafo import *

def cargarGrafo(ruta, dirigido):
    grafo = None
    with open(ruta, 'r') as file:
        cantidadNodos = int(file.readline())
        file.readline()
        grafo = Grafo(cantidadNodos, dirigido)
        for aristaStr in file.readlines():
            nodoInicio = (aristaStr.split(' ')[0]).rstrip("\n")
            nodoDestino = (aristaStr.split(' ')[1]).rstrip("\n")
            grafo.agregarArista(nodoInicio, nodoDestino)
            if (not dirigido):
                grafo.agregarArista(nodoDestino, nodoInicio)
    return grafo