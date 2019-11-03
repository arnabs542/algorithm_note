class Solution841:
    def canVisitAllRooms(self, rooms):
        def openDoors(door_number, rooms):
            # base case
            if rooms[door_number] == None:
                return door_number, rooms
            
            # recursive rule
            temp = rooms[door_number]
            rooms[door_number] = None
            if len(temp) == 0:
                return door_number, rooms
            
            print(temp)
            
            for i in temp:
                door_number, rooms = openDoors(i, rooms)
            
            return door_number, rooms
        
        door_number, rooms = openDoors(0, rooms)
        print(rooms)
        for i in rooms:
            if i != None:
                return False
        return True
                
# S = Solution841()
# ret = S.canVisitAllRooms([[1],[2],[3],[]])
# print(ret)
            
class Solution547: # wrong
    def findCircleNum(self, M):
        
        def dfs(M, i, j):
            # base case 
            if M[i][j] == None or M[i][j] == 0:
                return M
            
            # recursive rule
            M[i][j] = None
            
            if i > 0:
                M = dfs(M, i - 1, j)
            if i < len(M) - 1:
                M = dfs(M, i + 1, j)
            if j > 0:
                M = dfs(M, i, j - 1)
            if j < len(M) - 1:
                M = dfs(M, i, j + 1)
        
            return M
        
        counter = 0 # count the number of friends circle
        
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    M = dfs(M, i, j)
                    counter += 1
        
        return counter

# S = Solution547()
# ret = S.findCircleNum([[1,0,0,1],
#                        [0,1,1,0],
#                        [0,1,1,1],
#                        [1,0,1,1]])
# print(ret)

class Solution542: # wrong
    def updateMatrix(self, M):
        ret = [[0 for i in range(len(M[0]))] for j in range(len(M))]
        
        def getDistance(M, i, j, n):
            # base case
            if M[i][j] == 0:
                return n
            
            # recursion rule
            self.vit[i][j] == True
            
            if i > 0:
                nu = getDistance(M, i - 1, j, n + 1)
            if i < len(M) - 1:
                nd = getDistance(M, i + 1, j, n + 1)
            if j > 0:
                nl = getDistance(M, i, j - 1, n + 1)
            if j < len(M[0]) - 1:
                nr = getDistance(M, i, j + 1, n + 1)
            
            return min(nl, nr, nd, nu)
        

        # for i in range(len(M)):
        #     for j in range(len(M[0])):
        #         if M[i][j] == 1:
        #             self.vit = [[False for i in range(len(M[0]))] for j in range(len(M))]
        #             ret[i][j] = getDistance(M, i, j, 0)
            self.vit = [[False for i in range(len(M[0]))] for j in range(len(M))]
            ret = getDistance(M, 2, 1, 0)
        return ret
            
S = Solution542()
ret = S.updateMatrix([[0,0,0],
                     [0,1,0],
                     [1,1,1]])

print(ret)