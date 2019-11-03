class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def treeGenerator(l):
    root = TreeNode(l[0])
    l[0]

    return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution100:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ret = self.helper(p, q);
        return ret
    
    def helper(self, p, q):
        # base case
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        print("p: ", p.val,"q: ", q.val)
        # recursive rule
        if p.val == q.val and self.helper(p.left, q.left) and self.helper(p.right, q.right):
            return True
        else:
            return False

class Solution110:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root)
        
    
    def helper(self, pointer):
        # base case
        if pointer == None:
            return True
        
        # recursive rule
        left = self.getHeight(pointer.left)
        right = self.getHeight(pointer.right)
        
        if abs(left - right) <= 1 and self.helper(pointer.left) and self.helper(pointer.right):
            return True
        else:
            return False
        
    def getHeight(self, pointer):
        # base case
        if pointer == None:
            return 0
        
        # recursive rule
        left = self.getHeight(pointer.left)
        right = self.getHeight(pointer.right)
        
        if left > right:
            return left + 1
        else:
            return right + 1

class Solution101:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.helper(root.left, root.right)
        
    
    def helper(self, left, right):
        # base case
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        
        # recursive rule
        if left.val != right.val:
            return False
        if self.helper(left.left, right.right) and self.helper(left.right, right.left):
            return True
        else:
            return False

class Solution733:
    def floodFill(self, image, sr, sc, newColor):
        R = len(image)
        C = len(image[0])
        visited = [[False] * C for _ in range(R)]
        temp = image[sr][sc]
        
        def dfs(sr, sc):
            image[sr][sc] = newColor
            visited[sr][sc] = True
            print(sr,sc)
        
            if sr - 1 >= 0 and image[sr-1][sc] == temp and not (visited[sr-1][sc]):
                dfs(sr-1, sc)
            if sr + 1 < len(image) and image[sr+1][sc] == temp and not (visited[sr+1][sc]):
                dfs(sr+1, sc)
            if sc - 1 >= 0 and image[sr][sc-1] == temp and not (visited[sr][sc-1]):
                dfs(sr, sc-1)
            if sc + 1 < len(image[0]) and image[sr][sc+1] == temp and not (visited[sr][sc+1]):
                dfs(sr, sc+1)
            return
        
        dfs(sr, sc)
        
        # print(visited)
        
        return image

S = Solution733()
T = S.floodFill([[1,1,1],[1,1,0],[1,0,1],[1,1,1]], 1, 1, 2)
print(T)