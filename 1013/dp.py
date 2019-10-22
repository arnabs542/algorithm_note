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
