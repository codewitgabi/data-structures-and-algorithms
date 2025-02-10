#!/usr/bin/python

# Dequeue

from collections import deque

# Adding Elements

deq = deque()
deq.append(3)
deq.append(4)
deq.appendleft(2)
deq.appendleft(1)
deq.extend([5, 6, 7])
deq.extendleft([0, -1])
deq.insert(1, 12)

# Removing Elements

deq.remove(4)

# Showing Deque Ends

deq.pop()
deq.popleft()


