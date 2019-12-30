# binary search: lc 704
class Solution704:

    def classic_search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            
            elif nums[mid] > target:
                right = mid - 1
        
        return -1
    
    def search_recursive(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1
        ret = self.helper(nums, 0, len(nums) - 1, target)
        
        if nums[ret] == target:
            return ret
        else:
            return -1
    
    def helper(self, nums, left, right, target):
        # base case
        if left >= right:
            return left
        
        # recursive rule
        mid = (right + left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        
        return self.helper(nums, left, right, target)

# leetcode 74
class Solution74:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2d indices to 1d index
        # def two2one(row, col, colN):
        #     return row * colN + col
        
        # 1d index to 2d indices
        # def one2two(idx, colN):
        #     return (idx // colN, idx % colN )
        
        if matrix == None or len(matrix) == 0:
            return False
        
        colN = len(matrix[0])
        rowN = len(matrix)
        
        # convert the 2d to 1d
        left = 0
        right = (rowN - 1) * colN + colN - 1
        
        # binary search
        while left <= right:
            mid = (left + right) // 2
            midRow, midCol = (mid // colN, mid % colN)

            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

# leetcode 240
class Solution240:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # O(m + n)
        if len(matrix) == 0 or matrix == [[]]:
            return False
        
        # we want to search from left bottom to right top
        m = len(matrix)
        n = len(matrix[0])
        
        row = m - 1
        col = 0
        
        # each time we move the row and col
        while row >= 0 and col <= n - 1:
            if matrix[row][col] == target:
                return True
            # if target is smaller, then move upper
            elif matrix[row][col] > target:
                row -= 1
            
            # if target is larger, then move right
            elif matrix[row][col] < target:
                col += 1
        
        return False

# laicode 17: find closest element
class Solution_lai17(object):
  def closest(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    if len(array) == 0:
      return -1
    if len(array) == 1:
      return 0
    # write your solution here
    # use a classic binary search, and then find the closest element
    left = 0
    right = len(array) - 1

    while left <= right: # (left < right - 1) could be better
      mid = (left + right) // 2

      if array[mid] == target:
        return mid
      elif array[mid] > target:
        right = mid - 1
      else:
        left = mid + 1
    
    if right < 0 or left > len(array) - 1:
      return mid

    if abs(array[left] - target) > abs(array[right] - target):
      return right
    else: 
      return left

# lc 658 find k closest
class Solution658:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 0:
            return []
        
        # firstly perform a binary search
        def b_search(arr, x):   
            left = 0
            right = len(arr) - 1

            while left < right:
                mid = (left + right) // 2

                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    right = mid - 1
                else:
                    left = mid + 1

            ret = 0

            # we save mid
            if left < 0 or right > len(arr) - 1:
                ret = mid

            if abs(arr[left] - x) > abs(arr[right] - x):
                ret = right
            else:
                ret = left
                
            return ret
        
        # post-procession to get the k closest elements by moving left and right
        def expand(arr, ret, k, x):
            # left (exclude in the result), right (exclude in the result) ******
            left = ret - 1
            right = ret + 1

            k -= 1

            while k > 0 and left >= 0 and right <= len(arr) - 1:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    left -= 1
                else: # elif abs(arr[left] - x) > abs(arr[right] - x):
                    right += 1

                k -= 1

            # if left or right has already arrived the edge
            if left >= 0:
                while k > 0:
                    left -= 1
                    k -= 1
            if right <= len(arr) - 1:
                while k > 0:
                    right += 1
                    k -= 1

            return left, right
    
        ret = b_search(arr, x)
        
        left, right = expand(arr, ret, k, x)
        
        # because we exclude left, so left ++, we exclude right, so right
        return arr[left + 1:right]

# lai15: find first occurence
class Solution_l15(object):
  def firstOccur(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    # first perform a classic binary search
    if len(array) == 0:
      return -1

    def b_search(array, target):
      left = 0
      right = len(array) - 1

      while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
          return mid
        elif array[mid] < target:
          left = mid + 1
        else:
          right = mid - 1

      return -1
    
    def find_first(array, ret, target):
      if ret == -1:
        return -1

      while ret >= 0 and array[ret] == target:
        ret -= 1

      return ret + 1
    
    ret = b_search(array, target)
    result = find_first(array, ret, target)

    return result

# lai 16 find last occurence
class Solution_l16(object):
  def lastOccur(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    # first perform a classic binary search
    if len(array) == 0:
      return -1

    def b_search(array, target):
      left = 0
      right = len(array) - 1

      while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
          return mid
        elif array[mid] < target:
          left = mid + 1
        else:
          right = mid - 1

      return -1
    
    def find_last(array, ret, target):
      if ret == -1:
        return -1
      
      while ret <= len(array) - 1 and array[ret] == target:
        ret += 1
      
      return ret - 1
    
    return find_last(array, b_search(array, target), target)

# lc 702 search in a sorted array with unknown size
class Solution702:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # firstly, want to find the target number in a range
        # ex: target = 9877
        # arr = 1 2 3 4 5 ............................
        # 
        # (1: 10^0
        # 1
        # (2: 10^1
        # 2 3 4 5 6 7 8 9 10 
        # (3: 10^2
        # 11 12 13 ...... 100
        # (4: 10^3
        # 100...... 1000
        # (5: 10^4
        # 1000.......10000
        # expand our searching space ten times each time
        # level 1
        k = 0
        if reader.get(k) == target:
            return k
        
        level = 1
        
        # should be >, could not be =;  if want to be >=, should change the left index
        while target > reader.get(2 ** level - 1):
            level += 1
        # after get the upper bound, we want to get the lower bound
        left = 2 ** (level - 1)
        right = 2 ** level - 1
        
        # perform binary search
        while left <= right:
            mid = (left + right) // 2
            
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

# leet code 33
# answer and analysis: https://leetcode.wang/leetCode-33-Search-in-Rotated-Sorted-Array.html
# solution 3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # judge which part is only increased
            # if left part is only increased
            if nums[left] <= nums[mid]:
                # judge whether the target is in the only increased part of array
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            # if right part is only increased
            else:
                # if target is in the only increased part
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                # if not
                else:
                    right = mid - 1
            
        return -1



# leect code 81
# solution and analysis:https://leetcode.wang/leetCode-81-Search-in-Rotated-Sorted-ArrayII.html
class Solution81:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # judge which part is only increased, if nums[left] == nums[mid], we update left
            if nums[left] == nums[mid]:
                left += 1
            # if left part is only increased
            elif nums[left] < nums[mid]:
                # judge whether the target is in the only increased part of array
                if target <= nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            # if right part is only increased
            else:
                # if target is in the only increased part
                if target <= nums[right] and target >= nums[mid]:
                    left = mid + 1
                # if not
                else:
                    right = mid - 1
            
        return False