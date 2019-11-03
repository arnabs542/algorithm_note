class Solution51: # O((n!)^2)
    def solveNQueens(self, n: int) -> List[List[str]]:
        # save each conditions when 1st queen in different columns
        positions = []
        # the result
        self.raw_ret = []
        # perform dfs
        self.helper(n, positions)
        # transfer the result
        print(self.raw_ret)
        self.transfer()
        
        return self.raw_ret
    
    def helper(self, n, positions):
        # base case when all the n queens positions have been set, we want to return and save the result 
        if len(positions) == n:
            self.raw_ret.append(positions.copy())
            return
        
        # recursion rule
        for i in range(n): # n is the number of columns in the board
            if self.check_nq(positions, i):
                positions.append(i)
                self.helper(n, positions)
                positions.pop()
            
        return
    
    def check_nq(self, positions, idx):
        invalid_set = set()
        for i in range(len(positions)):
            invalid_set.add(positions[i]) # check if in same col
            diff = len(positions) - i # think the current idx is on the len(positions)-th row, and the positions[i] is on i-th row, so we want the different
            invalid_set.add(positions[i] + diff) # right diagano
            invalid_set.add(positions[i] - diff) # left diagano
        if idx in invalid_set:
            return False
        
        return True
    
    def transfer(self):
        for pos_i in range(len(self.raw_ret)):
            positions = self.raw_ret[pos_i]
            
            for idx in range(len(positions)):
                stri = ''
                for i in range(positions[idx]): 
                    stri += '.'
                stri += 'Q'
                for i in range(positions[idx] + 1, len(positions)):
                    stri += '.'
                self.raw_ret[pos_i][idx] = stri
        return
                
        
        
#     recursion tree:
#         level: n, each represent the n-th queen
#                                     1st
#         /       /       /       /        \       \       \       \  save the 1st q's index in the positions list          n *  n
#        2nd     2nd
#      ///\\\   //|\\                                                 use positions to check whether the branch is valid
    
#      .....
        
class Solution51_q: # O(n!)
    def solveNQueens(self, n: int) -> List[List[str]]:
        # save each conditions when 1st queen in different columns
        positions = []
        # the result
        self.raw_ret = []
        # perform dfs
        self.helper(n, positions)
        # transfer the result
        print(self.raw_ret)
        self.transfer()
        
        return self.raw_ret
    
    def helper(self, n, positions):
        # base case when all the n queens positions have been set, we want to return and save the result 
        if len(positions) == n:
            self.raw_ret.append(positions.copy())
            return
        
        # recursion rule
        invalid_set = set()
        for i in range(len(positions)):
            invalid_set.add(positions[i]) # check if in same col
            diff = len(positions) - i # think the current idx is on the len(positions)-th row, and the positions[i] is on i-th row, so we want the different
            invalid_set.add(positions[i] + diff) # right diagano
            invalid_set.add(positions[i] - diff) # left diagano
            
        for i in range(n): # n is the number of columns in the board
            if i not in invalid_set:
                positions.append(i)
                self.helper(n, positions)
                positions.pop()
            
        return
    
    def transfer(self):
        for pos_i in range(len(self.raw_ret)):
            positions = self.raw_ret[pos_i]
            
            for idx in range(len(positions)):
                stri = ''
                for i in range(positions[idx]): 
                    stri += '.'
                stri += 'Q'
                for i in range(positions[idx] + 1, len(positions)):
                    stri += '.'
                self.raw_ret[pos_i][idx] = stri
        return
  