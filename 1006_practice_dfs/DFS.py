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

# lc 200 numbers of island

class Solution200:
    def numIslands(self, grid: List[List[str]]) -> int:
        # coner case
        if grid == None or len(grid) == 0 or grid == [[]]:
            return 0
        
        # fill the visited map
        def dfs(grid, r, c):
            # base case
            if grid[r][c] == '0' or visited[r][c]:
                return
            
            # recursion rule
            
            visited[r][c] = True
            
            if r < row - 1:
                dfs(grid, r + 1, c)
            if r > 0:
                dfs(grid, r - 1, c)
            if c < col - 1:
                dfs(grid, r, c + 1)
            if c > 0:
                dfs(grid, r, c - 1)
            
            return
        
        # bfs not work, repeatly expand so many grid point, time limited exceeded
        def bfs(grid, r, c):
            # initial state
            queue = deque([(r, c)])
            
            # ternimate
            while queue:
                # generate
                r, c = queue.popleft()
                visited[r][c] = True
                
                # expand
                if r < row - 1 and grid[r + 1][c] == '1' and not visited[r + 1][c]:
                    queue.append((r + 1, c))
                if r > 0 and grid[r - 1][c] == '1' and not visited[r - 1][c]:
                    queue.append((r - 1,c))
                if c < col - 1 and grid[r][c + 1] == '1' and not visited[r][c + 1]:
                    queue.append((r, c + 1))
                if c > 0 and grid[r][c - 1] == '1' and not visited[r][c - 1]:
                    queue.append((r, c - 1))
            
            return
            
        # set to check whether is expanded for bfs
        expanded = set((0, 0))
        # fill the visited matrix, modified by add a set to avoid repeatly expand, could run
        def bfs(grid, r, c):
            # initial state
            queue = deque([(r, c)])
            
            # ternimate
            while queue:
                # generate
                r, c = queue.popleft()
                grid[r][c] = '0'
                
                # expand
                if r < row - 1 and grid[r + 1][c] == '1' and (r + 1, c) not in expanded:
                    expanded.add((r + 1, c))
                    queue.append((r + 1, c))
                if r > 0 and grid[r - 1][c] == '1' and (r - 1, c) not in expanded:
                    expanded.add((r - 1, c))
                    queue.append((r - 1,c))
                if c < col - 1 and grid[r][c + 1] == '1' and (r, c + 1) not in expanded:
                    expanded.add((r, c + 1))
                    queue.append((r, c + 1))
                if c > 0 and grid[r][c - 1] == '1' and (r, c - 1) not in expanded:
                    expanded.add((r, c - 1))
                    queue.append((r, c - 1))
            return

        # col row number
        row = len(grid)
        col = len(grid[0])
        
        # count
        count = 0
        
        # visited map
        visited = [[False for i in range(col)] for i in range(row)]
        
        # run dfs for each point
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # only 1 or not visited point could run dfs, and count add 1
                if grid[i][j] == '1' and visited[i][j] == False:
                    dfs(grid, i, j)
                    count += 1
        
        return count