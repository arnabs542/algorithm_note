class Solution1: # two sum
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            else:
                hashmap[target - nums[i]] = i

# why the below is quicker?
#         hashmap = {}
        
#         for i in range(len(nums)):
#             hashmap[nums[i]] = i
        
#         for i in range(len(nums)):
#             temp = target - nums[i]
#             if temp in hashmap:
#                 if hashmap[temp] != i:
#                     return i, hashmap[temp]
        
class Solution15: # three sum with hashset and hashmap
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        
        sorted_nums = sorted(nums)
        hashmap = {}
        ret = set()
        
        pnt = 0
        
        for i in range(1, len(sorted_nums) - 1):
            for j in range(i, len(sorted_nums)):
                if sorted_nums[j] in hashmap:
                    ret.add((sorted_nums[pnt], sorted_nums[hashmap[sorted_nums[j]]], sorted_nums[j]))
                else:
                    hashmap[0 - sorted_nums[pnt] - sorted_nums[j]] = j 
                
            pnt += 1
            hashmap = {}
        
        return list(ret)

class Solution15_2: # two pointer
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        
        ret = []
        
        for i in range(len(nums) - 2): # we will set i as the target, and do a two sum in the right hand side of the array
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]: # if the nums[i] == nums[i - 1], we will not set the target as a same number
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                temp_sum = nums[i] + nums[l] + nums[r]
            
                if temp_sum < 0:
                    l += 1
                elif temp_sum > 0:
                    r -= 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    while nums[r] == nums[r - 1] and l < r: # if the the nums[l] or nums[r] is equal its +1, -1 obejct, we will move to a different number to avoid duplicates
                        r -= 1
                    while nums[l] == nums[l + 1] and l < r:
                        l += 1
                    l += 1
                    r -= 1
        return ret

S=Solution15_2()
print(S.threeSum([-1,0,1,2,-1,-4]))

class Solution16: # three cloest
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        global_cloest = float('inf')
        global_diff = float('inf')
        
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > target:
                    if abs(total - target) < global_diff:
                        global_diff = abs(total - target)
                        global_cloest = total
                    r -= 1
                elif total < target:
                    if abs(total - target) < global_diff:
                        global_diff = abs(total - target)
                        global_cloest = total
                    l += 1
                else:
                    return target
        return global_cloest

class Solution1089: # two pointers
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_counter = arr.count(0)
        slow, fast = len(arr) - 1, 0
        length = len(arr)
        
        for i in range(zero_counter):
            arr.append(0)
            
        fast = len(arr) - 1
        
        while zero_counter >= 0 and slow >= 0:
            if arr[slow] == 0:
                zero_counter -= 1
                arr[fast] = 0
                arr[fast - 1] = 0
                fast -= 1
                arr.pop()
            else:
                arr[fast] = arr[slow]
            
            fast -= 1
            slow -= 1
        return

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1 -> 2 -> 3 -> 4 -> 5    n = 2
#                     p    n = 2
#                p         n = 1
#           p              n = 0    delete 3.next:  3.next = 3.next.next

class Solution19:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or head.next == None:
            return None
        
        n = self.helper(head, n)
        
        if n == 0:
            head = head.next
        
        return head
        
    def helper(self, head, n):    
        if head == None:
            return n
        
        n = self.helper(head.next, n) 
        
        if n == 0:
            head.next = head.next.next
            
        return n - 1

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution160(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if headA == None or headB == None:
            return None
        
        self.node = None
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
    
        diff = abs(lenA - lenB)
        if lenA > lenB:
            while diff > 0:
                headA = headA.next
                diff -= 1
        else:
            while diff > 0:
                headB = headB.next
                diff -= 1
        
        ret = self.helper(headA, headB)
        return ret
        
    def getLength(self, head):
        l = 0
        while head != None:
            l += 1
            head = head.next
        return l
        
    def helper(self, headA, headB):
        while headA != None and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
            
        
        
            