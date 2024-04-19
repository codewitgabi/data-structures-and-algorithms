class BinarySearchTree:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data: int):
        if data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)

    def preorder_traversal(self):
        print(self.data)
        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()

    def find(self, data):
        if data < self.data:
            if self.left is None:
                return self.left
            else:
                return self.left.find(data)
        elif data > self.data:
            if self.right is None:
                return self.right
            else:
                return self.right.find(data)
        else:
            return True


tree = BinarySearchTree(5)
tree.insert(0)
tree.insert(1)
tree.insert(8)
tree.insert(3)
tree.insert(10)


tree.preorder_traversal()  # 5
print(tree.find(8))