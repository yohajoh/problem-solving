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
    
  def insertAtAny(self, pos, val):
    node = Node(val)
    if self.head is None:
      print('Error: The list is empty!!!')
      return
    
    if self.head.value == pos:
      node.next = self.head
      self.head = node
      return
    
    cur = self.head
    while cur.next is not None:
      if cur.next.value == pos:
        node.next = cur.next
        cur.next = node
        return
      cur = cur.next
    print("Error: The value is not present on the list!!!")
  
  def display(self):
    if self.head is None:
      return
    cur = self.head
    while cur is not None:
      print(cur.value, end=" --> ")
      cur = cur.next
    
# linkedList = SinglyLinkedList()
# linkedList.insertAtBeginning(4)
# linkedList.insertAtBeginning(5)
# linkedList.insertAtEnd(6)
# linkedList.insertAtEnd(1)
# linkedList.insertAtBeginning(9)
# linkedList.insertAtAny(6, 10)
# linkedList.insertAtAny(1, 20)
# linkedList.insertAtAny(23, 20)
# linkedList.display()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def print_linked_list(head):
    current = head
    result = []

    while current:
        result.append(current.val)
        current = current.next

    print(result)


head1 = build_linked_list([1, 2, 3, 4, 5])
middle1 = Solution().middleNode(head1)
print_linked_list(middle1)

head2 = build_linked_list([1, 2, 3, 4, 5, 6])
middle2 = Solution().middleNode(head2)
print_linked_list(middle2)
