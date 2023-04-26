# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        minNum = float('inf')
        maxProfit = 0

        for num in prices:
            if num < minNum:
                minNum = num 
            elif num > minNum:
                maxProfit = max(maxProfit, num-minNum)

        return maxProfit


nums1 = [1,10,3,5,6,4,7]
nums2 = [10,9,8,2]
obj = Solution()

print(obj.maxProfit(nums1))
print(obj.maxProfit(nums2))
