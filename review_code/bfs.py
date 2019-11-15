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

# is Bipartite     

# reference: https://leetcode.com/problems/is-graph-bipartite/discuss/119514/Python-3-BFS-DFS-solutions

# we could consider each node has a color (0,1), if one node neibour has the same color with itself, it is not a Bipartite

# we could consider the Bipartite as a kind of tree (n-ray), each time we will check whether every node is valid

# dfs: firstly check one node to its botton

# 0----1
# |    |
# |    |
# 3----2

# [[1,3], [0,2], [1,3], [0,2]]

# color = {...}

    # node 0                  0
    #                   /           \
    # node 1           1             3x
    #                 / \           
    #               0x   2             
    # node 2            / \          
    #                  1x  3                    every has color, so we need not to go to another level
    #                     / \
    # node 3             0x  2x
# class Solution785_dfs_rec(object):
#     def isBipartite(self, graph):
#         color = {}
#         if self.dfs(graph, 0, color):
#             return True
#         return False

#     def dfs(self, graph, node, color): # report flag and color, manipulate node
#         # base case
#         if node in color:
#             return 

class Solution785_dfs(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}

        for item in range(len(graph)):
            if item not in color:    # we need to check, because there might be multiple separate parts in the graph
                stack = [item]
                color[item] = 1      # we don't care the color of the start point of the separate part, because it must be separated with the part of graph we have searched before. 

                while stack:
                    node = stack.pop()
                    for nb in graph[node]:
                        if nb not in color:
                            color[nb] = -color[node]
                            stack.append(nb)
                        elif color[nb] == color[node]:
                            return False
        return True

# bfs:

# [[1,3], [0,2], [1,3], [0,2]]

# color = {...}

    # node 0                  0
    #                   /           \
    # node 1, 3        1             3
    #                 / \           / \
    #               0x   2         0x  2x         every has color, so we need not to go to another level
    # node 2            / \           / \
    #                  1x  3x        1x 3x
from collections import deque
class Solution785_bfs(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}
        
        for item in range(len(graph)):
            if item not in color:    # we need to check, because there might be multiple separate parts in the graph
                queue = deque([item])
                color[item] = 1      # we don't care the color of the start point of the separate part, because it must be separated with the part of graph we have searched before. 
                while queue:
                    node = queue.popleft()

                    for nb in graph[node]:
                        if nb not in color:
                            color[nb] = -color[node]
                            queue.append(nb)
                        elif color[nb] == color[node]:
                            return False
        
        return True      


