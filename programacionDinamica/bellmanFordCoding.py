# TODO: Create a graph and code dynamic programing 



# OPT[ni,j] = Minimun cost from 's' to 'ni' into less than j steps
# Recurrency ecuacion
# OPT[ni, j] = MIN { OPT[ni, j-1], 
#                   all p into prev(i)/ MIN { OPT[p, j-1] + weight(p,j) }
#                   }
# OPT[ni, 0] = INF
# OPT[s, j] = 0


import re
from graph import Graph, Edge
from matrix import Matrix

NODE_INITIAL = 's'
NODE_FINAL = 't'

MAX_WEIGHT = 10000

def bestPath(V, OPT):
    N = OPT.getRows()-1
    path = []
    edge = OPT.getValue(V.index(NODE_FINAL), N)[1]
    path.append(NODE_FINAL)
    while not edge == None:
        path.append(edge.origin())
        edge = OPT.getValue(V.index(edge.origin()), N)[1]
    return (path, OPT.getValue(V.index(NODE_FINAL), N)[0])

def buildGraph():
    V = ["s", "n1", "n2", "n3", "n4", "n5", "t"]
    E = [Edge("s", "n1", 1), Edge("s", "n2", 4), Edge("s", "n3", 5), Edge("n1", "n2", 1), Edge("n1", "n4", 1), Edge("n2", "n5", 3), Edge("n3", "n1", 2), Edge("n3", "t", 1),
    Edge("n4", "n5", 1), Edge("n5", "n3", 0), Edge("n5", "n1", 2), Edge("n5", "t", 2)]
    return Graph(V,E)

# arg:{'OPT': OPT, 'step', j-1, 'minCost': minCost}
def minCost(edge, arg):
    previousCost = arg['OPT'].getValue(arg['indexOrigin'], arg['step'])[0] + edge.weight()
    if previousCost < arg['minCost'][0]:
        arg['minCost'] = (previousCost, edge)
    return arg


def main():
    G = buildGraph()
    V = G.vertices()
    E = G.edges()
    N = len(V)

    OPT = Matrix(N, N)

    # Initialize
    for i in range(N):
        OPT.setValue(V.index(NODE_INITIAL), i, (0, None))
        OPT.setValue(i, 0, (MAX_WEIGHT, None))

    for j in range(1, N):
        for ni in V:
            if not ni == NODE_INITIAL:
                indexNi = V.index(ni)
                optLeft = OPT.getValue(indexNi, j-1)
                arg= {'OPT': OPT, 'step': j-1, 'minCost': (MAX_WEIGHT, None)}
                arg = G.runEachPrecentsTo(ni, arg, minCost)
                optRight = arg['minCost']
                if optLeft[0] < optRight[0]:
                    OPT.setValue(indexNi, j, optLeft)
                else:
                    OPT.setValue(indexNi, j, optRight)
    
    path = bestPath(V, OPT)
    print(OPT)
    print("Best route from [", NODE_INITIAL, "] to [", NODE_FINAL, "] is : ", path[0], " and the it costs: ", path[1])


if __name__ == '__main__':
    main()