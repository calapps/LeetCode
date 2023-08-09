# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins = [1,2,5], amount = 11
        # 5+5+1 == 11 => 3
        # 5 = 5, 5+5 = 10, 10+1 = 1
        # dynamic programming, where we can do it either recursively top down or
        # iteratively bottom up
        # and because of stack overflow I would choose to do it iteravteyl bottom up

        # memo = [-1 * amount]
        # for coin in coins, memo[coin] = coin
        # for i in range(amount), for coin in coins, if i-coin >= 0, memo[i] = max(memo[i]memo[i-coin] + 1)
        #return memo[-1]

        memo = [99999 for _ in range(amount+1)]
        memo[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if i-coin >= 0:
                    memo[i] = min(memo[i], 1 + memo[i-coin])

        return -1 if memo[amount] == 99999 else memo[amount]

# memo[1] = 1
# memo[2] = 1
# memo[5] = 1
# memo[10] = 1+1
# memo[11] = 2+1
# 



