"""
Check if the string of parenthesis is balanced.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


class Stack:
    """Stack class with inbuilt functions."""

    def __init__(self):
        self.items = []

    def peek(self):
        return self.items[self.size()-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def balance_checker(string):
    """Check if the parentheses string is balanced.

    Returns boolean value based on the result
    """

    if len(string)%2 != 0:
        return False

    opening_par = set("({[")
    matching_par = set([("(", ")"), ("{", "}"), ("[", "]")])
    stack = Stack()

    for parentheses in string:
        if parentheses is in opening_par:
            stack.push(parentheses)
        else:
            if stack.is_empty():
                return False
            last_open_par = stack.pop()
            if (last_open_par, parentheses) not in matching_par:
                return False
    return not stack.is_empty()

