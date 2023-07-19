import pytest
from graph.graph import Graph
from graph.graph_business_trip import business_trip

g = Graph()
pandora = g.add_vertex('Pandora')
arendelle = g.add_vertex('Arendelle')
metroville = g.add_vertex('Metroville')
monstroplolis = g.add_vertex('Monstroplolis')
narnia = g.add_vertex('Narnia')
naboo = g.add_vertex('Naboo')

g.add_edge(pandora, metroville, 82)
g.add_edge(pandora, arendelle, 150)
g.add_edge(arendelle, metroville, 99)
g.add_edge(arendelle, monstroplolis, 42)
g.add_edge(metroville, monstroplolis, 105)
g.add_edge(metroville, narnia, 37)
g.add_edge(metroville, naboo, 26)
g.add_edge(monstroplolis, naboo, 73)
g.add_edge(narnia, naboo, 250)


def test_no_trip():
    """
    Test case for the business_trip function when there is no trip between cities.
    """
    actual = business_trip(g, [narnia, arendelle, naboo])
    expected = None
    assert actual == expected


def test_with_trip():
    """
    Test case for the business_trip function when there is a trip between cities.
    """
    actual = business_trip(g, [narnia, naboo, monstroplolis])
    expected = 323
    assert actual == expected


def test_one_city():
    """
    Test case for the business_trip function when there is only one city in the trip.
    """
    actual = business_trip(g, [narnia])
    expected = 0
    assert actual == expected
