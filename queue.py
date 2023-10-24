"""
Items are added at the end of the list
Items are removed from the beginning
Works like a first come, first served system
"""
class Queue:
    def __init__(self, arr, limit=None):
        self.arr = arr
        self.limit = limit

    # adding something to the end
    def add(self, item):
        if len(self.arr) >= self.limit:
            self.arr = self.arr[0:self.limit]
        else:
            self.arr += [item]

    # removing an item at start
    def remove(self):
        if self.limit <= len(self.arr):
            self.arr = self.arr[0: self.limit]
        if len(self.arr):
            self.arr = self.arr[1:len(self.arr)]
        else:
            print("Empty array")

"""
# example
queue = Queue([0, 1, 3, 4, 3, 2], 20)
queue.add(5)
queue.remove()
print(queue.arr)
"""


