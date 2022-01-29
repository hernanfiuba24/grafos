import unittest

class Edge:
    def __init__(self, o, d, weight):
        self.o = o
        self.d = d
        self.weight = weight
    
    def origin(self):
        return self.o

    def destine(self):
        return self.d

    def weight(self):
        return self.weight

    def __repr__(self): 
        return self.o + "->" + self.d + " = " + str(self.weight)

class Graph:
    # V: list of vertices. Example: ["s", "n1", "n2", "n3", "n4", "n5", "t"]
    # A: list of edges. Example: [Egde("s", "n1", 3), Egde("s", "n2", 4), Egde("s", "n3", 3)]
    # adjacents: For each vertice has a list of adjacents
    def __init__(self, V, A):
        self.V = V
        self.A = A
        self.adjacents = [[]]*len(V)
        for edge in A:
            self.adjacents[V.index(edge.origin())].append(edge)
    
    def vertices(self):
        return self.V

    def edges(self):
        return self.A

    def adyacentTo(self, node):
        return self.adjacents[self.V.index(node)]
            

class GraphTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        V = ["s", "n1", "n2", "n3"]
        E = [Edge("s", "n1", 3), Edge("s", "n2", 4), Edge("s", "n3", 3)]
        cls.G = Graph(V,E)
    
    def test_count_vertices(self):
        self.assertTrue(len(self.G.vertices()) == 4 )
    
    def test_count_edges(self):
        self.assertTrue(len(self.G.edges()) == 3 )

    def test_count_adyacent_to(self):
        self.assertTrue(len(self.G.adyacentTo('s')) == 3 )

    def test_adyacent_to(self):
        self.assertEqual(self.G.adyacentTo('s')[0].destine(), 'n1')
        self.assertEqual(self.G.adyacentTo('s')[1].destine(), 'n2')
        self.assertEqual(self.G.adyacentTo('s')[2].destine(), 'n3')

if __name__ == "__main__":
    unittest.main()