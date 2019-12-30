# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# reverse linked list
# leet code 206

# reverse part of the list
# leet code 92
# iterate
class Solution92:
    def reverseBetween_iterate(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        
        # _  _  m  _  _  n  _  _
        #    b  s        h  a
        # b: before
        # s: start
        # h: head
        # a: after
        
        dummy = ListNode(None)
        dummy.next = head
        before = dummy
        idx = 1
        
        while head != None:
            if idx == m:
                break
                
            before = head
            head = head.next
            idx += 1
        
        # start node in the reverse part
        start = head
        
        while head != None:
            if idx == n:
                break
            
            head = head.next
            idx += 1
        
        # because n <= length of list, thus, head must not be None
        after = head.next
        
        ptn = start
        prev = None
        
        while ptn != after:
            temp = ptn
            ptn = ptn.next
            temp.next = prev
            prev = temp
        
        before.next = head
        start.next = after
        
        return dummy.next

# try recursive version


# middle node of linked list
# leetcode 876

# if has cycle in list
# leetcode 141: the key point is to judge whether we have revisted the node
# use hashset
class Solution141_set:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        
        hashset = set()
        
        while head != None:
            if head in hashset:
                return True
            hashset.add(head)
            head = head.next
        
        return False
        
# use two pointers
class Solution141_two_pointers:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        
        slow = head
        fast = head.next
        
        while fast != None and fast.next != None:
            if fast == slow or fast.next == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False
            

# insert in a sorted linked list
# laicode 39
class Solution_l39(object):
  def insert(self, head, value):
    """
    input: ListNode head, int value
    return: ListNode
    """
    if head == None:
      return ListNode(value)

    # write your solution here
    prev = None
    dummy = head
    while head != None and head.val < value:
      prev = head
      head = head.next
    
    newNode = ListNode(value)

    # if insert to the last place, head == None
    if head:
      newNode.next = head
  
    # if insert in the 1st place, prev == None, so we will return the new node
    if prev:
      prev.next = newNode
    else:
      return newNode

    return dummy

# merge two sorted list
# leetcode 21
# iterative 
class Solution21:
    def mergeTwoLists_iterate(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1
        
        # create new list
        dummy = ListNode(None)
        
        head = dummy
        
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    head.next = l1
                    head = head.next
                    l1 = l1.next
                else:
                    head.next = l2
                    head = head.next
                    l2 = l2.next
            elif l1:
                head.next = l1
                head = head.next
                l1 = l1.next
            elif l2:
                head.next = l2
                head = head.next
                l2 = l2.next
        
        return dummy.next

# recursiveclass Solution:
    def mergeTwoLists_rec(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def helper(l1, l2, head):
            # base case
            if not l1 and not l2: return
            
            # recursive rule
            if l1 and l2:
                if l1.val <= l2.val:
                    head.next = l1
                    helper(l1.next, l2, head.next)
                else:
                    head.next = l2
                    helper(l1, l2.next, head.next)
            elif l1:
                head.next = l1
                helper(l1.next, l2, head.next)
            elif l2:
                head.next = l2
                helper(l1, l2.next, head.next)
            
            return 
        
        dummy = ListNode(None)
        head = dummy
        helper(l1, l2, head)
        return dummy.next

    def mergeTwoLists_short_rec(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def helper(l1, l2):
            # base case
            if not l1:
                return l2
            if not l2:
                return l1
            
            # recursive wule
            # each time move forward with the smaller element's list, and each level return current level node
            if l1.val <= l2.val:
                l1.next = helper(l1.next, l2)
                return l1
            else:
                l2.next = helper(l1, l2.next)
                return l2
            
        return helper(l1, l2)

# leet code 138 copy linked list with random pointer
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
# what's the diff between my version and laioffer's version?
# laioffer's version's curr pointer is already exsited (copied in the previous loop), so no need to do the first copy in my version, thus, only need to copy the next and random pointer.
# my version copy the node in the current loop, so needs to clone three things, the node, its next, and its random
class Solution138:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        # hashmap to store the relationship between orignal and copied list
        hashmap = {None: None}
        
        # dummy node
        dummy = Node(None, None, None)
        
        new_head = dummy
        
        # loop through original linked list
        while head:
            # copy the node and val
            if head in hashmap:
                new_head.next = hashmap[head]
            else:
                new_head.next = Node(head.val, None, None)
                hashmap[head] = new_head.next
            
            new_head = new_head.next
            
            # copy next
            # if next is not none
            if head.next in hashmap:
                new_head.next = hashmap[head.next]
            else:
                new_head.next = Node(head.next.val, None, None)
                hashmap[head.next] = new_head.next
            
            # copy the random
            if head.random in hashmap:
                new_head.random = hashmap[head.random]
            else:
                new_head.random = Node(head.random.val, None, None)
                hashmap[head.random] = new_head.random
            
            head = head.next
        
        return dummy.next
                
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# merge k linked list
class Solution23:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists == None or len(lists) == 0:
            return None
            
        if len(lists) == 1:
            return lists[0]
        
        # 2n + 3n + 4n + kn = O(k^2 * n)
        # one by one O(k^2 * n)
        def solution1(lists):
            dummy = ListNode(None)
            dummy.next = lists[0]
            
            for i in range(1, len(lists)):
                head = dummy.next
                l1 = dummy.next
                l2 = lists[i]
                
                dummy.next = mergeTwoLists(l1, l2)
                
            return dummy.next
        
        def mergeTwoLists(l1, l2):
            dummy = ListNode(None)
            head = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    head.next = l1
                    head = head.next
                    l1 = l1.next
                else:
                    head.next = l2
                    head = head.next
                    l2 = l2.next
            
            if l1:
                head.next = l1
            
            if l2:
                head.next = l2
            
            return dummy.next
        
        # return solution1(lists)
        
        
        # solution2 binary reduction
        # k lists with each length is n
#         n_ 
#         n_|_
#         n_  |
#         n_|_|_
#         n_
#         n_|_
#         n_  |
#         n_|_|_
        
#         2k * n/2 + 4k * n/4 + 8k * n/8 = O(log(k) k n)
        def solution2(lists):
            # store each term binary reducted dummy nodes
            temp_lists = [ListNode(None) for i in range(len(lists) // 2)]
            
            while len(lists) > 1:
                if len(lists) % 2 != 0:
                    temp_lists.append(lists[-1])
                    
                    for i in range(len(temp_lists) - 1):
                        temp_lists[i] = mergeTwoLists(lists[2 * i], lists[2 * i + 1])
                else:
                    for i in range(len(temp_lists)):
                        temp_lists[i] = mergeTwoLists(lists[2 * i], lists[2 * i + 1])
                
                lists = temp_lists
                temp_lists = [ListNode(None) for i in range(len(lists) // 2)]
                
            return lists[0]
        
        # return solution2(lists)
        
        # import heapq
        from queue import PriorityQueue
        # each time find the smallest value in each list, and connect each other
        
        # use a min heap to keep track the second smallest pointer
        
        # we scan k * n points, and each time we perform k-sized heap related operation, so it's log(k)
        
        # so total time complexity: O(k * n * log(k))
        
#         not work # https://stackoverflow.com/questions/3954530/how-to-make-heapq-evaluate-the-heap-off-of-a-specific-attribute
#         def new_cmp_lt(self,a,b):
#             return a[0]<b[0]
        
#         heapq.cmp_lt=new_cmp_lt
        
        def solution3(lists: List[ListNode]) -> ListNode:
            root = ListNode(0)
            cur = root
            q = PriorityQueue()

            for node in lists:
                if node:
                    q.put((node.val,id(node), node))

            while q.qsize()>0:
                cur.next = q.get()[2]
                cur = cur.next
                if cur.next:
                    q.put((cur.next.val, id(cur.next), cur.next))

            return root.next

#         node could not be compared in python, below code will not work
#         def solution3(lists):
#             # initialize the heap
#             heap = PriorityQueue()
#             for i in range(len(lists)):
#                 if lists[i] != None:
#                     heap.put((lists[i].val, lists[i]))
        
#             dummy = ListNode(None)
#             ptn = dummy
            
#             while heap:
#                 # pop the smallest val
#                 temp = heap.get(heap)[1]
#                 # connect the correspond pointer
#                 ptn.next = temp
#                 ptn = ptn.next
                
#                 temp = temp.next
                
#                 if temp != None:
#                     heap.put((temp.val, temp))
                    
#             return dummy.next
            
        return solution3(lists)