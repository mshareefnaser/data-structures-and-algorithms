from node import Node

class Edge:
    def __init__(self, vertex, weight=0):
        """Initialize an edge with a vertex and optional weight."""
        self.vertex = vertex
        self.weight = weight

    def __repr__(self):
        """Return a string representation of the edge."""
        return str(self.vertex)


class Graph:
    def __init__(self):
        """Initialize an empty graph."""
        self.adj_list = {}

    def add_vertex(self, value):
        """Add a vertex to the graph with the given value."""
        vertex = Node(value)
        self.adj_list[vertex] = []
        return vertex

    def add_edge(self, vertex1, vertex2):
        """Add an edge between vertex1 and vertex2 in the graph."""
        if vertex1 not in self.adj_list.keys():
            raise ValueError('vertex1 doesn\'t exist')
        if vertex2 not in self.adj_list.keys():
            raise ValueError('vertex2 doesn\'t exist')

        edge1 = Edge(vertex2)
        edge2 = Edge(vertex1)
        self.adj_list[vertex1].append(edge1)
        self.adj_list[vertex2].append(edge2)

    def get_vertices(self):
        """Return a list of all vertices in the graph."""
        return self.adj_list.keys()

    def get_neighbours(self, vertex):
        """Return a list of neighbors of a given vertex in the graph."""
        return self.adj_list[vertex]
    
    def get_size(self):
        """Return the number of vertices in the graph."""
        return len(self.adj_list)

    def __str__(self):
        """Return a string representation of the graph."""
        graph_str = ''
        for vertex in self.adj_list.keys():
            graph_str += f'Vertex = {vertex}\n'
            graph_str += f'Edges = {self.adj_list[vertex]}\n'
        return graph_str
