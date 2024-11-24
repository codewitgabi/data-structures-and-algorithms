class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur_head = self.head
            self.head = Node(data)
            self.head.next = cur_head

    def pop(self):
        if not self.head:
            raise IndexError("Stack is empty, can't pop")
        else:
            self.head = self.head.next

    def display(self):
        arr = []
        cur_node = self.head

        while cur_node:
            arr.append(cur_node.data)
            cur_node = cur_node.next

        print(arr)


stack = Stack()
stack.push(5)
stack.push(4)
stack.push(1)

stack.pop()
stack.pop()

stack.display()
