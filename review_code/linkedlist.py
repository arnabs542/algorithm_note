# Q1 middle of the linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution876:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        fast = head
        slow = head
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
        

# Q4 merge two sorted linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1->2->4

# 1->3->4

# dummy -> 

class Solution21:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        ptn = dummy

        while l1 and l2 != None:
            if l1.val <= l2.val:
                ptn.next = l1
                l1 = l1.next
            else:
                ptn.next = l2
                l2 = l2.next
            ptn = ptn.next
        
        if l1 == None:
            while l2 != None:
                ptn.next = l2
                l2 = l2.next
                ptn = ptn.next
        
        if l2 == None:
            while l1 != None:
                ptn.next = l1
                l1 = l1.next
                ptn = ptn.next
        
        return dummy.next

# linked list Q5
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# ------
# 1 -> 3 <- 2 1.next = 3
# 1 -> 3    2 2.next = None
# 2 -> 1 -> 3 2.next = 1
# 2 -> 1 -> 3

# 1 -> 2   3 -> 4   5 -> 6
#                   ------
#                   None
#                   5.next = None
#                   6.next = 5
#                   6 -> 5 -> None
#                   return 6
#          ------   
#          6
#          3.next -> 6
#          4.next -> 3
#          4 -> 3 -> 6 -> 5 -> None
#          return 4
# ------  

# linked list Q6
class Solution24:
    def swapPairs(self, head: ListNode) -> ListNode:

        newhead = self.helper(head)
        
        return newhead
        
    def helper(self, head):
        if head == None or head.next == None:
            return head
        
        newhead = self.helper(head.next.next)
        temp = head.next
        head.next.next = head
        head.next = newhead
        
        return temp
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution86:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None:
            return head
        
        smalldummy = ListNode(None)
        smallhead = smalldummy
        largedummy = ListNode(None)
        largehead = largedummy
        
        while head != None:
            # temp = head.next
            # head.next = None
            if head.val < x:
                smallhead.next = head
                smallhead = smallhead.next
            else:
                largehead.next = head
                largehead = largehead.next
            # head = temp
            head = head.next
        
        largehead.next = None
        
        smallhead.next = largedummy.next
        
        return smalldummy.next

