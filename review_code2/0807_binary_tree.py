class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution94:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        RET = []
        
        def rec(root):
            # base case
            if root == None:
                return
            
            # recursive rule
            rec(root.left)
            RET.append(root.val)
            rec(root.right)
            
            return
        
        # rec(root)
        def ite1(root):
            stack = [root]
            hashset = set()
            
            while stack:
                root = stack.pop()
                if root in hashset:
                    RET.append(root.val)
                else:
                    if root:
                        hashset.add(root)
                        stack.append(root.right)
                        stack.append(root)
                        stack.append(root.left)
                            
            return
        
        ite1(root)
        
        return RET
    
    # other iterative solution
        def ite2(root): # in order traverse
            if root == None:
                return []
            
            # flag: whether we need to put back the node
            stack = [(root, True)]
            ret = []
            while stack:
                temp = stack.pop()
                
                if temp[1]:
                    if temp[0].right:
                        stack.append((temp[0].right, True))
    
                    stack.append((temp[0], False))
                    
                    if temp[0].left:
                        stack.append((temp[0].left, True))
                    
                else:
                    ret.append(temp[0].val)
                
            return ret
        
        return ite2(root)

class Solution145:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        RET = []
        
        def rec(root):
            if root == None:
                return
            
            rec(root.left)
            rec(root.right)
            RET.append(root.val)
            
            return 
        
        # rec(root)
        
        def ite(root):
            stack = [root]
            
            while stack:
                root = stack.pop()
                if root:
                    stack.append(root.left)
                    stack.append(root.right)
                    RET.append(root.val)
            
            left, right = 0, len(RET) - 1
            while left < right:
                RET[left], RET[right] = RET[right], RET[left]
                left += 1
                right -= 1
            
            return
        
        ite(root)
        
        return RET

class Solution144:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        RET = []
        
        def rec(root):
            # base case
            if root == None:
                return
            
            # recursive rule
            RET.append(root.val)
            rec(root.left)
            rec(root.right)
            
            return
    
        # rec(root)
        
        def ite(root):
            stack =[root]
            
            while stack:
                ptn = stack.pop()
                if ptn:
                    stack.append(ptn.right)
                    stack.append(ptn.left)
                    RET.append(ptn.val)
        
        ite(root)
        
        return RET

# balanced tree
# lc 110
class Solution110:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def helper(root):
            if root == None:
                return True
            
            if helper(root.left) and helper(root.right):
                left_height = getHeight(root.left, 0)
                right_height = getHeight(root.right, 0)

                if abs(left_height - right_height) <= 1:
                    return True
                else:
                    return False
            else:
                return False
            
            
        def getHeight(root, height):
            if root == None:
                return height
            
            left = getHeight(root.left, height) + 1
            right = getHeight(root.right, height) + 1
            
            return max(left, right)
        
        return helper(root)
        

# symmetric tree
# lc 101
class Solution101:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            
            if root1.val == root2.val:
                return helper(root1.left, root2.right) and helper(root1.right, root2.left)
            else:
                return False
        
        if root == None:
            return True
        
        return helper(root.left, root.right)

# same tree
# lc 100
class Solution100:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            
            if root1.val == root2.val:
                return helper(root1.left, root2.left) and helper(root1.right, root2.right)
            else:
                return False
        
        return helper(p, q)

# issutree
# lc 572
class Solution572:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        ### *** analysis not correct
#       use isSameTree function to every node
#            2
#        2       2
#       2  2    2  2
      
#       lev = log n
    
#                           node   *    each node's operation
#       log^n level: 2 ^ (log (n) - 1) * 2 ^ 0
#       log^n - 1 level: 2 ^ (log (n) - 2) * (2 ^ 1 + 2 ^ 0)
#       log^n - 2 level: 2 ^ (log (n) - 3) * (2 ^ 2 + 2 ^ 1 + 2 ^ 0)
#         ...
#       1 level        : 2^0 * n
#       n * n = n^2 * logn

#         get height of m, n
#         start at the same level
        
#         m + n + n * m ~ n^2
      
        def isSame(s, t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            
            if s.val == t.val and isSame(s.left, t.left) and isSame(s.right, t.right):
                return True
            else:
                return False
        
        def helper(s, t):
            if s == None:
                return False
            
            # if this two nodes are same, then return True, and will not go down
            if isSame(s,t):
                print(s.val)
                return True
            
            return helper(s.left, t) or helper(s.right, t)
            
        return helper(s,t)
# valid bst     
# lc 98
class Solution98:
    def isValidBST(self, root: TreeNode) -> bool:
        min_v = -float('inf')
        max_v = float('inf')

        def rec(root, lower, upper):
            if root == None:
                return True
            
            if root.val > lower and root.val < upper:
                return rec(root.left, lower, root.val) and rec(root.right, root.val, upper)
            
            else:
                return False
        
        return rec(root, -float("inf"), float("inf"))

        def ite(root): # in order traverse
            if root == None:
                return True
            
            # flag: whether we need to put back the node
            stack = [(root, -float('inf'), float('inf'))]

            while stack:
                temp = stack.pop()
                
                if temp[0].val <= temp[1] or temp[0].val >= temp[2]:
                    return False
                
                if temp[0].left:
                    stack.append((temp[0].left, temp[1], temp[0].val))
                
                if temp[0].right:
                    stack.append((temp[0].right, temp[0].val, temp[2]))
                
            return True
        
        return ite(root)

# range sum of BST
# LC 938
class Solution938:
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # traverse all node and conditionally add the cur.val
        self.TOTAL_SUM = 0
        def naive_sol(root):
            if root == None:
                return 
            
            naive_sol(root.left)
            naive_sol(root.right)
            
            if root.val >= L and root.val <= R:
                self.TOTAL_SUM += root.val
                   
            return
        
        # naive_sol(root)
        # return self.TOTAL_SUM
    
        # quicker method
        def helper(root):
            if root == None:
                return
            
            if root.val >= L and root.val <= R:
                self.TOTAL_SUM += root.val
                
                helper(root.left)
                helper(root.right)
            
            elif root.val > R:
                helper(root.left)
                
            elif root.val < L:
                helper(root.right)
                
            return
        
        helper(root)
        return self.TOTAL_SUM

# extra
# populating next right pointers in each node
# lc 113
from collections import deque
class Solution113:
    # bfs version
    def connect_bfs(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        
        queue = deque([(root, 1)])
        # trace the previous pointer
        prev = None
        pre_lev = 0
        
        while True:
            cur, lev = queue.popleft()
            if prev and prev_lev == lev:
                prev.next = cur
            prev = cur
            prev_lev = lev
            if cur == None:
                break
            else:
                queue.append((cur.left, lev + 1))
                queue.append((cur.right, lev + 1))
            
        return root
    # dfs solution
    def connect_dfs(self, root: 'Node') -> 'Node':
        if root == None:
            return
        
        def dfs(root):
            # base case: becaue it's a perfect tree, we could handle all operations on N-1 level
            if root.left == None:
                return
            
            # recursive rule
            root.left.next = root.right
            
            if root.next:
                root.right.next = root.next.left
            
            dfs(root.left)
            dfs(root.right)
            
            return
        
        dfs(root)
        
        return root

