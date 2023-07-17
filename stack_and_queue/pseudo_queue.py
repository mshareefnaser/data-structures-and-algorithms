from stack import Stack


class PseudoQueue:
    """A class representing a Queue implemented using two Stacks."""

    def __init__(self):
        """Initialize an empty pseudo queue."""
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """Add an element to the rear of the pseudo queue."""
        #Big O(1)
        #Space O(1)
        self.stack1.push(value)

    def dequeue(self):
        """Remove and return the element from the front of the pseudo queue."""
        #Big O(n)
        #Space O(1)
        if self.stack1.is_empty() and self.stack2.is_empty():
            raise Exception("Queue is empty")
        elif self.stack2.is_empty():
            while self.stack1.top:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def __str__(self):
        """Return a string representation of the pseudo queue."""
        return str(self.stack1)
