from graph.graph import Graph
from graph.node import Node

def business_trip(graph:Graph, cities:list):
    """
    Takes in a graph and a list of cities.
    Return: True or False, depending on whether the trip is possible with direct flights, and how much it would cost.
    """
    cost = 0
    for index,city in enumerate(cities):
        if index < len(cities) - 1:
            neighbours = graph.get_neighbours(city)
            next_city_name = cities[index+1].value
            for neighbour in neighbours:
                neighbour_name = neighbour[0].value
                travel_cost = neighbour[1]
                if next_city_name == neighbour_name:
                    cost += travel_cost
                    break
            if cost == 0:
                return None
    return cost
