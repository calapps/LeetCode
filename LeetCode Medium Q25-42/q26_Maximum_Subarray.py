# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        memo = [0 for _ in range(len(nums))]
        memo[0] = nums[0]

        for i in range(1, len(nums)):
            memo[i] = max(memo[i-1] + nums[i], nums[i])
        return max(memo)

        # [5,4,-1,7,8]
        # [5,9,8,15,23]

        # [-2,1,-3,4,-1,2,1,-5,4]
        # [-2,1,-2,4,3,5,6,-1,4]