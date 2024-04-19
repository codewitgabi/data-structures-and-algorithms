"""
BINARY SEARCH TREE:
    A binary tree in which for each node, all elements in its left subtree are less than the node,
    and all elements in its right subtree are greater than the node.
    
    Node Insertion:
        Nodes are inserted according to their values, maintaining the BST property.
    Application:
        Ideal for applications where efficient search, insertion, and deletion are required, such as in databases and dictionaries
"""

from typing import Union


# TEST_TREE = 5, 2, 5, 3, 8, 5, 9

class BasicBinarySearchTree:
    def __init__(self, data: Union[int, None]) -> None:
        self.data = data
        self.left = None
        self.right = None


tree = BasicBinarySearchTree(5)
tree.left = BasicBinarySearchTree(2)
tree.right = BasicBinarySearchTree(5)
tree.left.right = BasicBinarySearchTree(3)
tree.right.right = BasicBinarySearchTree(8)
tree.right.right.left = BasicBinarySearchTree(5)
tree.right.right.right = BasicBinarySearchTree(9)


# print(tree.data)
# print(tree.left.data)
# print(tree.right.data)
# print(tree.left.right.data)
# print(tree.right.right.data)
# print(tree.right.right.left.data)
# print(tree.right.right.right.data)


class AdvancedBinarySearchTree:
    def __init__(self, data: Union[int, None]) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data: int):
        # left branch base case

        if data < self.data:
            if self.left is None:
                self.left = AdvancedBinarySearchTree(data)
            else:
                self.left.insert(data)
        else:
            # right branch base case

            if self.right is None:
                self.right = AdvancedBinarySearchTree(data)
            else:
                self.right.insert(data)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)

        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.data)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()

        if self.right:
            self.right.postorder_traversal()
        print(self.data)

    def find(self, value: int) -> bool | None:
        if value < self.data:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        elif value > self.data:
            if self.right is None:
                return None
            else:
                return self.right.find(value)

        else:
            return True

    def delete(self, value: int):
        if value < self.data:
            if self.left is not None:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right is not None:
                self.right = self.right.delete(value)
        else:
            # Case 1: Node has no children
            if self.left is None and self.right is None:
                return None

            # Case 2: Node has only one child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # Case 3: Node has two children
            min_right = self.right.find_min()
            self.data = min_right.data
            self.right = self.right.delete(min_right.data)

        return self

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current


# advanced_tree = AdvancedBinarySearchTree(5)
# advanced_tree.insert(5)
# advanced_tree.insert(2)
# advanced_tree.insert(5)
# advanced_tree.insert(3)
# advanced_tree.insert(8)
# advanced_tree.insert(5)
# advanced_tree.insert(9)


# print(advanced_tree.data)
# print(advanced_tree.left.data)
# print(advanced_tree.right.data)
# print(advanced_tree.left.right.data)
# print(advanced_tree.right.right.data)
# print(advanced_tree.right.right.left.data)
# print(advanced_tree.right.right.right.data)

advanced_tree = AdvancedBinarySearchTree(10)
advanced_tree.insert(5)
advanced_tree.insert(4)
advanced_tree.insert(2)
advanced_tree.insert(1)
advanced_tree.insert(3)
advanced_tree.insert(22)
advanced_tree.insert(11)
advanced_tree.insert(12)

# print(advanced_tree.left.left.left.right.data)
# print(advanced_tree.right.left.right.data)
# advanced_tree.inorder_traversal()
# advanced_tree.preorder_traversal()

print(advanced_tree.find(1))
advanced_tree.delete(10)
advanced_tree.preorder_traversal()
