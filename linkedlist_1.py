#!/usr/bin/python

# Singly Linked List


class node:
	def __init__(self, data=None) -> None:
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self) -> None:
		self.head = node()
	
	def append(self, value) -> None:
		"""
		Adds a node to the end of the linked list object
		"""
		cur_node: node = self.head
		new_node: node = node(value)
		
		while cur_node.next is not None:
			cur_node = cur_node.next
		cur_node.next = new_node
	
	def prepend(self, value) -> None:
		"""
		Adds a node to be beginning of the linked list object
		"""
		new_node: node = node(value)
		new_node.next = self.head
		self.head = new_node
	
	def display(self) -> str:
		"""
		Returns a str object representing the linked list
		"""
		cur_node: node = self.head
		pack: list = []
		
		while cur_node is not None:
			if cur_node.data is not None:
				pack.append(cur_node.data)
			cur_node = cur_node.next
			
		return " ==> ".join(str(data) for data in pack)
	
	def length(self) -> int:
		"""
		Returns the length of the linked list
		"""
		cur_node: node = self.head
		count: int = 0
		
		while cur_node.next is not None:
			count += 1
			cur_node = cur_node.next
			
		return count
	
	def insert(self, value, index) -> None:
		"""
		Inserts a new node with the given value at the specified index in the linked list
		"""
		if index < 0: return
		
		new_node: node = node(value)

		if index == 0:
			new_node.next = self.head
			self.head = new_node
		else:
			cur_node = self.head
			prev_node = None
			count = 0
			
			while count < index and cur_node is not None:
				prev_node = cur_node
				cur_node = cur_node.next
				count += 1
			
			if cur_node is None and count < index: return
			new_node.next = cur_node
			prev_node.next = new_node
	
	def remove(self) -> None:
		"""
		Deletes the last data from the linked list
		"""
		cur_node = self.head
		
		if self.length() == 0: return
		cur_node = self.head
		idx = 0
		
		while True:
			last_node = cur_node
			cur_node = cur_node.next
			if idx == self.length() - 1:
				last_node.next = cur_node.next
				return
			idx += 1
	
