# https://leetcode.com/problems/flood-fill/

from collections import deque 

class Solution:
    def floodFill(self, image, sr, sc, color):
        
        if not image or image[sr][sc] == color:
            return image 
    
        fillColor = image[sr][sc]
        qfill = deque([[sr,sc]])

        while qfill:     

            for _ in range(len(qfill)):

                x,y = qfill.popleft()
                image[x][y] = color 

                for i, j in [[x-1,y], [x+1,y], [x,y-1], [x,y+1]]:
                    
                    if i >= 0 and i < len(image) and j >= 0 and j < len(image) and image[i][j] == fillColor:
                        qfill.append([i,j])

        return image


grid1 = [[1,2,2], 
         [3,2,1], 
         [0,3,2]]
sr, sc, color = 1, 1, 3

obj = Solution()
print(obj.floodFill(grid1, sr, sc, color))
