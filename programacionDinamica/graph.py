from cmath import cos
import unittest

class Edge:
    def __init__(self, o, d, weight):
        self.o = o
        self.d = d
        self.w = weight
    
    def origin(self):
        return self.o

    def destine(self):
        return self.d

    def weight(self):
        return self.w

    # By error into minimum heap. Because, when firs values are equal, next it compares second value. And 
    # how second value is edge, so it should implement comparator. 
    def __lt__(self, other):
        return self.w < other.weight()

    def __repr__(self): 
        return self.o + "->" + self.d + " = " + str(self.w)

class Graph:
    # V: list of vertices. Example: ["s", "n1", "n2", "n3", "n4", "n5", "t"]
    # A: list of edges. Example: [Egde("s", "n1", 3), Egde("s", "n2", 4), Egde("s", "n3", 3)]
    # adjacents: For each vertice has a list of adjacents
    def __init__(self, V, A):
        self.V = V
        self.A = A
        self.adjacents = []
        self.precedents = []
        for i in range(len(V)):
            self.adjacents.append([])
            self.precedents.append([])
        for edge in A:
            adjacentsToNode = self.adjacents[V.index(edge.origin())]
            adjacentsToNode.append(edge)
            precedentsToNode = self.precedents[V.index(edge.destine())]
            precedentsToNode.append(edge)

    def vertices(self):
        return self.V

    def edges(self):
        return self.A

    def adjacentsTo(self, node):
        return self.adjacents[self.V.index(node)]
    
    def precedentsTo(self, node):
        return self.precedents[self.V.index(node)]
            
    def runEachPrecentsTo(self, node, arg, function):
        for edge in self.precedentsTo(node):
            arg['indexOrigin'] = self.V.index(edge.origin())
            arg = function(edge, arg)
        return arg
            

    

class GraphTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        V = ["s", "n1", "n2", "n3", "n4", "n5", "t"]
        E = [Edge("s", "n1", 1), Edge("s", "n2", 4), Edge("s", "n3", 5), Edge("n1", "n2", 1), Edge("n1", "n4", 1), Edge("n2", "n5", 3), Edge("n3", "n1", 2), Edge("n3", "t", 1),
        Edge("n4", "n5", 1), Edge("n5", "n3", 0), Edge("n5", "n1", 2), Edge("n5", "t", 2)]
        cls.G = Graph(V,E)
    
    def test_count_vertices(self):
        self.assertTrue(len(self.G.vertices()) == 7 )
    
    def test_count_edges(self):
        self.assertTrue(len(self.G.edges()) == 12 )

    def test_count_adyacent_to(self):
        self.assertTrue(len(self.G.adjacentsTo('s')) == 3 )

    def test_adyacents_to(self):
        self.assertEqual(self.G.adjacentsTo('s')[0].destine(), 'n1')
        self.assertEqual(self.G.adjacentsTo('s')[1].destine(), 'n2')
        self.assertEqual(self.G.adjacentsTo('s')[2].destine(), 'n3')

    def test_precedents_to(self):
        self.assertEqual(self.G.precedentsTo('n1')[0].origin(), 's')
        self.assertEqual(self.G.precedentsTo('n1')[1].origin(), 'n3')

if __name__ == "__main__":
    unittest.main()