class BinaryTree:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value: int):
        if value < self.data:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinaryTree(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinaryTree(value)

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


tree = BinaryTree(15)
tree.insert(12)
tree.insert(15)
tree.insert(10)
tree.insert(5)
tree.insert(9)

tree.inorder_traversal()
tree.preorder_traversal()
tree.postorder_traversal()
