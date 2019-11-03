# 1. math problems
# power function https://leetcode.com/problems/powx-n/discuss/19544/5-different-choices-when-talk-with-interviewers
class Solution50:
    def myPow(self, x, n):
        
        if x == 0 and n <= 0:
            return -1
        
        if n < 0:
            return 1 / self.helper(x, -n)
        else:
            return self.helper(x, n)
        
    def helper(self, x, n):
        if n == 0:
            return 1
        
        # we partition the n into 2 part each time, so we have O(logn) complexity
        # we make the n/2 to int, and then judge whether it's odd or even
        half_result = self.helper(x, int(n/2))
        
        if n % 2 == 0: # if it's even, we directly return the half result square
            return half_result * half_result
        else: # if it's odd, we need to multiply additional x
            return half_result * half_result * x

# 2. 2d array
# n queens
class Solution51: # O((n!)^2)
    def solveNQueens(self, n):
        # save each conditions when 1st queen in different columns
        positions = []
        # the result
        self.raw_ret = []
        # perform dfs
        self.helper(n, positions)
        # transfer the result
        print(self.raw_ret)
        self.transfer()
        
        return self.raw_ret
    
    def helper(self, n, positions):
        # base case when all the n queens positions have been set, we want to return and save the result 
        if len(positions) == n:
            self.raw_ret.append(positions.copy())
            return
        
        # recursion rule
        for i in range(n): # n is the number of columns in the board
            if self.check_nq(positions, i):
                positions.append(i)
                self.helper(n, positions)
                positions.pop()
            
        return
    
    def check_nq(self, positions, idx):
        invalid_set = set()
        for i in range(len(positions)):
            invalid_set.add(positions[i]) # check if in same col
            diff = len(positions) - i # think the current idx is on the len(positions)-th row, and the positions[i] is on i-th row, so we want the different
            invalid_set.add(positions[i] + diff) # right diagano
            invalid_set.add(positions[i] - diff) # left diagano
        if idx in invalid_set:
            return False
        
        return True
    
    def transfer(self):
        for pos_i in range(len(self.raw_ret)):
            positions = self.raw_ret[pos_i]
            
            for idx in range(len(positions)):
                stri = ''
                for i in range(positions[idx]): 
                    stri += '.'
                stri += 'Q'
                for i in range(positions[idx] + 1, len(positions)):
                    stri += '.'
                self.raw_ret[pos_i][idx] = stri
        return
                
        
        
#     recursion tree:
#         level: n, each represent the n-th queen
#                                     1st
#         /       /       /       /        \       \       \       \  save the 1st q's index in the positions list          n *  n
#        2nd     2nd
#      ///\\\   //|\\                                                 use positions to check whether the branch is valid
    
#      .....
        
class Solution51_q: # O(n!)
    def solveNQueens(self, n):
        # save each conditions when 1st queen in different columns
        positions = []
        # the result
        self.raw_ret = []
        # perform dfs
        self.helper(n, positions)
        # transfer the result
        print(self.raw_ret)
        self.transfer()
        
        return self.raw_ret
    
    def helper(self, n, positions):
        # base case when all the n queens positions have been set, we want to return and save the result 
        if len(positions) == n:
            self.raw_ret.append(positions.copy())
            return
        
        # recursion rule
        invalid_set = set()
        for i in range(len(positions)):
            invalid_set.add(positions[i]) # check if in same col
            diff = len(positions) - i # think the current idx is on the len(positions)-th row, and the positions[i] is on i-th row, so we want the different
            invalid_set.add(positions[i] + diff) # right diagano
            invalid_set.add(positions[i] - diff) # left diagano
            
        for i in range(n): # n is the number of columns in the board
            if i not in invalid_set:
                positions.append(i)
                self.helper(n, positions)
                positions.pop()
            
        return
    
    def transfer(self):
        for pos_i in range(len(self.raw_ret)):
            positions = self.raw_ret[pos_i]
            
            for idx in range(len(positions)):
                stri = ''
                for i in range(positions[idx]): 
                    stri += '.'
                stri += 'Q'
                for i in range(positions[idx] + 1, len(positions)):
                    stri += '.'
                self.raw_ret[pos_i][idx] = stri
        return

