class Node:
  def __init__(self, val):
    self.value = val
    self.next = None
    
class SinglyLinkedList:
  def __init__(self):
    self.head = None
    
  def insertAtBeginning(self, value):
    node = Node(value)
    
    if self.head is None:
      self.head = node
      return
    node.next = self.head
    self.head = node
    
  def insertAtEnd(self, value):
    node = Node(value)
    if self.head is node:
      self.head = node
    cur = self.head
    while cur.next is not None:
      cur = cur.next
    cur.next = node
  
  def display(self):
    if self.head is None:
      return
    cur = self.head
    while cur is not None:
      print(cur.value, end=" --> ")
      cur = cur.next
    
    
linkedList = SinglyLinkedList()
linkedList.insertAtBeginning(4)
linkedList.insertAtBeginning(5)
linkedList.insertAtEnd(6)
linkedList.insertAtEnd(1)
linkedList.insertAtBeginning(9)
linkedList.display()
