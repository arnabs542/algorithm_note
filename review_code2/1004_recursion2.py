


# leetcode 408
class Solution408:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
#         w: applestore
#         abb: app3to1e
#         index: 0
#               applestore             app3to1e
#                                       /     
#               pplestore            pp3to1e
#                                     /
#               plestore           p3to1e
#                                     \
#               lestore               3to1e
#                                    /
#               tore               to1e
#                                  /
#               ore              o1e, 7
#                                /
#               re              1e, 8
#                                \
#               e                 e
#                                 /
#               null              t
                        
        # word_id: the index of the word
        # abb_id: the index of the abbreviation
        # flag: whether prior index is digit
        def helper(word, abbr):
            # base case
            if word == '' and abbr == '':
                return True
            if word == '' or abbr == '':
                return False
            
            # recursive rule
            # abbrev's index
            i = 0
            counts = '0'
            # print(word, abbr)
            while i < len(abbr) and abbr[i].isdigit():
                if i == 0 and abbr[i] == '0':
                    return False
                counts += abbr[i]
                i += 1
            
            # number of indices we need to move
            counts = int(counts)
            
            # if the length is longer than remaining word
            if counts > len(word):
                return False
            
            if counts == 0 and word[0] == abbr[0]:
                return helper(word[1:], abbr[1:])
            elif counts != 0:
                return helper(word[counts:], abbr[counts // 10 + 1:])
                
        return helper(word, abbr)

# leetcode 48
# change of spiral matrix, rotate the matrix in-place
class Solution_48:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.n = len(matrix)
        
        def helper(matrix, lev):
            if self.n - 2 * lev == 1:
                # new_matrix[lev][lev] = matrix[lev][lev]
                return
            if self.n - 2 * lev == 0:
                return
            arr_copy = matrix[lev][lev:self.n - 1 - lev]
            # up, copy the right side matrix into the arr_copy
            for i in range(lev, self.n - 1 - lev):
                temp = matrix[i][self.n - 1 - lev]
                print(i, self.n - 1 - lev, lev)
                matrix[i][self.n - 1 - lev] = arr_copy[i - lev]
                arr_copy[i - lev] = temp
            # right, copy the down side matrix into the arr_copy
            for i in range(lev, self.n - 1 - lev):
                temp = matrix[self.n - 1 - lev][self.n - 1 - i]
                matrix[self.n - 1 - lev][self.n - 1 - i] = arr_copy[i - lev]
                arr_copy[i - lev] = temp
            # down, copy down side to left side
            for i in range(lev, self.n - 1 - lev):
                temp = matrix[self.n - 1 - i][lev]
                matrix[self.n - 1 - i][lev] = arr_copy[i - lev]
                arr_copy[i - lev] = temp
            # left, we need not copy any thing, becasue it's already be the final round
            for i in range(lev, self.n - 1 - lev):
                matrix[lev][i] = arr_copy[i - lev]
            
            helper(matrix, lev + 1)
            
            return

        # new_matrix = [[0 for i in range(self.n)] for i in range(self.n)]
        helper(matrix, 0)