#!/usr/bin/python

# Queue

class Queue:
    """
    First In First Out(FIFO) Object.
    """
    def __init__(self):
        self.__queue = []

    def push(self, data):
        """
        Adds an element to the queue
        """
        self.__queue.insert(0, data)

    def pop(self):
        """
        Removes the first element in the queue
        """
        if len(self.__queue) > 0:
            self.__queue.pop()

    def peek(self):
        """
        Shows the earliest element in the queue.
        """
        return self.__queue[-1] if len(self.__queue) > 0 else None

    def __repr__(self):
        return str(self.__queue)

