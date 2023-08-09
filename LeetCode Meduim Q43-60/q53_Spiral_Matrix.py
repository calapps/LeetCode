# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        mn = m*n
        
        res = []
        u,d,l,r = 0, m-1, 0, n-1

        while u<=d and l<=r:

            for i in range(l,r+1):
                res.append(matrix[u][i])
            u += 1

            if len(res) > mn:
                break

            for j in range(u,d+1):
                res.append(matrix[j][r])
            r -= 1

            if len(res) > mn:
                break
            
            for k in range(r,l-1,-1):
                res.append(matrix[d][k])
            d -= 1

            if len(res) > mn:
                break

            for o in range(d,u-1,-1):
                res.append(matrix[o][l])
            l += 1

            if len(res) > mn:
                break
                
        return res[:mn]
