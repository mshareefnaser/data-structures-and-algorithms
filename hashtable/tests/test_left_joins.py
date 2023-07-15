import pytest
from hashmap_left_join import left_joins

def test_left_joins_non_empty_hash_tables():
    """
    This test case verifies that the `left_joins` function correctly performs a left join operation
    on two non-empty hash tables and returns the expected result.
    """
    hash1 = {'A': 'Apple', 'B': 'Banana'}
    hash2 = {'A': 'Ant', 'B': 'Bear'}
    assert left_joins(hash1, hash2) == [['A', 'Apple', 'Ant'], ['B', 'Banana', 'Bear']]


def test_left_join_with_empty_right_input():
    """
    This test case verifies the behavior of the `left_joins` function when the right input hash table is empty.
    """
    hash1 = {'A': 'Apple'}
    hash2 = {}
    assert left_joins(hash1, hash2) == [['A', 'Apple', 'NONE']]


def test_left_join_with_empty_left_input():
    """
    This test case verifies the behavior of the `left_joins` function when the left input hash table is empty.
    """
    hash1 = {}
    hash2 = {'X': 'XYZ', 'Y': 'Yellow'}
    assert left_joins(hash1, hash2) == []

