# review the dp1 lesson in laioffer
class Solution_674:
    def findLengthOfLCIS(self, nums):
#         current = current + 1       if array[2] > array[1]
#                   1                otherwise

#         global max = current        if current > global max
# 	                 global max     otherwise
#         base case
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        
        # induction rule
        solu = []
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
            else:
                curr = 1
            solu.append(curr)
                
        return max(solu)

class Solution_55_no_dp:
    def canJump(self, nums):
        # no dp
        farrest_posi = 0
        
        if len(nums) == 0: return True
        if len(nums) == 1: return True
        
        farrest_posi = 0 + nums[0]
        
        for i in range(1, len(nums)):
            if i > farrest_posi:
                return False
            temp = i + nums[i]
            if farrest_posi < temp:
                farrest_posi = temp
        
        return True

class Solution_55_dp:
    def canJump(self, nums):
        # dp
        if len(nums) == 0: return False
        if len(nums) == 1: return True
        
        solu = [False for x in range(len(nums))] # store whether we could get to the final target at that index
        
        # base case
        j = len(nums) - 1 # latest true index
        solu[j] = True # the final one index must be true

        # induction rule
        # from right to left, if index = n-1 could reach the latest true status index (j), then we could move forward (right to left) 
        # i.e. j <= nums[i] + i and solu[j] = True
        for i in range(len(nums) - 1, -1, -1):
            if j <= nums[i] + i and solu[j]:
                solu[i] = True
                j = i
        
        return solu[0]

class Solution_Q2:
#     Q2. Maximal Product when Cutting Rope
#     Given a rope with integer-length n, how to cut the ropt into m integer-length parts
#     with length p[0], p[1], ... p[m-1], in order to get the maximal product of p[0]*p[1]*...*p[m-1]?
#     m is determined by you and must be greater than 0 (at least one cut must be made)

    # method1 dp 左大段 右大段
    # base case 
    # m = 1
    # ONE CASE
    # _ 
    # M[1] = 1


    # induction rule:
    # m = 2
    # ONE CASE
    # _ | _    
    # M[2] = M[1] * M[1] = 1

    # m = 3
    # Two cases
    # _ | _ _
    # M[3] = max(1, M[1]) * max(2,  M[2]) = 1 * 2 = 2

    # _ _ | _ (repeated before)
    # M[3] = max(2, M[2]) * max(1, M[1]) = 2 * 1 = 2
    
    # M[3] = max(case1, case2) = 2

    # m = 4
    # Three cases (one repeated)
    # _ | _ _ _
    # M[4] = max(1, M[1]) * max(3, M[3]) = 3

    # _ _ | _ _
    # m[4] = max(2, M[2]) * max(2, M[2]) = 4

    # _ _ _ | _ (repeated before)

    # M[4] = max(case1, case2) = 4

    # ......

    def getMaxProduct_m1(self, m): # m: the length of the rope
        # base case
        if m == 0: return 0
        if m == 1: return 1

        solu = [1 for i in range(m + 1)] # store all solution for dp

        for n in range(2,m+1): # n test each length of rope that is smaller than m
            curr = [] # store each length of rope's all cases result
            for i in range(1, int((n + 1)/2) + 1): # i test the left part length of each case in different m
                curr.append(max(i, solu[i]) * max (n - i, solu[n - i]))
            
            solu[n] = max(curr) # add the maximum result to the solution
        return solu[m]

    # method2 dp 左大段 右小段
    # base case 
    # m = 1
    # ONE CASE
    # _ 
    # M[1] = 1

    # induction rule
    # m = 2
    # one case
    # _ | _
    # M[2] = max(1, M[1]) * 1 = 1

    # m = 3
    # two cases (this method, there are no repeats)
    # _ | _ _
    # M[3] = max(1, M[1]) * 2 = 2

    # _ _ | _
    # M[3] = max(2, M[2]) * 1 = 2

    # m = 4
    # three cases
    # _ | _ _ _
    # M[4] = max(1, M[1]) * 3 = 3
    # _ _ | _ _
    # M[4] = max(2, M[2]) * 2 = 4
    # _ _ _ | _
    # M[4] = max(3, M[3]) * 1 = 3

    # ...

    def getMaxProduct_m2(self, m): # m: the length of the rope
        # base case
        if m == 0: return 0
        if m == 1: return 1

        solu = [1 for i in range(m + 1)]

        # induction rule
        for n in range(2, m + 1):
            curr = []
            for i in range(1, n):
                curr.append(max(i, solu[i]) * (n - i))
            solu[n] = max(curr)

        return solu[m]

    # method3 recursion
    # base case
    # m == 1; return 0

    # recursive rule
    # 左大段 右小段
    # _ _ _ _ | _
    # _ _ _ | _ _
    # _ _ | _ _ _
    # ...

    def getMaxProduct_m3(self, m): # m: the length of the rope
        # base case
        if m <= 1: return 1

        solu = []
        for i in range(1, m):
            # do something
            solu.append(max(i, self.getMaxProduct_m3(i)) * max(m - i, self.getMaxProduct_m3(m - i)))

        return max(solu)

S = Solution_Q2()
print(S.getMaxProduct_m1(10))
print(S.getMaxProduct_m1(12))
print(S.getMaxProduct_m2(10))
print(S.getMaxProduct_m3(10))

class Solution152:
    def maxProduct(self, nums):
        max_ = 1
        min_ = 1
        ret = float('-inf')
        for n in nums:
            if n < 0:
                temp = max_
                max_ = min_
                min_ = temp
            max_ = max(max_*n, n) # if the number previous n is 0, then we will reset the max_, and begin a new loop
            min_ = min(min_*n, n)
            ret = max(max_, ret)
        return ret

class Solution53:
    def maxSubArray(self, nums):
        curl, curr = 0, 0
        cur_sum = 0
        global_max = float("-inf")
        while curr < len(nums):
            cur_sum += nums[curr]
            if cur_sum > global_max:
                global_max = cur_sum
            curr += 1
            if cur_sum < 0:
                curl = curr
                cur_sum = 0
                
        return global_max

class Solution300:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        
        solu = [1 for i in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i+1):
                if nums[j] < nums[i]: 
                    # we need to check the nums[j] <? nums[i], if <, then consider update the solu[i]. But if solu[i] > nums[j] + 1 (previous loop could cause this), we need not update the solu[i]
                    
                    #solu[i] = solu[j] + 1     if solu[i] < solu[j] + 1
                    #          solu[i]         otherwise
                    solu[i] = max(solu[i], solu[j] + 1)
        
        return max(solu)
                    
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74836/My-easy-to-understand-O(n2)-solution-using-DP-with-video-explanation

# nlogn solution (AND ALSO OTHER NORMAL DP SOLUTION
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/152065/Python-explain-the-O(nlogn)-solution-step-by-step

# jump game 2 worked O n^2 solution
class Solution45:
    def jump(self, nums: List[int]) -> int:
        cache = [float('inf') for i in range(len(nums))]
        
        cache[0] = 0
        
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                next_ind = min(i + j, len(nums) - 1) # what is the next index we could jump to
                
                cache[next_ind] = min(cache[next_ind], cache[i] + 1) # whether or not we will update the solu at the next_ind, if it's smaller, we need to update
                
        return cache[len(nums) - 1]