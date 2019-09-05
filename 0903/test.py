# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printListNode(head):
    curr = head
    while curr != None:
        print(curr.val)
        curr = curr.next

# leet code 445
class Solution445:
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []
        dummy = ListNode(None) 
        pointer = dummy
        
        while l1 != None:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2 != None:
            stack2.append(l2.val)
            l2 = l2.next
        
        flag = False
        while len(stack1) != 0 and len(stack2) != 0:
            numSum = stack1.pop() + stack2.pop()
            numSum, flag, pointer = self.compute(numSum, flag, pointer)
            print(numSum)
        
        if len(stack2) == 0:
            while len(stack1) != 0:
                numSum = stack1.pop()
                numSum, flag, pointer = self.compute(numSum, flag, pointer)
                print(numSum)
        
        if len(stack1) == 0:
            while len(stack2) != 0:
                numSum = stack2.pop()
                numSum, flag, pointer = self.compute(numSum, flag, pointer)
                print(numSum)
        if flag:
            pointer.next = ListNode(1)
            pointer = pointer.next
        
        return self.reverseList(dummy.next)
        
    def compute(self, numSum, flag, pointer):
        if flag:
            numSum += 1
            flag = False
        if numSum >= 10:
            flag = True
            numSum -= 10
        pointer.next = ListNode(numSum)
        pointer = pointer.next
        return numSum, flag, pointer
    
    def reverseList(self, head):
        if head.next == None:
            return head
        
        curr = head
        newHead = self.reverseList(head.next)
        curr.next.next = curr
        curr.next = None
        
        return newHead
        
# leetcode 328
class Solution328:
    def oddEvenList(self, head):
        if head == None or head.next == None:
            return head
        
        odd = head
        evenHead = head.next
        even = evenHead
        
        while odd.next != None and even.next != None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            if even != None:
                even = even.next
            
        if even != None:
            even.next = None
        
        odd.next = evenHead
        
        return head
