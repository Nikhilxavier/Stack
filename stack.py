"""
Implementation of Stack.
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
