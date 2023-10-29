"""
Holds nodes of given value
Each parent node has children nodes
if value of child is less than parent then child is on left side
Otherwise child is on the right side of parent
Can be very fast for searching
Faster than linear search most of the time
Can easily traverse the tree in multiple ways shown in the code
-- recursive approach --
"""

class BinaryTreeNode:
    # initialising the tree
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    # adding a value to the binary tree
    def add(self, value):
        # checks on which side to place the tree
        if self.value > value:
            if self.left is None:
                # makes that value a tree node by it self
                self.left = BinaryTreeNode(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                # makes that value a tree node by it self
                self.right = BinaryTreeNode(value)
            else:
                self.right.add(value)

    # inorder traversal
    # visits the most left node then goes from order based on value
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    # preorder traversal
    # visits all the left most nodes then right nodes
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    # postorder traversal
    # only prints when algorith has gone all the way to the end of the tree
    # again works from left to right
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)

    # finds a node in the binary tree based on value
    # recursion occurs based on whether the value you are looking for
    # is greater than, less than or equal to the current value at the tree
    def find(self, value):
        if self.value == value:
            print("Found")
        elif self.value <= value:
            if self.right:
                self.right.find(value)
            else:
                print("Not found")
        else:
            if self.left:
                self.left.find(value)
            else:
                print("Not found")
