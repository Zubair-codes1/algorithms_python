"""
Works like a regular array
Items are added and removed from the end of list
"""
class Stack:
    # initialising
    def __init__(self, arr):
        self.arr = arr

    # adding
    def append(self, item):
        self.arr += [item]

    # removing
    def remove(self):
        self.arr = self.arr[0: len(self.arr) - 1]

