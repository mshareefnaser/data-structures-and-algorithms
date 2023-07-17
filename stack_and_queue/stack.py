from node import Node


class Stack:
    """A class representing a Stack using a linked list."""

    def __init__(self):
        """Initialize an empty stack."""
        self.top = None
        self.size = 0

    def push(self, value):
        """Add an element to the top of the stack."""
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        """Remove and return the element from the top of the stack."""
        if not self.top:
            raise ValueError("Empty Stack")
        else:
            temp = self.top
            self.size -= 1
            self.top = self.top.next
            return temp.value

    def peek(self):
        """Return the element at the top of the stack without removing it."""
        if not self.top:
            raise ValueError("Empty Stack")
        else:
            return self.top.value

    def is_empty(self):
        """Check if the stack is empty."""
        if not self.top:
            return True
        else:
            return False
