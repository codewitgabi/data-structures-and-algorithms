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

    def index(self, data: int) -> int:
        iteration: int = 0

        while self is not None:
            if self.data != data:
                iteration += 1
                self = self.next
            else:
                return iteration

        return -1

    def remove(self, data: int):
        if self.data == data:
            pass

        # ? CASE: When the data to be removed is not the first element

        if self.next.data == data:
            self.next = self.next.next
        else:
            return self.next.remove(data)

    def __repr__(self):
        arr = []

        while self is not None:
            arr.append(self.data)
            self = self.next

        return f"<LinkedList {arr}>"

    def __str__(self) -> str:
        return self.__repr__()


advanced_instance = AdvancedLinkedList(3)
advanced_instance.insert(4)
advanced_instance.insert(8)
advanced_instance.insert(5)
advanced_instance.insert(7)
advanced_instance.insert(2)


# print(advanced_instance.data)
# print(advanced_instance.next.data)
# print(advanced_instance.next.next.data)
# print(advanced_instance.next.next.next.data)

advanced_instance.remove(2)
advanced_instance.remove(3)

print(advanced_instance)

# print(advanced_instance.index(3))
# print(advanced_instance.index(4))
# print(advanced_instance.index(8))
# print(advanced_instance.index(2))
# print(advanced_instance.index(0))
