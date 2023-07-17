from stack import Stack
from queue import Queue


def multi_bracket_validation(input):
    """
    Validate if brackets in input string are balanced.
    
    Args:
        input (str): The input string containing brackets.
    
    Returns:
        bool: True if the brackets are balanced, False otherwise.
    """
    stack = Stack()
    for char in input:
        if char in ['(', '[', '{']:
            stack.push(char)
        elif char in [')', ']', '}']:
            if stack.is_empty():
                return False
            if char == ')' and stack.peek() == '(':
                stack.pop()
            elif char == ']' and stack.peek() == '[':
                stack.pop()
            elif char == '}' and stack.peek() == '{':
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False
