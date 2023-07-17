from stack import Stack
from queue import Queue
from pseudo_queue import PseudoQueue
from animal_shelter import AnimalShelter, Dog, Cat
from stack_queue_brackets import multi_bracket_validation
import pytest

# push onto a stack


def test_push_onto_stack():
    stack1 = Stack()
    stack1.push(1)
    actual = stack1.top.value
    expected = 1
    assert actual == expected

# push multiple values onto a stack

def test_push_multiple_values_onto_stack():
    stack1 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    actual = stack1.top.value
    expected = 3
    assert actual == expected

# pop off the stack

def test_pop_off_stack():
    stack1 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    actual = stack1.pop()
    expected = 3
    assert actual == expected

# empty a stack after multiple pops
def test_empty_stack_after_multiple_pops():
    stack1 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.pop()
    stack1.pop()
    stack1.pop()
    actual = stack1.is_empty()
    expected = True
    assert actual == expected

# peek the next item on the stack
def test_peek_next_item_on_stack():
    stack1 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    actual = stack1.peek()
    expected = 3
    assert actual == expected

# instantiate an empty stack
def test_instantiate_empty_stack():
    stack1 = Stack()
    actual = stack1.top
    expected = None
    assert actual == expected

# calling pop or peek on empty stack raises exception
def test_pop_on_empty_stack_raises_exception():
    stack1 = Stack()
    try:
        stack1.pop()
        assert False  
    except ValueError:
        assert True  


def test_peek_on_empty_stack_raises_exception():
    stack1 = Stack()
    try:
        stack1.peek()
        assert False
    except ValueError:
        assert True

# enqueue into a queue
def test_enqueue_into_queue():
    queue1 = Queue()
    queue1.enqueue(1)
    actual = queue1.front.value
    expected = 1
    assert actual == expected

# enqueue multiple values into a queue
def test_enqueue_multiple_values_into_queue():
    queue1 = Queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    actual = queue1.front.value
    expected = 1
    assert actual == expected

# dequeue out of a queue the expected value
def test_dequeue_out_of_queue_expected_value():
    queue1 = Queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    actual = queue1.dequeue()
    expected = 1
    assert actual == expected

# peek into a queue, seeing the expected value
def test_peek_into_queue_seeing_expected_value():
    queue1 = Queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    actual = queue1.peek()
    expected = 1
    assert actual == expected

# empty a queue after multiple dequeues
def test_empty_queue_after_multiple_dequeues():
    queue1 = Queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    queue1.dequeue()
    queue1.dequeue()
    queue1.dequeue()
    actual = queue1.is_empty()
    expected = True
    assert actual == expected

# instantiate an empty queue
def test_instantiate_empty_queue():
    queue1 = Queue()
    actual = queue1.front
    expected = None
    assert actual == expected

# calling dequeue or peek on empty queue raises exception
def test_dequeue_on_empty_queue_raises_exception():
    queue1 = Queue()
    try:
        queue1.dequeue()
        assert False
    except ValueError:
        assert True

def test_peek_on_empty_queue_raises_exception():
    queue1 = Queue()
    try:
        queue1.peek()
        assert False
    except ValueError:
        assert True

#test pseudo queue
def test_pseudo_queue():
    queue1 = PseudoQueue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    actual = queue1.dequeue()
    expected = 1
    assert actual == expected

#test animal shelter


def test_animal_shelter():
    shelter = AnimalShelter()
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    actual = str(shelter.dequeue('cat'))
    expected = str(Cat())
    assert actual == expected


def test_animal_shelter_empty():
    shelter = AnimalShelter()
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.dequeue('cat')
    shelter.dequeue('cat')
    shelter.dequeue('dog')
    shelter.dequeue('dog')
    with pytest.raises(ValueError) as error:
        shelter.dequeue('cat')
    assert str(error.value) == 'No animals available'

#test bracket validation
# test matching brackets
def test_bracket_validation_matching():
    actual = multi_bracket_validation('{}')
    expected = True
    assert actual == expected

# test non matching brackets
def test_bracket_validation_non_matching():
    actual = multi_bracket_validation('{(})')
    expected = False
    assert actual == expected
