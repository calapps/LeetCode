# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        if not mat:
            return 

        rowLen = len(mat)
        colLen = len(mat[0])
        res = [[0 if mat[i][j] == 0 else 1 for j in range(colLen)] for i in range(rowLen)]
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        q = deque()
        visited = set()

        for i in range(rowLen):
            for j in range(colLen):
                if mat[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))
        
        while q:
                i,j = q.popleft()
                for x,y in directions:
                    newX = i-x
                    newY = j-y
                    if newX < 0 or newX >= rowLen or newY < 0 or newY >= colLen or (newX, newY) in visited:
                        continue
                    else:
                        res[newX][newY] = res[i][j] + res[newX][newY]
                        visited.add((newX, newY))
                        q.append([newX, newY])

        return res  
 
        # Here we basically know how to do bfs and want to use it but
        # the pre-main logic we need to have here is that to make it more efficient, we should do bfs starting
        # from the 0's that have 1's next to them and the way we do that is within the interal bfs logic where we
        # check if our adjacent node is in visited, or is a 0 or not and if so then it is a 0 or visited 1 and if not
        # it is a unvisited 1