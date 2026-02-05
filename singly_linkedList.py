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

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# head1 = build_linked_list([1, 2, 3, 4, 5])
# middle1 = Solution().middleNode(head1)
# print_linked_list(middle1)

# head2 = build_linked_list([1, 2, 3, 4, 5, 6])
# middle2 = Solution().middleNode(head2)
# print_linked_list(middle2)


class Solution1:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 if list1 else list2
        
        return dummy.next
          
# head1 = build_linked_list([1,2,4]) 
# print_linked_list(head1)
# head2 = build_linked_list([1,3,4])
# print_linked_list(head2) 

# Solution1().mergeTwoLists(head1, head2)
# print_linked_list(head1)             


class Solution2:
    def deleteNode(self, head, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = head
        while cur.next:
          if cur.next.val == node.val:
            cur.next = cur.next.next
          cur = cur.next
          
node = ListNode(2)
head1 = build_linked_list([1,2,4]) 
print_linked_list(head1)
Solution2().deleteNode(head1, node)
print_linked_list(head1)