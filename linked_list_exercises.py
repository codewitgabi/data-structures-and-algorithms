"""
Exception classes
"""

from typing import Self


class RotationError(Exception):
    def __init__(self, *args, **kwargs):
        super(RotationError, self).__init__(*args, **kwargs)


class DeletionError(Exception):
    def __init__(self, *args, **kwargs):
        super(DeletionError, self).__init__(*args, **kwargs)


class PopError(Exception):
    def __init__(self, *args, **kwargs):
        super(PopError, self).__init__(*args, **kwargs)


"""
End exception classes
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)

        else:
            cur_node = self.head

            while cur_node.next:
                cur_node = cur_node.next

            cur_node.next = Node(data)

    def length(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next

        return count

    def count(self, data):
        i = 0
        cur_node = self.head

        while cur_node:
            if cur_node.data == data:
                i += 1
            cur_node = cur_node.next

        return i

    def get_node(self, index):
        idx = 0
        cur_node = self.head

        while cur_node:
            if idx == index:
                return cur_node
            idx += 1
            cur_node = cur_node.next

        raise IndexError("Linked list out of range")

    @property
    def __middle(self):
        size = self.length()
        mid = size // 2 if size % 2 == 1 else size // 2

        return mid

    def middle(self):
        mid = self.__middle

        return self.get_node(mid).data

    def reverse(self):
        size = self.length()

        for i in range(0, size // 2):
            left = i
            right = size - i - 1

            left_node = self.get_node(left)
            right_node = self.get_node(right)
            left_data = left_node.data

            left_node.data = right_node.data
            right_node.data = left_data

    def rotate(self, k=0):
        i = 0

        if not self.head:
            raise RotationError("Cannot rotate an empty list")

        while i < k:
            next_node = self.head.next
            last_node = self.get_node(self.length() - 1)

            last_node.next = Node(self.head.data)

            self.head = next_node

            i += 1

    def nth_node_from_end(self, n):
        size = self.length()

        return self.get_node(size - n).data

    def convert_to_circular_linked_list(self):
        cur_node = self.head

        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = self.head

    def __delete(self, index):
        idx = 0
        cur_node = self.head

        if index == 0 and self.head:
            self.head = self.head.next
            return

        elif index == 0 and not self.head:
            raise DeletionError("No index found")

        while cur_node:
            if idx == index:
                prev_node = self.get_node(idx - 1)
                next_node = (
                    self.get_node(idx + 1) if idx < (self.length() - 1) else None
                )

                prev_node.next = next_node
                return

            idx += 1
            cur_node = cur_node.next

        raise IndexError("Linked list out of range")

    def delete_last_occurrence(self, data):
        last_occurrence = None
        idx = 0
        cur_node = self.head

        while cur_node:
            if cur_node.data == data:
                last_occurrence = idx
            cur_node = cur_node.next
            idx += 1

        # get nodes around the last_occurrence

        if isinstance(last_occurrence, int):
            self.__delete(last_occurrence)
        else:
            raise Exception("Could not find data")

    def delete_middle(self):
        middle = self.__middle

        self.__delete(middle)

    def __remove_duplicate(self, data):
        if self.count(data) == 1:
            return

        self.delete_last_occurrence(data)
        return self.__remove_duplicate(data)

    def remove_duplicate(self):
        cur_node = self.head
        idx = 0

        while cur_node:
            self.__remove_duplicate(cur_node.data)
            idx += 1
            cur_node = cur_node.next

    def delete_n_after_m(self, m, n):
        """
        args:
            m -> Number of nodes to keep
            n -> Number of nodes to delete.
        """

        step = m

        while step < self.length():
            for _ in range(0, n):
                self.__delete(step)
            step += m

    def detect_loop(self):
        cur_node = self.head

        while cur_node.next:
            if cur_node.next == self.head:
                return True
            cur_node = cur_node.next
        return False

    def alternate_merge(self, list1: Self, list2: Self):
        list1_length = list1.length()  # O(n)

        for i in range(list1_length):  # O(n)
            cur_node = list1.get_node(i + 2)
            cur_node_next = cur_node.next
            cur_node.next = list2.head
            list2.head = list2.head.next
            cur_node.next.next = cur_node_next

    def traverse_circular(self):
        cur_node = self.head
        arr = []

        while cur_node:
            arr.append(cur_node.data)
            if cur_node.next == self.head:
                break
            cur_node = cur_node.next

        print(" => ".join(list(map(str, arr))))

    def remove_kth_node(self, k):
        pass

    def __repr__(self):
        cur_node = self.head
        arr = []

        while cur_node:
            arr.append(cur_node.data)
            cur_node = cur_node.next

        return " => ".join(list(map(str, arr)))

    def __str__(self):
        return self.__repr__()


d = LinkedList()
d.insert(1)
d.insert(2)  # out 1
d.insert(3)
d.insert(4)  # out 2
d.insert(5)
d.insert(6)  # out 3


# d.convert_to_circular_linked_list()

# d.traverse_circular()


print(d)


class Stack:
    def __init__(self):
        self.head: Node | None = None

    def push(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            head = self.head
            self.head = Node(data)
            self.head.next = head

    def pop(self):
        if self.head:
            self.head = self.head.next

    def peek(self):
        if self.head:
            print(self.head.data)

    def __repr__(self) -> str:
        arr = []
        cur_node = self.head

        while cur_node:
            arr.append(cur_node.data)
            cur_node = cur_node.next

        return "<Stack " + " => ".join(list(map(str, arr))) + " />"


class Queue:
    def __init__(self):
        self.head: Node | None = None

    def enqueue(self, data):
        """
        Adds a node to the end of the queue
        """

        if not self.head:
            self.head = Node(data)
        else:
            head = self.head
            self.head = Node(data)
            self.head.next = head

    def dequeue(self):
        """
        Removes the top node from the queue
        """

        cur_node = self.head

        if self.head:
            if self.head.next is None:
                self.head = None
                return
        else:
            raise PopError("Queue is empty")
        
        while cur_node.next.next:
            cur_node = cur_node.next

        cur_node.next = None

    def peek(self):
        """
        Returns the next node in the queue.
        """

        cur_node = self.head

        while cur_node.next:
            cur_node = cur_node.next

        print(cur_node.data)

    def __repr__(self):
        arr = []
        cur_node = self.head

        while cur_node:
            arr.append(cur_node.data)
            cur_node = cur_node.next

        return "<Queue " + " => ".join(list(map(str, arr))) + " />"


def check_bracket(brackets: str) -> bool:
    """
    Checks if the brackets are balanced.
    """

    bracket_patterns = {"(": ")", "[": "]", "{": "}", "<": ">"}
    checker = []

    for bracket in brackets:
        if bracket in bracket_patterns.keys():
            checker.append(bracket)
        else:
            if len(checker) == 0:
                return False
            elif bracket == bracket_patterns[checker[-1]]:
                checker.pop()

    return len(checker) == 0


print(check_bracket("[[{}]()]"))


def forward_loop_recursion(n):
    if n == 0:
        return 0

    forward_loop_recursion(n - 1)
    print(n)


forward_loop_recursion(10)


def reverse_loop_recursion(n):
    if n == 0:
        return 0

    print(n)
    reverse_loop_recursion(n - 1)


reverse_loop_recursion(10)


def get_combinations(nums):
    def backtrack(start, path):
        if start == len(nums):
            return
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            combinations.append(list(path))
            backtrack(i + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations


nums = [1, 2, 3, 4]
all_combinations = get_combinations(nums)
print(all_combinations)

