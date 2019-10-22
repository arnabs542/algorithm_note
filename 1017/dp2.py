class Solution45:
    def jump(self, nums):
        # 2 3 1 1 4
        #         0
        
        # 2 3 1 1 4
        #       1 0
        
        # 2 3 1 1 4
        #     2 1 0
        
        # 2 3 1 1 4
        #   1 2 1 0
        
        # 2 3 1 1 4
        # 2 1 2 1 0
        
        # base case
        M = [0 for i in range(len(nums))]
        
        # induction rule
#         M[4]
        
#         M[3] = min(M[3:3+1]) + 1
        
#         M[2] = min(M[2:2+1]) + 1
        
#         M[1] = min(M[1:1+3]) + 1
        
#         M[0] = min(M[0:0+2]) + 1
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                M[i] = float('inf')
            else:
                M[i] = min(M[i+1:i+nums[i]+1]) + 1
            print(M)
            # for j in range(i, i + nums[i] + 1):
            #     solu.append()
        return M[0]
S = Solution45()           
print(S.jump([2,3,0,1,4]))
