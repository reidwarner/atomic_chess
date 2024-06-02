class Node:
"""Class Represents a node in a link list"""
def __init__(self, data):
"""Constructor initializes two data members, one for data held in that node
and one that is a reference to the next node in the list."""
self.data = data
self.next = None
class LinkedList:
"""Class representing a linked list implementation of the List ADT."""
def __init__(self):
"""Head starts out equal to NONE when the linked list is empty."""
self._head = None
def get_head(self):
"""Methd for Getting first Node from list."""
return self._head
def rec_add(self, node, data):
"""Recursive add method which is a helper function that adds a new node
to the linked list at the end."""
if node.next is None: # if node is empty
node.next = Node(data)
else:
self.rec_add(node.next, data)
def add(self, val):
"""Adds a node containing val to the end of the linked list."""
if self._head is None: # if the list is empty
self._head = Node(val) # if empty, create a new node
else:
self.rec_add(self._head, val) # if not empty call rec_add
def rec_remove(self, prev_node, current_node, val):
"""Recursive remove method, which is a helper function that removes a node from the
linked list."""
if current_node is None:
return # if the list is empty
if current_node.data == val: # if the node to remove is the head
if prev_node is None:
self._head = current_node.next
else:
prev_node.next = current_node.next
else:
self.rec_remove(current_node, current_node.next, val)
def remove(self, val):
"""Removes the node containing val from the linked list."""
self.rec_remove(None, self._head, val)
def rec_contains(self, node, val):
"""Recursive method, which is a helper function that checks
if given node already exists in the linked list."""
if node is None: # if the list is empty
return False
if node.data == val: # if val found in any of the nodes
return True
return self.rec_contains(node.next, val)
def contains(self, val):
"""Method for Checking if linked list already contains node data."""
return self.rec_contains(self._head, val)
def rec_insert(self, prev_node, current_node, data, position):
"""Recursive inset method, which is a helper function that inserts new node
with the given data to its correct position."""
if position == 0: # if data is valid
new_node = Node(data)
if prev_node is None:
new_node.next = self._head
self._head = new_node # inserts new node at that position
else:
new_node.next = current_node # adjusts next data in line accordingly
prev_node.next = new_node
else:
if current_node is None:
raise IndexError("Index is out of range")
self.rec_insert(current_node, current_node.next, data, position - 1)
def insert(self, data, position):
"""Insert a new node with the given data at the specified position."""
if position < 0: # if negative, raise IndexError
raise IndexError("Index is out of range")
self.rec_insert(None, self._head, data, position)
def rec_reverse(self, prev_node, current_node):
"""Recursive reverse method that is a helper function that reverses linked list."""
if current_node is None:
self._head = prev_node
return
next_node = current_node.next
current_node.next = prev_node
self.rec_reverse(current_node, next_node)
def reverse(self):
"""Rearrange nodes to reverse the linked list."""
self.rec_reverse(None, self._head) # adjusts next pointers of each node to previous node
def rec_to_plain_list(self, node, result_list):
"""Recursive helper function that converts linked list to python list."""
if node is None: # initializes with empty list
return
result_list.append(node.data)
self.rec_to_plain_list(node.next, result_list)
def to_plain_list(self):
"""Recursive that returns regular python list that has same values in the same order."""
result_list = []
self.rec_to_plain_list(self._head, result_list) # calls rec_to_plain_list with head node to
start
return result_list

mylist = LinkedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
print(mylist.to_plain_list())
mylist.remove(4)
print(mylist.to_plain_list())
mylist.reverse()
print(mylist.to_plain_list())
mylist.insert(7,2)
print(mylist.to_plain_list())
print(mylist.contains(2))
print(mylist.contains(4))