# spiral print similar (m * n)
class Solution54:
    def spiralOrder(self, matrix):
        if matrix == None or matrix == []:
            return []
        
        self.ret = []
        self.m = len(matrix) # row index
        self.n = len(matrix[0]) # col index
        
        self.helper(matrix, 0)
        
        return self.ret
        
    def helper(self, matrix, level):
        # base 0
        if level >= int(self.m / 2) or level >= int(self.n / 2):
            if self.m == self.n:
                if self.m % 2 == 0:
                    return
                self.ret.append(matrix[level][level])
                return

            # base 1, only part of row left
            if self.m < self.n:
                if self.m % 2 == 0:
                    return
                for col_id in range(level, self.n - level):
                    self.ret.append(matrix[level][col_id])
                return

            # base 2, only part of col left
            if self.m > self.n:
                if self.n % 2 == 0:
                    return
                for row_id in range(level, self.m - level):
                    self.ret.append(matrix[row_id][level])
                return
            
        # recursive rule    
        # append right
        for col_id in range(level, self.n - 1 - level):
            self.ret.append(matrix[level][col_id])
        
        # append down
        for row_id in range(level, self.m - 1 - level):
            self.ret.append(matrix[row_id][self.n - 1 - level])
        
        # append left
        for col_id in range(self.n - 1 - level, level, -1):
            self.ret.append(matrix[self.m - 1 - level][col_id])
        
        # append up
        for row_id in range(self.m - 1 - level, level, -1 ):
            self.ret.append(matrix[row_id][level])
        
        self.helper(matrix, level + 1)
        
        return

# 3. linked list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# reverse linked list
class Solution206:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        return self.reverse_helper(head)
        
    def reverse_helper(self, head):
        # base rule
        if head.next == None:
            return head
        
        # recursive rule
        temp = head.next
        new_head = self.reverse_helper(head.next)
        head.next = None
        temp.next = head
        
        return new_head

# Reverse Nodes in k-Group
class Solution25: 
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head
        
        self.length = self.get_length(head, 0)
        
        new_head = self.reverse_connect_k(head, 0, k)
        
        return new_head
    
    # connect each reversed linked list
    def reverse_connect_k(self, head, total, k): # total nodes we will handle
        # base case, if total >= the last k multiple
        if total > self.length - k:
            return head
        
        # recursive rult
        input_head = head
        for i in range(k):
            input_head = input_head.next
        
        # head is the old head
        connect_head = self.reverse_connect_k(input_head, total + k, k) # in graph is the part after the reversed part, in time is previous reversed list
        
        # reversed part's new head
        new_head = self.reverse_helper(head, k)
        head.next = connect_head
        
        #    ... -> new_head -> head -> connect_head -> ...
        
        return new_head
              
    # reverse k linked list
    def reverse_helper(self, head, counter): # counter starts at k
        if counter == 1:
            return head
        
        temp = head.next
        new_head = self.reverse_helper(head.next, counter - 1)
        temp.next = head
        head.next = None
        
        return new_head
        
    def get_length(self, head, length):
        if head.next == None:
            return length + 1
        
        length = self.get_length(head.next, length)
        
        return length + 1

node_list = []
for i in range(1,6):
    node_list.append(ListNode(i))
for i in range(len(node_list) - 1):
    node_list[i].next = node_list[i + 1]
head = node_list[0]

def print_node_list(head):
    while head != None:
        print(head.val)
        head = head.next

S = Solution25()
# print(S.get_length(head, 0))
#print_node_list(S.reverse_helper(head, 2))

new_head = S.reverseKGroup(head,2)
print_node_list(new_head)

# 4. string

# 5. tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# laicode 646. Store Number Of Nodes In Left Subtree
class Solution646_laicode(object):
  def numNodesLeft(self, root):
    """
    :type root: TreeNode
    """ 
    if root == None:
      return

    self.getNumber(root)

    return

  def getNumber(self, root):
    if root == None:
      return 0
    
    totalLeft = self.getNumber(root.left)
    root.numNodesLeft = totalLeft
    totalRight = self.getNumber(root.right)

    return totalLeft + totalRight + 1

# LCA: lowest common ancestor
class Solution236:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        
        leftReturn = self.lowestCommonAncestor(root.left, p, q)
        
        rightReturn = self.lowestCommonAncestor(root.right, p, q)
        
        if leftReturn == None and rightReturn == None:
            return None
        elif leftReturn != None and rightReturn == None:
            return leftReturn
        elif leftReturn == None and rightReturn != None:
            return rightReturn
        else: #if leftReturn != None and rightReturn != None:
            return root

            