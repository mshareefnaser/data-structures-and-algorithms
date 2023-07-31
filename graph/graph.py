from node import Node
from queue import Queue
from stack_and_queue.stack import Stack
class Edge:
    def __init__(self, vertex, wieght=0):
        """Initialize an edge with a vertex and optional wieght."""
        self.vertex = vertex
        self.wieght = wieght

    # def __repr__(self):
    #     """Return a string representation of the edge."""
    #     return str(self.vertex)


class Graph:
    def __init__(self):
        """Initialize an empty graph."""
        self.adj_list = {}

    def add_vertex(self, value):
        """Add a vertex to the graph with the given value."""
        vertex = Node(value)
        self.adj_list[vertex] = []
        return vertex

    def add_edge(self, vertex1, vertex2, weight = 0):
        """Add an edge between vertex1 and vertex2 in the graph."""
        if vertex1 not in self.adj_list.keys():
            raise ValueError('vertex1 doesn\'t exist')
        if vertex2 not in self.adj_list.keys():
            raise ValueError('vertex2 doesn\'t exist')

        edge1 = Edge(vertex2, weight)
        edge2 = Edge(vertex1, weight)
        self.adj_list[vertex1].append([edge1.vertex, edge1.wieght])
        self.adj_list[vertex2].append([edge2.vertex, edge2.wieght])


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

    def breadth_first(self, vertex):
        """ Return: A collection of nodes in the order they were visited."""
        nodes = []
        breadth = Queue()
        visited = set()
        breadth.put(vertex)
        visited.add(vertex)
        while not breadth.empty():
            front = breadth.get()
            nodes.append(front.value)
            for child in self.adj_list[front]:
                if child[0] not in visited:
                    visited.add(child[0])
                    breadth.put(child[0])
        return nodes
    def depth_first(self, vertex):
        """ Return: A collection of nodes in the order they were visited."""
        nodes = []
        depth = Stack()
        visited = set()
        depth.push(vertex)
        visited.add(vertex)
        while not depth.is_empty():
            top = depth.pop()
            nodes.append(top.value)
            for child in self.adj_list[top]:
                if child[0] not in visited:
                    visited.add(child[0])
                    depth.push(child[0])
        return nodes
    # def get_vertex(self, name):
    #     """get the whole vertex (as Node) from the vertex value"""
    #     v_list_nodes = self.get_vertices()
        
    #     if name 
# Create a new graph and add vertices and edges
g = Graph()
pandora = g.add_vertex('Pandora')
arendelle = g.add_vertex('Arendelle')
metroville = g.add_vertex('Metroville')
monstroplolis = g.add_vertex('Monstroplolis')
narnia = g.add_vertex('Narnia')
naboo = g.add_vertex('Naboo')

g.add_edge(pandora, arendelle,150)
g.add_edge(arendelle, metroville,99)
g.add_edge(arendelle, monstroplolis,42)
g.add_edge(metroville, monstroplolis,105)
g.add_edge(metroville, narnia,37)
g.add_edge(metroville, naboo,26)
g.add_edge(monstroplolis, naboo,73)
g.add_edge(narnia, naboo,250)

ne = g.get_neighbours(pandora)

