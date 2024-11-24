"""
Author: Gabriel Michael Ojomakpene [codewitgabi]
Email: codewitgabi222@gmail.com
LINKED LIST:
"""

from typing import Union


class BasicLinkedList:
    """
    This basic linked list class gives the basics about what a singly linked list actually is.
    It explains how a node works and explains how it actually links to other nodes.

    BasicLinkedList():
        A linked list node. In a singly linked list, every node has its data and a pointer to other nodes.
        The default value of the node's next attribute is None due to the fact that the last item in the list points to nothing.
        Therefore if we have a node that points to nothing, it is the last node in the linked list.

        Parameters
        ----------
        data : int, optional
            The data of the node. The default is None.

        next : Union[BasicLinkedList, None], optional
            The next node in the linked list. The default is None.
    """

    def __init__(self, data: Union[int, None] = None) -> None:
        self.data = data
        self.next: Union[BasicLinkedList, None] = None


basic_instance = BasicLinkedList(4)
basic_instance.next = BasicLinkedList(5)
basic_instance.next.next = BasicLinkedList(1)

# print(basic_instance.data)
# print(basic_instance.next.data)
# print(basic_instance.next.next.data)


class AdvancedLinkedList:
    def __init__(self, data: Union[int, None]) -> None:
        self.data = data
        self.next = None

    def insert(self, data: int) -> None:
        if self.next is not None:
            self.next.insert(data)
        else:
            self.next = AdvancedLinkedList(data)

    def display(self):
        arr = []

        while self:
            print(self)
            arr.append(self.data)
            self = self.next

        print(f"<LinkedList {arr}>")

    def find(self, data: int) -> int:
        iteration: int = 0

        while self is not None:
            if self.data == data:
                return iteration
            iteration += 1
            self = self.next

        return -1

    def get_node(self, index: int):
        idx: int = 0

        while self:
            if index == idx:
                return self

            idx += 1
            self = self.next

    def remove(self, data: int):
        if self.data == data:
            pass

        # ? CASE: When the data to be removed is not the first element

        if self.next.data == data:
            self.next = self.next.next
        else:
            return self.next.remove(data)

    def length(self):
        count: int = 0

        while self:
            self = self.next
            count += 1

        return count

    def reverse(self):
        size: int = self.length()

        for i in range(size // 2):
            left: AdvancedLinkedList = self.get_node(i)
            right: AdvancedLinkedList = self.get_node(size - i - 1)
            temp = left.data

            left.data = right.data
            right.data = temp

    def insert_at(self, index: int, data: int):
        idx: int = 0

        while self.next:
            if index == idx:
                cur_node_data = self.data
                next_node = self.next

                self.data = data
                self.next = AdvancedLinkedList(cur_node_data)
                self.next.next = next_node

                return

            idx += 1
            self = self.next
        else:
            self.next = AdvancedLinkedList(data)

    def insert_at_beginning(self, data):
        cur_node_data = self.data
        cur_next_node = self.next
        self.data = data
        self.next = AdvancedLinkedList(cur_node_data)
        self.next.next = cur_next_node

    def insert_at_end(self, data):
        # go to the end of the list

        while self.next:
            self = self.next

        self.next = AdvancedLinkedList(data)

    def is_empty(self):
        return self is None

    def empty(self):
        self.next = None
        self = None

    def is_present(self, data):
        while self:
            if self.data == data:
                return "Found"
            self = self.next
        else:
            return "Not found"

    def empty(self):
        self.next = None
        self = None


ll = AdvancedLinkedList(6)
ll.insert(4)
ll.insert(0)
ll.insert(9)

ll.empty()

ll.display()


class DoublyLinkedList:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def append(self, value):
        if self.next is None:
            self.next = DoublyLinkedList(value)
            self.next.prev = self
        else:
            self.next.append(value)

    def prepend(self, value):
        cur_next_node = self.next
        new_node = DoublyLinkedList(self.data)
        new_node.next = cur_next_node
        self.data = value
        self.next = new_node

    def size(self):
        iteration: int = 0

        while self:
            iteration += 1
            self = self.next

        return iteration

    def find(self, value):
        """Returns first occurence of the value"""

        cur = self
        count: int = 0

        while cur.prev is not None:
            cur = cur.prev

        while cur is not None:
            if cur.data == value:
                return count

            count += 1
            cur = cur.next

        return -1

    def pop(self):
        # move to the beginning of the list

        while self.prev is not None:
            self = self.prev

        # move to the end and remove last element

        while self.next is not None:
            self = self.next

        if self.prev:
            self.prev.next = None
        else:
            # if node is the last node
            self.data = None
            self = None

    def remove(self, value):
        # go to beginning of linked list

        while self.prev is not None:
            self = self.prev

        # find if value matches node data

        while self is not None:
            if self.data == value:
                print("Found")
                if self.prev:
                    print(self.prev.data)
                    self.prev.next = self.next
                else:
                    self = None
            self = self.next

    def display(self) -> str:
        # go to beginning of list

        cur = self
        arr = []

        while cur.prev is not None:
            cur = cur.prev

        # move next till end of list

        while cur is not None:
            arr.append(cur.data)
            cur = cur.next

        print(f"<DoublyLinkedList {arr}>")

    def get_head_tail(self):
        head = self.data

        while self.next:
            self = self.next

        tail = self.data

        return head, tail

    def insert(self, index, data):
        idx: int = 0

        while self.next:
            if index == idx:
                cur_next_node = self.next
                cur_prev_node = self.prev

                new_node = AdvancedLinkedList(self.data)
                self.data = data

                # self.next

            idx += 1
            self = self.next


# ====================================
# Updated Linked List
# ====================================


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        right = "==>" if self.next else str(None)
        top = "|" + "=" * 5 + "|" + "=" * 5 + "|"
        center = f"|{self.data:^5}" + "|" + f"{right:^5}" + "|"
        bottom = "|" + "=" * 5 + "|" + "=" * 5 + "|"

        return f"{top}\n{center}\n{bottom}"


class UpdatedLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur_node = self.head
            new_node = Node(data)

            while cur_node.next:
                cur_node = cur_node.next

            cur_node.next = new_node

    def display(self):
        cur_node = self.head
        arr = []

        while cur_node:
            arr.append(cur_node.data)
            cur_node = cur_node.next

        print(arr)

    def insert_at_beginning(self, data):
        cur_node = self.head
        new_node = Node(data)

        self.head = new_node
        self.head.next = cur_node

    def search(self, data):
        idx = 0
        cur_node = self.head

        while cur_node:
            if cur_node.data == data:
                return idx
            idx += 1
            cur_node = cur_node.next

        return -1

    def length(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next

        return count

    def get_node(self, index):
        idx = 0
        cur_node = self.head

        while cur_node:
            if idx == index:
                return cur_node
            idx += 1
            cur_node = cur_node.next

        return None

    def remove(self, index):
        idx = 0
        cur_node = self.head

        while cur_node:
            if idx == index:
                prev_node = self.get_node(idx - 1)
                next_node = self.get_node(idx + 1)

                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = next_node

                return
            idx += 1
            cur_node = cur_node.next

        raise IndexError("Out of range")

    def empty(self):
        self.head = None

    def reverse(self):
        mid = self.length() // 2
        for i in range(mid):
            left = self.get_node(i)
            right = self.get_node(self.length() - 1 - i)
            prev_left_data = left.data

            left.data = right.data
            right.data = prev_left_data

    def swap_nodes(self):
        """
        Good morning! Here's your coding interview problem for today.

        This problem was asked by Google.

        Given the head of a singly linked list, swap every two nodes and return its head.

        For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
        """
        cur_node = self.head
        idx = 0

        while cur_node:
            if idx % 2 == 0:
                cur_node_data = cur_node.data
                next_node = cur_node.next

                cur_node.data = next_node.data
                next_node.data = cur_node_data

            idx += 1
            cur_node = cur_node.next

    def __repr__(self) -> str:
        pass
