class Solution78_:
    def subsets(self, nums):
        solution = []
        self.findSubsets(nums, 0, solution)
        return
    
    def findSubsets(self, nums, index, solution):
        if index == len(nums):
            print(solution)
            return
        
        solution.append(nums[index])
        self.findSubsets(nums, index + 1, solution)
        solution.pop()
        self.findSubsets(nums, index + 1, solution)
    
# s = Solution78_()
# s.subsets(['a','b','c','d'])

class Solution78:
    def subsets(self, nums):
        ret = []
        solution = []
        self.findSubsets(nums, 0, solution, ret)
        return ret
    
    def findSubsets(self, nums, index, solution, ret):
        if index == len(nums):
            ret.append(solution.copy())
            return
        
        solution.append(nums[index])
        self.findSubsets(nums, index + 1, solution, ret)
        solution.pop()
        self.findSubsets(nums, index + 1, solution, ret)

# s = Solution78()
# print(s.subsets(['a','b','c']))

class Solution90:
    def subsetsWithDup(self, nums):
        ret = []
        solution = []
        nums = sorted(nums)
        self.findSubsets(nums, 0, solution, ret)
        return ret
    
    def findSubsets(self, nums, index, solution, ret):
        if index == len(nums):
            if solution not in ret:
                ret.append(solution.copy())
            return

        solution.append(nums[index])
        self.findSubsets(nums, index + 1, solution, ret)
        solution.pop()
        self.findSubsets(nums, index + 1, solution, ret)

s = Solution90()
print(s.subsetsWithDup(['1','2','2']))

