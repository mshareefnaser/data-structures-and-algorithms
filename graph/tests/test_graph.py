import pytest
from graph import Graph

def test_add_vertex():
    """Test adding a vertex to the graph."""
    graph = Graph()
    vertex = graph.add_vertex(1)
    assert vertex.value == 1

def test_add_edge():
    """Test adding an edge between vertices in the graph."""
    graph = Graph()
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    graph.add_edge(vertex1, vertex2)
    neighbors = graph.get_neighbours(vertex1)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == vertex2

def test_get_vertices():
    """Test retrieving all vertices from the graph."""
    graph = Graph()
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    vertices = graph.get_vertices()
    assert len(vertices) == 2
    assert vertex1 in vertices
    assert vertex2 in vertices

def test_get_neighbours():
    """Test retrieving neighbors of a vertex in the graph."""
    graph = Graph()
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    graph.add_edge(vertex1, vertex2)
    neighbors = graph.get_neighbours(vertex1)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == vertex2

def test_get_neighbours_with_weight():
    """Test retrieving neighbors with weights of a vertex in the graph."""
    graph = Graph()
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    graph.add_edge(vertex1, vertex2)
    neighbors = graph.get_neighbours(vertex1)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == vertex2
    assert neighbors[0].weight == 0  

def test_get_size():
    """Test retrieving the size (number of vertices) of the graph."""
    graph = Graph()
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    assert graph.get_size() == 2