# tree completeance

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution958(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return False
        
        queue = deque([root])
        node = root
        
        while True:
            node = queue.popleft()
            if node == None:
                break
            queue.append(node.left)
            queue.append(node.right)
        
        while queue:
            if queue.popleft():
                return False
        return True
            
# Best first search: bfs2
# leetcode 378. Kth Smallest Element in a Sorted Matrix
import heapq
class Solution378:
    def kthSmallest(self, matrix, k):
        counter = 0 # count the number of elements we pop out of the pqueue
        ret = 0
        
        # initial
        pqueue = [(matrix[0][0], (0, 0))]
        visited_set = set((0,0))
        heapq.heapify(pqueue)
        
        while counter < k:
            row, col = heapq.heappop(pqueue)[1]
            ret = matrix[row][col]
            counter += 1
            
            # generate
            if row + 1 < len(matrix) and (row + 1, col) not in visited_set:
                heapq.heappush(pqueue, (matrix[row + 1][col], (row + 1, col)))
                visited_set.add((row + 1, col))
            if col + 1 < len(matrix) and (row, col + 1) not in visited_set:
                heapq.heappush(pqueue, (matrix[row][col + 1], (row, col + 1)))
                visited_set.add((row, col + 1))
            
        return ret

#################################################
# BFS practiceX
#################################################
# 103. Binary Tree Zigzag Level Order Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution103(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        level = 1 # whether we store left to right
        ret = []
        
        # we maintain two data struc(two stacks)
        # a stack1 for print left ot right
        # a stack2 for print right to left
        # all the element pop from stack1, their childrens will be append to stack2 (left first, right last)
        # same with the elements pop from stack2, their childrens will be append to stack1 (right first, right last)
        # each round we only pop queue or stack until it is empty (first queue then stack)
        stack1 = [root]
        stack2 = []
        
        while stack1 or stack2:
            temp_ret = [] # store each level elements
            while stack1:
                # expand rule
                temp = stack1.pop()
                temp_ret.append(temp.val)
                # generate rule
                if temp.left:
                    stack2.append(temp.left)
                if temp.right:
                    stack2.append(temp.right)
            if len(temp_ret) > 0:
                ret.append(temp_ret)
            
            temp_ret = []
            while stack2:
                temp = stack2.pop()
                temp_ret.append(temp.val)
                if temp.right:
                    stack1.append(temp.right)
                if temp.left:
                    stack1.append(temp.left)
            if len(temp_ret) > 0:
                ret.append(temp_ret)
        
        return ret

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# use deque instead of two stacks
from collections import deque
class Solution103_dequeue(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        level = 1 # whether we store left to right
        ret = []
        
        # use deque instead of two data stuc
        deq = deque([root])
        
        while deq:
            temp_ret = [] # store each level elements
            count = 0 # number of node we have expanded
            size = len(deq) # current level nodes number
            
            while (count < size):
                if level % 2 == 1 and deq:
                    # expand rule
                    temp = deq.popleft()
                    temp_ret.append(temp.val)
                    # generate rule
                    if temp.left:
                        deq.append(temp.left)
                    if temp.right:
                        deq.append(temp.right)

                else: #if level % 2 == 0 and deq:
                    temp = deq.pop()
                    temp_ret.append(temp.val)
                    if temp.right:
                        deq.appendleft(temp.right)
                    if temp.left:
                        deq.appendleft(temp.left)
                
                count += 1
                
            ret.append(temp_ret)
            level += 1
        return ret

# bfs2
# find kth largest in array
# n + k log n
class Solution215(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # finding kth largest is equal to finding len(nums) + 1 - k th smallest
        # so we could use a heapq in python
        
        heapq.heapify(nums)
        
        nth = 1
        
        k = len(nums) + 1 - k
        
        while nth < k:
            heapq.heappop(nums)
            nth += 1
            
        return heapq.heappop(nums)  

# n log k
class Solution215_quicker(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # finding kth largest is equal to finding len(nums) + 1 - k th smallest
        # so we could use a heapq in python
        
        heap = []
        heapq.heapify(heap)
        
        for el in nums:
            if len(heap) < k:
                heapq.heappush(heap, el)
            else:
                heapq.heappush(heap, el)
                heapq.heappop(heap)
                
        return heapq.heappop(heap)

# laicode 27 Kth Smallest Sum In Two Sorted Arrays
import heapq
class Solution27(object):
  def kthSum(self, A, B, k):
    """
    input: int[] A, int[] B, int k
    return: int
    """
    # write your solution here
    ptn_a = 0
    ptn_b = 0
    count = 0
    visited_set = set()

    # a heap that contains (sum, (ptn_a, ptn_b))
    heap = [(A[ptn_a] + B[ptn_b], (ptn_a, ptn_b))]
    heapq.heapify(heap)
    visited_set.add((ptn_a, ptn_b))

    while count < k - 1:
      # expand 
      ptn_a, ptn_b = heapq.heappop(heap)[1]
      count += 1
      
      # generate 
      # similar with the 2d mtrix, but replace matrix[i][j] with A[ptn_a] + B[ptn_b]
      if ptn_a < len(A) - 1 and (ptn_a + 1, ptn_b) not in visited_set:
        heapq.heappush(heap, (A[ptn_a + 1] + B[ptn_b], (ptn_a + 1, ptn_b)))
        visited_set.add((ptn_a + 1, ptn_b))
      if ptn_b < len(B) - 1 and (ptn_a, ptn_b + 1) not in visited_set:
        heapq.heappush(heap, (A[ptn_a] + B[ptn_b + 1], (ptn_a, ptn_b + 1)))
        visited_set.add((ptn_a, ptn_b + 1))
      print(heap)
        
    return heapq.heappop(heap)

S = Solution27()
S.kthSum([1,3,5,8,9], [2,3,4,7], 20)  

# word ladder
# leet code 127
from collections import deque
class Solution127(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
                 #    hit
                 #     |  all possible words (must exist in the wordList, and not visited) that has one difference with 0 level's word
                 #    hot
                 #   /   \
                 # dot   lot all possible words (must exist in the wordList, and not visited) that has one difference with 1 level's word
                 #  |     |     
                 # dog   log all possible words (must exist in the wordList, and not visited) that has one difference with 2 level's word
                 #  |     |
                 # cog   cog all possible words (must exist in the wordList, and not visited) that has one difference with 3 level's word
                    
        # initial state: queue will store the current word and the current length of the transformation path
        queue = deque([(beginWord, 1)])
        wordList = set(wordList)
        visited = set(beginWord)
        
        while queue:
            # expand: queue will pop the first in word and its transformation path's length, add the word to the visited matrix
            currWord, length = queue.popleft()
            
            # generate: try every possible 'one letter different' word to the currWord. If it is inside the wordList and it has not been shown before, then we will add it toe the BFS queue
            for i in range(len(currWord)):
                for ch in 'abcdefghigklmnopqrstuvwxyz':
                    tempWord = currWord[:i] + ch + currWord[i + 1:]
                    if tempWord in wordList and tempWord not in visited:
                        queue.append((tempWord, length + 1))
                        visited.add(tempWord)
            
            # termination: if currWord is the endWord, it means we have found the shortest path
            if currWord == endWord:
                return length
            
        return 0

# WORD LADDER2, pure bfs, store paths instead of length
# we need to pop all element in queue in each level
# https://leetcode.wang/leetCode-126-Word-LadderII.html
from collections import deque
from copy import copy
class Solution126(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # same question with word ladder
        # in this case, we will maintain a data struc to track all possible answer
        # we will track the path rather than the length, the length is just the len(path)
        
        # initial state: queue will store the current word and the current length of the transformation path
        queue = deque([[beginWord]])
        
        wordList = set(wordList)
        visited = set(beginWord)
        ret = []
        global_min_length = float('inf')
        is_find = False
        
        while queue:
            num = len(queue)
            subvisited = set()
            
            ### must pop all paths in queue and add them in the subvisited
            # IN FACT, THIS IS RELATED TO OUR TERMINATION RULE, LIKE FIND KTH SMALLEST, WE ONLY POP K NUMBER; HERE, THE LAST ELEMENTS WE POP WILL BE THE LEVEL THAT HAS THE SMALLEST PATHS.
            for i in range(num):
                # expand: queue will pop the first in word and its transformation path's length, add the word to the visited matrix
                path = queue.popleft()
                currWord = path[-1]
                length = len(path)
            
                # termination: if currWord is the endWord, it means we have found the shortest path
                if currWord == endWord:
                    is_find = True
                    global_min_length = min(len(path), global_min_length)
                    ret.append(path)
                    # if we found the result, we will not generate the currWord
                    continue 
            
                # generate: try every possible 'one letter different' word to the currWord. If it is inside the wordList and it has not been shown before, then we will add it toe the BFS queue
                for i in range(len(currWord)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        tempWord = currWord[:i] + ch + currWord[i + 1:]
                        if tempWord in wordList and (tempWord not in visited):
                            path.append(tempWord)
                            queue.append(copy(path))
                            path.pop()
                            subvisited.add(tempWord)

            visited = visited.union(subvisited)
            if is_find:
                break
        return ret