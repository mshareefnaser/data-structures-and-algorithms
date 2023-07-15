from node import Node


class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, value):
        vertex = Node(value)
        self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        node1 = Node(vertex1)
        node2 = Node(vertex2)

        if self.adj_list.keys():
            raise ValueError('vertex1 doesn\'t exist')
        if node2 not in self.adj_list.keys():
            raise ValueError('vertex2 doesn\'t exist')

        edge1 = Edge(node2)
        edge2 = Edge(node1)
        self.adj_list[node1].append(edge1)
        self.adj_list[node2].append(edge2)

    def get_vertices(self):
        vertices = []
        for vertex in self.adj_list:
            vertices.append(vertex.value)
        return vertices
    
    def get_neighbours(self, vertex):
        edges = []
        for edge in self.adj_list[vertex]:
            edges.append(edge.vertex)
        return edges

    def __str__(self):
        graph_str = ''
        for vertex in self.adj_list.keys():
            graph_str += f'Vertex = {vertex}\n'
            graph_str += f'Edges = {self.adj_list[vertex]}\n'
        return graph_str
    
g = Graph()
a = g.add_vertex(1)
b = g.add_vertex(12)
print(g.get_vertices())
g.add_edge(a,b)

print (g.get_neighbours(12))