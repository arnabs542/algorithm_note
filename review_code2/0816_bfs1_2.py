# graph and heap
import heapq

# leet code 378
# kth smallest in a sorted matrix
# use min heap 
class Solution378_min:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        priority_queue = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                priority_queue.append(matrix[i][j])
                
        heapq.heapify(priority_queue)
        
        while k > 1:
            k -= 1
            heapq.heappop(priority_queue)
        
        return heapq.heappop(priority_queue)
        
# use pesu-max heap
# set minus of the element, and keep a k sized, min heap 
class Solution378_max:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        priority_queue = []
        heapq.heapify(priority_queue)
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if len(priority_queue) >= k:
                    temp = heapq.heappop(priority_queue)
                    if temp < -matrix[i][j]:
                        heapq.heappush(priority_queue,-matrix[i][j])
                    else:
                        heapq.heappush(priority_queue,temp)
                else:
                    heapq.heappush(priority_queue,-matrix[i][j])

        return -heapq.heappop(priority_queue)

# kth smallest in binary search tree
# leetcode 230
# inorder traverse, and decrese k each time
class Solution230:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # flag to judge, whether we need to put back the root
        queue = [(root, True)]
        
        # restul
        res = 0
        
        while k > 0 and queue:
            temp = queue.pop()
            if temp[1]:
                if temp[0].right:
                    queue.append((temp[0].right, True))
                queue.append((temp[0], False))
                if temp[0].left:
                    queue.append((temp[0].left, True))
            else:
                k -= 1
                res = temp[0].val
        return res


# laicode 436
# find the kth largest in an unsorted array
# use quick partition
# same logic with the quick sort, in quick sort, we make sure the left hand side of pivot is smaller than pivot, and the right hand side is equal or larger than the pivot.
# so if the pivot is the (n - k)th index, we could make sure that this pivot is just the one we want to find
# time O(n) artomized, because if we the pivot is in the middle of the array each time, we will only cost log n times to find the kth largest,
#                              and each time ,we only move n/2, n/4, n/8 ,.... times, which will totally cost n.
#                              so te answer is O(log n + n) ~ O(n)
#      O(n^2) worst case       but if we always split at the 1st or last index, it could cost us n times to find the kth largest, 
#                              and each time, we could move n - 1, n - 2, n - 3, n - 4, ..... times, which will totally cost n^2 if we split n times.
# space O(1) we didn't use new data sturcture in the process
class Solution_lai436(object):
  def findKthLargest(self, nums, k):
    """
    input: int[] nums, int k
    return: int
    """
    # write your solution here
    # quick partition

    # k = 4 k_id =(6 - 4) = 2

    # 3 2 1 5 6 4
    # p:5 l:3 r:4
    # p_id = 3
    # 3 2 1 4 6 5
      # 4 2 1 3 6 5
      # 4 3 1 2 6 5
      # 4 3 2 1 6 5
      # 4 3 2 1 5 6
    # k_id < p_id
    # 3 2 1 (4 6 5)
    # p:2 l:3 r:1
    # p_id = 1
    # 1 2 3

    # k_id > p_id
    # (1) 2 3 (4 6 5)
    # p:3 l:2 r:3
    # p_2

    # k_id == p_id
    # return nums[p_id]

    K_ID = len(nums) - k
    # k = 4
    #               2
    # 3 2 1 4 5 6
    #       r l
    #         m

    def partition(nums, left, right):
      i, j = left, right
      p = int((left + right + 1) / 2)
      nums[p], nums[j] = nums[j], nums[p]

      while i <= j:
        if nums[j] < nums[right]:
          nums[i], nums[j] = nums[j], nums[i]
          i += 1
        else:
          j -= 1
      nums[i], nums[right] = nums[right], nums[i]
      return i

    def helper(nums, left, right):
      # base 
      if left >= right:
        return 

      # find the partition index of the array
      mid = partition(nums, left, right)

      if mid == K_ID:
        return
      elif mid < K_ID:
        helper(nums, mid + 1, right)
      else: # mid > K_ID
        helper(nums, left, mid - 1)

      return
    
    helper(nums, 0, len(nums) - 1)
    return nums[K_ID]

# breath first search
from collections import deque
# level order traversal


# zigzag order traversal
# leetcode 103
# use deque, and keep track of the level 
# trick part, when we generate new node in the even level, we need to consider
# because each odd level, we pop from left, and append from right, 
# so in order to correspond that, we need to pop from right (just act like stack, FILO), and append from left
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        RET = []
        def bfs(root):
            if root == None:
                return RET
            
            lev = 1
            
            # initial
            queue = deque([root])
            while queue:
                length = len(queue)
                temp_ret = []
                
                for i in range(length):
                    # expand
                    if lev % 2 == 0:
                        temp = queue.pop()
                        temp_ret.append(temp.val)
                        if temp.right:
                            queue.appendleft(temp.right)
                        if temp.left:
                            queue.appendleft(temp.left)
                    else:
                        temp = queue.popleft()
                        temp_ret.append(temp.val)
                        if temp.left:
                            queue.append(temp.left)
                        if temp.right:
                            queue.append(temp.right)
                        
                RET.append(temp_ret)
                lev += 1
                
            return RET
        
        return bfs(root)

# leetcode 1161
# same with level order traversal
# just keep two variable for the max val and max level
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        def bfs(root):
            MAX_VAL = -float("inf")
            MAX_LEV = 0
        
            queue = deque([root])
            
            lev = 1
            
            while queue:
                length = len(queue)
                temp_sum = 0

                for i in range(length):
                    # expand
                    temp = queue.popleft()
                    temp_sum += temp.val

                    # generate
                    if temp.left:
                        queue.append(temp.left)
                    if temp.right:
                        queue.append(temp.right)

                if temp_sum > MAX_VAL:
                    MAX_VAL = temp_sum
                    MAX_LEV = lev
                    
                lev += 1
            return MAX_LEV
    
        return bfs(root)

