# 81 O(n)，较为复杂的方法，通过O（n）判断是否sorted，有更简单方法判断是否为sorted
class Solution81:
    def search(self, nums, target):
        if nums == None or len(nums) == 0:
            return False
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True
            if nums[mid] >= nums[left] and self.isInc(nums[left:mid+1]):
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1 
                else: 
                    left = mid + 1
            elif nums[right] >= nums[mid]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else: 
                    right = mid - 1
        return False
    
    def isInc(self, arr):
        if len(arr) == 1:
            return True
        for i in range(len(arr)-1):
            if arr[i] <= arr[i+1]:
                pass
            else:
                return False
        return True

# 153，最小值一定是pivot，所以每次binary search淘汰sorted过的部分（rotated array由sorted和unsorted两部分组成）
class Solution153:
    def findMin(self, nums):
        if len(nums) == 0:
            return None
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((left + right)/2)
            if nums[mid] < nums[left]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return nums[left]

# 154，153 的follow up，遇到重复时，将指针移动1（left+1 or right-1），但不要越界mid
class Solution154:
    def findMin(self, nums):
        if len(nums) == 0:
            return None
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((left + right)/2)
            if nums[left] == nums[mid] and left < mid:
                left += 1
                continue
            if nums[right] == nums[mid] and right > mid:
                right -= 1
                continue
            if nums[mid] < nums[left]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return nums[left]

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

# 206 reverse linkedlist
class Solution206_wrong: # dead loop, why, not change the head.next, the result will be 1 <-> 2 <- 3 <- 4 <- 5
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        curr = head.next         # the l1 node.next, will always point to the l2, not None !!!
        prev = head
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
head = l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
# printListNode(head)
#S = Solution206_wrong()
#newhead = S.reverseList(head)
#printListNode(newhead) # error will be here, infinite loop

class Solution206: # right modified anwser
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        curr = head.next
        prev = head
        prev.next = None # should add this line
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

class Solution206_rec_wrong: # not work, because didn't return a value after finish the each recersive function
    def reverseList(self, head):
        if head == None or head.next == None:
            print("base")
            return head
        temp = head.next
        print(head.val)
        head.next = None
        nextHead = self.reverseList(temp)
        print(nextHead)
        nextHead.next = head

# S = Solution206_rec_wrong()
# newhead = S.reverseList(head)
# printListNode(newhead) 

class Solution206_rec_modified: # still not work, because didn't save the head of the new linklist, the return value should be teh new head of the new linkedlist 
    def reverseList(self, head):
        if head == None or head.next == None:
            print("base")
            return head
        temp = head.next
        print(head.val)
        head.next = None
        nextHead = self.reverseList(temp)
        print(nextHead.val)
        nextHead.next = head
        return head
#S = Solution206_rec_modified()
#newhead = S.reverseList(head)
#printListNode(newhead) 

class Solution206_rec: # not work, because you didn't return a value after finish the base case iteration function
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        temp = head.next
        head.next = None
        nextHead = self.reverseList(temp)
        temp.next = head
        return nextHead # the return value should be the new head of the new list
# S = Solution206_rec()
# newhead = S.reverseList(head)
# printListNode(newhead) 

# 234, complicated methods, reuse other function
class Solution234:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        
        halfList = self.findMid(head)
        newList = self.reverseList(halfList)
        ret = self.isPalindromeHelper(head, newList)
        return ret
    
    def findMid(self, head) :
        f, s = head, head
        while f != None and f.next != None:
            f = f.next.next
            s = s.next
        return s
    
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return newHead
        
    def isPalindromeHelper(self, head, newList):
        while head != None and newList != None:
            if head.val != newList.val:
                return False
            head = head.next
            newList = newList.next
        return True

# 92 reverse linked list II
class Solution92_not_work: # still forget set the first node to None.
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None or head.next == None:
            return head
        # ---   -----    -----   =>  --- ----- -----
        #   1   2   3    4             1 3   2 4
        #   ------- ------
        # 1 2     3 4
        #----- -------
        #    1 2     3 4
        position = 1
        curr = head     
        prev = None #3
        startNode = None #2
        no1Node = None #1
        no4Node = None #4
        
        while position <= n: # when the position is 2. the 2 is still point to 3, which will generate a loop after the algorithm, need to set it to None
            no4Node = curr.next
            if position == m:
                startNode = curr
                no1Node = prev # add a set none here
            elif position > m:
                curr.next = prev
            prev = curr
            curr = no4Node
            position += 1
        if no1Node and no4Node:
            startNode.next = no4Node
            no1Node.next = prev
            return head
        elif no1Node == None and no4Node:
            startNode.next = no4Node
            return prev
        elif no1Node and no4Node == None:
            no1Node.next = prev
            return head
        else:
            return prev

class Solution92_worked: # use iteration one-pass
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None or head.next == None:
            return head
        # ---   -----    -----   =>  --- ----- -----
        #   1   2   3    4             1 3   2 4
        #   ------- ------
        # 1 2     3 4
        #----- -------
        #    1 2     3 4
        position = 1
        curr = head     
        prev = None #3
        startNode = None #2
        no1Node = None #1
        no4Node = None #4
        
        while position <= n:
            no4Node = curr.next
            if position == m:
                startNode = curr
                no1Node = prev
                curr.next = None # very important step
            elif position > m:
                curr.next = prev
            prev = curr
            curr = no4Node
            position += 1
        if no1Node and no4Node:
            startNode.next = no4Node
            no1Node.next = prev
            return head
        elif no1Node == None and no4Node:
            startNode.next = no4Node
            return prev
        elif no1Node and no4Node == None:
            no1Node.next = prev
            return head
        else:
            return prev
S = Solution92_worked()
newhead = S.reverseBetween(head,2,5)
printListNode(newhead) 