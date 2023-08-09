# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        height = len(grid)
        width = len(grid[0])
        
        minutes = 0
        freshCount = 0
        q = deque()

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        
        while q and freshCount > 0:

            minutes += 1
            qlen = len(q)

            for _ in range(qlen):
                x,y = q.popleft()

                for i,j in [[x-1, y], [x+1, y], [x, y-1], [x,y+1]]:

                    if i >= 0 and i < height and j >= 0 and j < width and grid[i][j] == 1:
                        grid[i][j] = 2
                        freshCount -= 1
                        q.append([i,j])
        
        return minutes if freshCount == 0 else -1