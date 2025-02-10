class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.parent: Node | None = None

    def insert(self, data):
        if not self.parent:
            self.parent = Node(data)

        else:
            self.__insert(self.parent, data)

    def __insert(self, node: Node | None, data):
        if not node:
            return Node(data)

        if data <= node.data:
            node.left = self.__insert(node.left, data)

        else:
            node.right = self.__insert(node.right, data)

        return node

    def inorder_traversal(self):
        self.__inorder_traversal(self.parent)

    def __inorder_traversal(self, node: Node | None):
        # base condition

        if not node:
            return

        self.__inorder_traversal(node.left)
        print(node.data)
        self.__inorder_traversal(node.right)

    def preorder_traversal(self):
        self.__preorder_traversal(self.parent)

    def __preorder_traversal(self, node: Node | None):
        # base condition

        if not node:
            return

        print(node.data)
        self.__preorder_traversal(node.left)
        self.__preorder_traversal(node.right)

    def postorder_traversal(self):
        self.__postorder_traversal(self.parent)

    def __postorder_traversal(self, node: Node | None):
        # base condition

        if not node:
            return

        self.__postorder_traversal(node.left)
        self.__postorder_traversal(node.right)
        print(node.data)

    def search(self, target):
        return self.__search(self.parent, target)

    def __search(self, node: Node | None, target):
        # base condition

        if not node:
            return

        elif node.data == target:
            return node

        elif target < node.data:
            return self.__search(node.left, target)

        else:
            return self.__search(node.right, target)

    def min(self):
        current_node = self.parent

        while current_node.left:
            current_node = current_node.left

        return current_node

    def max(self):
        current_node = self.parent

        while current_node.right:
            current_node = current_node.right

        return current_node


bst = BinarySearchTree()

bst.insert(30)
bst.insert(25)
bst.insert(14)
bst.insert(45)
bst.insert(91)
bst.insert(17)
bst.insert(10)
bst.insert(0)
bst.insert(7)
bst.insert(32)

# bst.inorder_traversal()
# bst.preorder_traversal()
# bst.postorder_traversal()

# print(bst.search(12))
# print(bst.search(10))

print(bst.min().data)
print(bst.max().data)