# leetcode 662
# utilized the heap properties of the position index: for nth node, node.left.index = 2 * n, node.right.index = 2 * n + 1
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # want to maintain a tuple include another position index for each node, the first root node will be 1 (using the property of heap tree)
        
        def bfs(root):
            max_width = 1
            
            if root == None:
                return max_width
            
            queue = deque([(root, 1)])
            
            while queue:
                length = len(queue)
                level_list = []
                
                for i in range(length):
                    temp = queue.popleft()
                    level_list.append(temp[1])
                    
                    if temp[0].left:
                        queue.append((temp[0].left, temp[1] * 2))
                        
                    if temp[0].right:
                        queue.append((temp[0].right, temp[1] * 2 + 1))
                
                if len(level_list) > 1:
                    max_width = max(max_width, level_list[-1] - level_list[0] + 1)
            
            return max_width
        
        return bfs(root)

# leet code 958
# is complete tree?
# also utilize the index property for heap
# we just care about the total number of the node we have, and compare with the position index.
class Solution958:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # utilize the position
        # initial state
        queue = deque([(root, 1)])
        counter = 0
        last_id = 0
        
        while queue:
            for i in range(len(queue)):
                temp = queue.popleft()
                counter += 1
                
                last_id = temp[1]
                
                if temp[0].left:
                    queue.append((temp[0].left, 2 * temp[1]))
                    
                if temp[0].right:
                    queue.append((temp[0].right, 2 * temp[1] + 1))
            
        if counter != last_id:
            return False
        

# is bipartie
# we maintaince a hashtable to keep track whether the graph is valid.
# we will try to find the contradiction of the property of bipartie
# in order to do this, we will set two colors (red, blud) for the node, and each time, we just check whether the color are same or not
# hash table will include the index of the node, and also the color of the node.
# e.g. we start with the 1st node with red color, so we will generate its neibour, and set them to blue.
#      next, we will perform the same operation on the neibours, and each neibours will generate its own neibour, and set them to red (contradict to blue)
#      we check the neibour, if the neibour has appered before, the color should be same, otherwise it will bread the rule, and return false
#                            if it's a new node, we will just set it to red in the dictionary, and add it to the queue, and continue
#      if the graph pass all node, we return true
#  for
#  time = O(v + e) ??? if the graph is just has one piece, I think is just O(e), if not ,we need to scan every node, it costs O(v + e)
#  space = O(v) the complexity is the number of nodes
#  
class Solution785:
    def isBipartite(self, graph: List[List[int]]) -> bool:
#         0      red 
#        / \
#       1   3    blue
#      /\   /\
#     0  2 0  2  red
      
#            0          red
#       /    |   \
#      1     2     3    blue
#     /\   / | \   /\
#    0  2 0  1  3 0  2  red   2 has already been blue, so we return false
        def bfs(graph):
        # h:    0:t 1:f 2:f 3:f
        # s:    0, 1, 2, 3
        # q:    2, 3
            hash_table = {0: True}
            for node in range(len(graph)):
                if node not in hash_table:
                    hash_table[node] = True
                
                queue = deque([node])

                while queue:
                    # expand
                    temp = queue.popleft()

                    curr_col = hash_table[temp]

                    for nei in graph[temp]:
                        if nei in hash_table:
                            if hash_table[nei] == curr_col:
                                return False

                        else: # neibour not in the hashtable
                            hash_table[nei] = not curr_col
                            # generate
                            queue.append(nei)
                    
            return True
        
        return bfs(graph)

# leetcode 547
# friend circle
# we consider the students as the graph, we need to search, not the relationship matrix.
# we will loop through the graph
# and in the bfs, we will initial, and generate new node(student) based on the condition in the relationship matrix, and the visited_graph(students), and we also update the graph, and queue each time
# and each time, we will expand one student.

class Solution547:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)

        def bfs(M):
            students = [False for i in range(N)]
            counter = 0
            
            for i in range(N):
                queue = deque([])
                if students[i] == False:
                    # initial
                    counter += 1
                    queue.append(i)
                    students[i] = True
                
                while queue:
                    # expand
                    temp = queue.popleft()
                    
                    # generate
                    for j in range(N):
                        if M[temp][j] == 1 and students[j] == False:
                            queue.append(j)
                            students[j] = True
                    
            return counter
        
        return bfs(M)

# leetcode 127 
# word ladder
#    
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
#            hit
#          /     
#         hot                       dict {hot: 1, dot: 2, log:3}
#         /   
#          dot  
#       /   |   \
#      dog  hot   lot
#    /  |  \   
#   log cog dot  
# dog
# curr_distance: 4
# queue: lot log cog
# dict:  hit:0  hot:1  dot:2 dog:3 lot:3 log:4 cog:4

        def bfs(beginWord, endWord, wordList):
            queue = deque([(beginWord)])
            hashset = set(beginWord)
            wordList = set(wordList)
            distance = 1
            
            while queue:
                length = len(queue)
                for i in range(length):
                    temp = queue.popleft()
                    if temp == endWord:
                        return distance

                    # check if there is any one diff word
                    for i in range(len(temp)):
                        for j in "abcdefghijklmnopqrstuvwxyz":
                            word = temp[:i] + j + temp[i+1:]

                            if word in wordList and word not in hashset:
                                queue.append(word)
                                hashset.add(word)
                
                distance += 1
                            
            return 0

        return bfs(beginWord, endWord, wordList)