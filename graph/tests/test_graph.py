import pytest 
from graph import Graph


def test_creating_empty_graph():
    g = Graph()
    actual = g.adj_list 
    expected = {}
    assert actual == expected
    
def test_add_vertex():
    g = Graph()
    g.add_vertex(11)
    g.add_vertex(9)
    actual = g.get_vertices()
    expected = [11,9]
    assert actual == expected

def test_add_edge():
    g = Graph()
    g.add_vertex(11)
    g.add_vertex(9)
    g.add_edge(9,11)
    print(g.get_vertices())
    actual = g.get_neighbours(11)
    expected = None
    assert actual == expected

test_add_edge()