# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,3,4]
        # prefix = [1,1,2,6]
        # postfix = [24, 12, 4, 1]
        # prefix[i] *= nums[i-1]

        res = [0 for _ in range(len(nums))]
        # prefix would be an array that for each index, that index
        # holds the mulitpliative sum of every number before that index
        # and postfix would be an array that for each index, that index
        # holds the same as above but for everthing on the right of that index

        prefix = [1 for _ in range(len(nums))]
        postfix = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            if i != 0:
                prefix[i] = prefix[i-1] * nums[i-1]
        
        for j in range(len(nums)-1, -1, -1):
            if j != len(nums)-1:
                postfix[j] = postfix[j+1] * nums[j+1]
        
        for k in range(len(nums)):
            res[k] = prefix[k] * postfix[k]
        
        return res

        # nums = [1,2,3,4,5]
        # prefix = [1,1,2,6,24]
        # postfix = [120,60,20,5,1]
        # res = [120, 60, 40, 30, 24]
        

