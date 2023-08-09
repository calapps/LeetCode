# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]
        memo[1][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                memo[i][j] = max(memo[i][j], memo[i-1][j] + memo[i][j-1])

        return memo[-1][-1]
