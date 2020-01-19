# leet code 78
# subset, not permutation, so we also need not to consider situation that duplicate like 21, 12
# I use the index to de-duplicate the useless situation.
# in each node in the recursion, we need to add the path into our result
# the index indicates that which element we have search (from depth or width)
class Solution78:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.RET = [[]]
        
#                            root
#                       /     |     \
#                      1      2      3
#                     / \     |
#                    2   3    3
#                    |
#                    3
        
        
        def dfs(nums, index, path):
            #print(path)
            # base case
            if index == len(nums):
                return
            
            path.append(nums[index])
            self.RET.append(path.copy())
            
            # search depth
            dfs(nums, index + 1, path)
            path.pop()
            
            # search same level
            dfs(nums, index + 1, path)
            return
        
        dfs(nums, 0, [])
        return self.RET

# leetcode 22: valid parenthesis
# we need to maintaince two variables, right and left, to keep track the number of the ( and )
# when we could add (: only when left < n
# when we could add ): only when right < left
# we also keep the path of the result, but we only add the path into the result in the last level

class Solution22:
    def generateParenthesis(self, n: int) -> List[str]:
        RET = []

        def dfs(right, left, path):
            # base case
            if right + left == 2 * n:
                RET.append("".join(path))
                return
            
            if right < n:
                path.append("(")
                dfs(right + 1, left, path)
                path.pop()
                
            if left < right:
                path.append(")")
                dfs(right, left + 1, path)
                path.pop()
            
            return
            
        dfs(0, 0, [])
        return RET

# leetcode 39 (same with the laioffer coin districution)
# this is not the best solution, we add the coins one by one, and keep the track of the anwser
# what about the recursion tree:


class Solution39:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        RET = []
        
        def dfs(path, curr_sum, index):
            # base case
            if curr_sum > target:
                return
            elif curr_sum == target:
                RET.append(path.copy())
                return
            
            # recursive rule
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(path, curr_sum + candidates[i], i)
                path.pop()
            
            return
        
        dfs([], 0, 0)
        
        return RET

# leetcode 46 permutation1
class Solution46:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
  #        recursion tree:
     
  #           root
  #        /    |    \
  # 0     1     2     3
  #     /  \   /  \   / \
  # 1  2   3  1   3  1   2
  #    |   |  |   |  |   |
  # 2  3   2  3   1  2   1
        
  # path -> List: track the path
  # visited -> Set: track the visited element
        # store all results
        RET = []
    
        def dfs(visited, path):
            # base case
            if len(path) == len(nums):
                RET.append(path.copy())
                return
            
            # recursive rule
            for i in range(len(nums)):
                if i not in visited:
                    path.append(nums[i])
                    visited.add(i)
                    dfs(visited, path)
                    visited.remove(i)
                    path.pop()
            
            return
        
        dfs(set(), [])
        return RET

# leetcode 47
class Solution47:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
  #        recursion tree:
     
  #           root
  #        /        \
  # 0     1           2
  #     /  \         / 
  # 1  1   2        1   
  #    |   |        |   
  # 2  2   1        1   
        
  # path -> List: track the path
  # visited -> Set: track the visited element
        # store all results
        RET = []
    
        def dfs(visited, path):
            # base case
            if len(path) == len(nums):
                RET.append(path.copy())
                return
            
            level_set = set()
            # recursive rule
            for i in range(len(nums)):
                if i not in visited and nums[i] not in level_set:
                        level_set.add(nums[i])
                        path.append(nums[i])
                        visited.add(i)
                        dfs(visited, path)
                        visited.remove(i)
                        path.pop()
                        
            return
        
        dfs(set(), [])
        return RET