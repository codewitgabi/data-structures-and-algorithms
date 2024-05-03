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

        while self is not None:
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


class DoublyLinkedList:
    def __init__(self, data=None):
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
        if self.prev is None:
            self.prev = DoublyLinkedList(value)
            self.prev.next = self
        else:
            self.prev.prepend(value)

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

    def __repr__(self) -> str:
        # go to beginning of list

        cur = self
        arr = []

        while cur.prev is not None:
            cur = cur.prev

        # move next till end of list

        while cur is not None and cur.data is not None:
            arr.append(cur.data)
            cur = cur.next

        return f"<DoublyLinkedList {arr}>"

    def __str__(self) -> str:
        return self.__repr__()
