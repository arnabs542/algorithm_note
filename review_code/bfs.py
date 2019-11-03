# heap
# leet code 703. Kth Largest Element in a Stream
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        heapq.heapify(self.nums)
        while len(nums) > k:
            heapq.heappop(self.nums)
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        
        return self.nums[0]
        
        


# bfs 1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level order traversal
from collections import deque
from copy import copy
class Solution102(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        q = deque([])
        ret = []
        
        q.append(root)
        
        while q:
            # save the result to the ret
            temp = []
            temp_node = deque([]) # store next round node
            while q:
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    temp_node.append(node.left)
                if node.right:
                    temp_node.append(node.right)

            ret.append(temp)
            
            q = copy(temp_node)
        
        return ret
