class BinaryTree:
    __size: int = 0
    __total: int = 0
    __max: int = 0
    __height: int = 0

    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

        BinaryTree.__size += 1
        BinaryTree.__total += data

        if data > BinaryTree.__max:
            BinaryTree.__max = data

    def insert(self, data: int):
        if data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = BinaryTree(data)

    @property
    def length(self):
        return BinaryTree.__size

    @property
    def sum(self):
        return BinaryTree.__total

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()

        if self.right:
            self.right.inorder_traversal()
        print(self.data)

    @property
    def maximum(self):
        return BinaryTree.__max
    
    def print_less(self, value: int):
        if self.left:
            self.left.print_less(value)

        if self.right:
            self.right.print_less(value)

        # print the value if it's less than the given value

        if  self.data < value:
            print(self.data)

    def height(self):
        pass


bin_tree = BinaryTree(20)
bin_tree.insert(17)
bin_tree.insert(32)
bin_tree.insert(12)
bin_tree.insert(18)
bin_tree.insert(10)
bin_tree.insert(21)
bin_tree.insert(25)

bin_tree.inorder_traversal()