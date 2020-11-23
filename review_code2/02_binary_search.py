
# search 2d I
class Solution74:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or matrix == [] or matrix == [[]]:
            return False
        # rows
        m = len(matrix)
        # colums
        n = len(matrix[0])
            
        def helper(matrix, target):
            left = 0
            right = m * n - 1
            
            while left <= right:
                mid = (left + right + 1) // 2
                
                r = mid // n
                c = mid % n
                
                if matrix[r][c] == target:
                    return True
                elif matrix[r][c] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return False
        
        return helper(matrix, target)

# search 2d II
class Solution240:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or matrix == [] or matrix == [[]]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        row = len(matrix) - 1
        col = 0
        
        while row >= 0 and col <= n - 1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
                
        return False
          