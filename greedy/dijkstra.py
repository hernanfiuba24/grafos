
from heapq import heappop, heappush
from graph import Graph, Edge

def buildGraph():
    V = ["s", "n1", "n2", "n3", "n4", "n5", "t"]
    E = [Edge("s", "n1", 1), Edge("s", "n2", 4), Edge("s", "n3", 5), Edge("n1", "n2", 1), Edge("n1", "n4", 1), Edge("n2", "n5", 3), Edge("n3", "n1", 2), Edge("n3", "t", 1),
    Edge("n4", "n5", 1), Edge("n5", "n3", 0), Edge("n5", "n1", 2), Edge("n5", "t", 2)]
    return Graph(V,E)

NODE_ORIGIN = "s"
NODE_END = "t"

# {'s': None, 'n1': (1, s->n1 = 1), 'n2': (2, n1->n2 = 1), 'n4': (2, n1->n4 = 1), 'n5': (3, n4->n5 = 1), 'n3': (3, n5->n3 = 0), 't': (4, n3->t = 1)}
def bestPath(Alcanzados):
    before = Alcanzados[NODE_END]
    path = [NODE_END]
    while before != None and before[1].origin() != NODE_ORIGIN:
        path.append(before[1].origin())
        before = Alcanzados[before[1].origin()]
    path.append(NODE_ORIGIN)
    return (path, Alcanzados[NODE_END][0])


def main():
    G = buildGraph()
    V = G.vertices()
    E = G.edges()
    N = len(V)
    print(V)
    print(E)

    Alcanzados ={NODE_ORIGIN : None}
    Frontera = dict()
    
    for adjacentToS in G.adjacentsTo(NODE_ORIGIN):
        # key: Node destine 'x'
        # value: (cost from 's' to destine, edge from 'origin' to 'destine' )
        Frontera[adjacentToS.destine()] = (adjacentToS.weight(), adjacentToS)

    heapMinimum = []
    for key in Frontera.keys():
        heappush(heapMinimum, (Frontera[key][0], (Frontera[key])))

    end = False
    while not end:
        # minimun heap is updated by repeat values, neverless repeat keys are not procesing 
        x = heappop(heapMinimum)
        destine =x[1][1].destine()
        if not destine in Alcanzados.keys():
            for adjacentToX in G.adjacentsTo(destine):
                if not adjacentToX.destine() in Alcanzados.keys():
                    if (adjacentToX.destine() in Frontera):
                        # Update if is newCost is lessthan actual cost
                        actualCost = Frontera[adjacentToX.destine()][0]
                        newCost =  x[0] + adjacentToX.weight()
                        if newCost < actualCost:
                            Frontera[adjacentToX.destine()] = (newCost, adjacentToX)
                            heappush(heapMinimum, (Frontera[adjacentToX.destine()][0], (Frontera[adjacentToX.destine()])))
                    else:
                        Frontera[adjacentToX.destine()] = (x[0] + adjacentToX.weight(), adjacentToX)
                        heappush(heapMinimum, (Frontera[adjacentToX.destine()][0], (Frontera[adjacentToX.destine()])))
            Alcanzados[destine] = Frontera[destine]
            del(Frontera[destine])
        end = len(Frontera) <=  0
        
    path = bestPath(Alcanzados)
    print("The best path from [", NODE_ORIGIN, "] to [", NODE_END, "] is :", path[0], " and it cost : ", path[1])


if __name__ == '__main__':
    main()
    