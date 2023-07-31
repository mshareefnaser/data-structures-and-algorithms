import pytest
from graph.graph import Graph

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
    assert neighbors[0][0] == vertex2

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
    assert neighbors[0][0] == vertex2

# def test_get_neighbours_with_weight():
#     """Test retrieving neighbors with weights of a vertex in the graph."""
#     graph = Graph()
#     vertex1 = graph.add_vertex(1)
#     vertex2 = graph.add_vertex(2)
#     graph.add_edge(vertex1, vertex2)
#     neighbors = graph.get_neighbours(vertex1)
#     assert len(neighbors) == 1
#     assert neighbors[0].vertex == vertex2
#     assert neighbors[0].weight == 0  

def test_get_size():
    """Test retrieving the size (number of vertices) of the graph."""
    graph = Graph()
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    assert graph.get_size() == 2

def test_bfs():
    """Test breadth-first traversal of the graph."""
    g = Graph()
    pandora = g.add_vertex('Pandora')
    arendelle = g.add_vertex('Arendelle')
    metroville = g.add_vertex('Metroville')
    monstroplolis = g.add_vertex('Monstroplolis')
    narnia = g.add_vertex('Narnia')
    naboo = g.add_vertex('Naboo')

    g.add_edge(pandora, arendelle)
    g.add_edge(arendelle, metroville)
    g.add_edge(arendelle, monstroplolis)
    g.add_edge(metroville, monstroplolis)
    g.add_edge(metroville, narnia)
    g.add_edge(metroville, naboo)
    g.add_edge(monstroplolis, naboo)
    g.add_edge(narnia, naboo)

    actual = g.breadth_first(pandora)
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
    assert actual == expected

def test_dfs():
    """Test depth-first traversal of the graph."""
    g = Graph()
    pandora = g.add_vertex('Pandora')
    arendelle = g.add_vertex('Arendelle')
    metroville = g.add_vertex('Metroville')
    monstroplolis = g.add_vertex('Monstroplolis')
    narnia = g.add_vertex('Narnia')
    naboo = g.add_vertex('Naboo')

    g.add_edge(pandora, arendelle)
    g.add_edge(arendelle, metroville)
    g.add_edge(arendelle, monstroplolis)
    g.add_edge(metroville, monstroplolis)
    g.add_edge(metroville, narnia)
    g.add_edge(metroville, naboo)
    g.add_edge(monstroplolis, naboo)
    g.add_edge(narnia, naboo)

    actual = g.depth_first(pandora)
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Naboo', 'Narnia']
    assert actual == expected