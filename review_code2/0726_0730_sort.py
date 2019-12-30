class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    # # [5,1,1,2,0,0]
    #    5,1,1 | 2,0,0
    #    5,1|1 | 2,0|0
    #    5|1     2|0
    #    1 5     0 2
    #    1 1 5   0 0 2
    #    l       r
    #    # 0 1 5   1 0 2   
    #    # l         r
    #    # 0 1 5   1 0 2
    #    #   l       r
    #    # 0 0 5   1 1 2
    #    #   l         r
    #   
    # 0 0 5   1 1 2
        # self.insertionSort(nums)

        # self.selectionSort(nums)

        self.mergeSort(nums)
        
        # self.quickSort(nums)
        
        

        return nums
    # bubble sort
    def bubbleSort(self, nums):
        for i in range(len(nums)):
            for j in range(1, len(nums) - i):
                if nums[j] < nums[j - 1]:
                    self.swap(nums, j, j - 1)
        return
    
    # selection sort 5 1 1 2 0 0
    def selectionSort(self, nums):
        print(nums)
        for p in range(len(nums) - 1):
            temp = nums[p]
            minId = p + 1
            for i in range(p, len(nums)):
                if nums[i] < nums[minId]:
                    minId = i
            self.swap(nums, p, minId)
        return
    
    # insertion sort 5 1 1 2 0 0
    def insertionSort(self, nums):
        for p in range(1, len(nums)):
            temp = nums[p]
            
            i = p - 1
            while i >= 0 and nums[i] > temp:
                nums[i + 1] = nums[i]
                i -= 1
            nums[i + 1] = temp
        return 
    def mergeSort(self, nums):
        if nums == None or len(nums) <= 1:
            return nums
        
        left = 0
        right = len(nums) - 1
        
        self.mergeSortHelper(nums, left, right)
        
        return nums
    
    def mergeSortHelper(self, nums, left, right):
        # base case
        if left >= right:
            return 
        
        # recursive rule
        pivot = int((left + right) / 2)
        self.mergeSortHelper(nums, left, pivot)
        self.mergeSortHelper(nums, pivot + 1, right)
        
        L = nums[left:pivot + 1]
        R = nums[pivot + 1:right + 1]
        
        i = j = 0
        p = left
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[p] = L[i]
                i += 1
            else:
                nums[p] = R[j]
                j += 1
            p += 1
            
        while i < len(L):
            nums[p] = L[i]
            i += 1
            p += 1
        
        while j < len(R):
            nums[p] = R[j]
            j += 1
            p += 1
        
        return