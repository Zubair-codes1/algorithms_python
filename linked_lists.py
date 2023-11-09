"""
When modifying/inserting something into an array/list the memory
allocated to that area changes. Sometimes one array can be split into multiple
areas of the memory. Linked lists have a pointer to the next element in the linked
list so that even if they are in different areas of the memory they can still be accessed
"""

# Each item in the list
class Node:
    def __init__(self, data=None, next_value=None):
        self.data = data
        self.next_value = next_value

    def __repr__(self):
        return self.data

# The actual linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # adds a node at the beginning of a list
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    # inserts something at the end of a linked list
    def insert_at_end(self, data):
        # inserts at front if linked list is None
        if self.head is None:
            self.head = Node(data, None)
            return

        # loops through linked list to get to the last value
        itr = self.head
        while itr.next_value:
            itr = itr.next_value

        # adds the value to the end of the list
        itr.next_value = Node(data, None)

    # Takes a list of value and inserts them at the start or
    # end of the list
    def insert_values(self, data_list, is_at_start=None):
        self.head = None
        for data in data_list:
            if is_at_start is not True:
                self.insert_at_end(data)
            else:
                self.insert_at_beginning(data)

    # returns a formatted version of the linked list
    def output(self):
        if self.head is None:
            print("Linked list has no items")
            return

        iterator = self.head
        linked_list_string = ""

        while iterator:
            linked_list_string += str(iterator.data) + "-->"
            iterator = iterator.next_value

        print(linked_list_string)

    # gets the length of the linked list by looping through it
    def get_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next_value

        return count

    # removes something at a certain valid index
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("This is not a valid index")

        if index == 0:
            self.head = self.head.next_value

        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                iterator.next_value = iterator.next_value.next_value
                break

            iterator = iterator.next_value
            count += 1

    # inserting data at a certain valid index
    def insert_at(self, index, data):
        # checks for errors
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        # while loop to find the index to insert the node at
        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                node = Node(data, iterator.next_value)
                iterator.next_value = node
                break

            iterator = iterator.next_value
            count += 1