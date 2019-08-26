
# leetcode  658  Find K Closest Elements
# post procession solution
class Solution:
    def findClosestElements(self, arr, k, x):
        if arr == None or len(arr) == 0:
            return None
        tar_id = self.bSearch(arr,x)
        ret = self.expand(arr, tar_id, k, x)
        return sorted(ret)
        
    def bSearch(self, arr, x):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = int((left + right) / 2)
            if x == arr[mid]:
                return mid
            elif x > arr[mid]:
                left = mid + 1 
            else:
                right = mid - 1
        
        return mid
    
    def expand(self, arr, tar_id, k, x):
        left, right = tar_id - 1, tar_id + 1
        counter = 1
        ret = [arr[tar_id]]
        
        while counter < k:
            if left < 0:
                ret += arr[right:right + k - counter]
                break
            if right > len(arr) - 1:
                ret += arr[left -(k - counter) + 1:left + 1]
                break
            if abs(arr[left] - x) > abs(arr[right] - x):
                ret.append(arr[right])
                print("add right", abs(arr[left] - arr[tar_id]), abs(arr[right] - arr[tar_id]))
                right += 1
            else:
                ret.append(arr[left])
                left -= 1
            print(ret, tar_id, left, right)
            
            counter += 1
        print(ret)
        
        return ret

# s = Solution()
#print(s.findClosestElements([1, 2, 2, 2, 2, 3, 3, 3, 5, 5, 5, 99, 99, 99, 100, 10000, 10002, 10004, 10004, 10004], 3, 100))

# directly find the lower bound of the window

# 74

class Solution74:
    def searchMatrix(self, matrix, target):
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        left = self.twoDToOneD(0, 0)
        right = self.twoDToOneD(m, n)
        
        while left <= right:
            mid = (left + right) // 2
            row, col = self.oneDToTwoD(mid, m, n)
            print(matrix[row][col])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
        
    def twoDToOneD(self, m, n):
        return  m*(n+1) + n
    
    def oneDToTwoD(self, index, m, n):
        return index // (n + 1), index - (index // n) * (n + 1)

s74 = Solution74()
#print(s74.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],13))

# 33
class Solution33:
    def search(self, nums, target):
        if nums == None or len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            print(nums[mid], left, right)
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[left]: #and nums[left] > nums[right]: # why mid = left
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid] and target >= nums[left]:
                    right = mid - 1 
                else: # target < nums[mid] and target < nums[left]
                    left = mid + 1
            elif nums[right] > nums[mid]:# and nums[left] > nums[right]:
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else: # target > nums[mid] and target > nums[right]:
                    right = mid - 1

            # else:
            #     if target > nums[mid]:
            #         left = mid + 1
            #     else:
            #         right = mid - 1
        return -1

s = Solution33()
print(s.search([3,1],1))