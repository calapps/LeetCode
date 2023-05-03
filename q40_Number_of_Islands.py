# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        numIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    numIslands += 1
                    self.dfs(grid, i, j)

        return numIslands

    def dfs(self, grid, i, j):

        grid[i][j] = "0"

        for x, y in [[0,1], [0,-1], [1,0], [-1,0]]:
            newX = i-x
            newY = j-y
            if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) and grid[newX][newY] == "1":
                self.dfs(grid, newX, newY)

        return 

        