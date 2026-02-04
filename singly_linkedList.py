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
    
    
    
linkedList = SinglyLinkedList()
linkedList.insertAtBeginning(4)
linkedList.insertAtBeginning(4)