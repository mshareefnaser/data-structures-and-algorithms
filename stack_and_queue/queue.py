from node import Node


class Queue:
    """A class representing a Queue using a linked list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """Add an element to the rear of the queue."""
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        if not self.front:
            raise ValueError("Empty Stack")
        if self.front == self.rear:
            self.rear = None

        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        """Return the element at the front of the queue without removing it."""
        if self.front is None:
            raise ValueError("Empty Stack")
        else:
            return self.front.value

    def is_empty(self):
        """Check if the queue is empty."""
        if self.front is None:
            return True
        else:
            return False
