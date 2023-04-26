  
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        # so first I setup a hashmap and iteratve over nums with it in order to create the hashmap 
        intMap = {}
        for idx, item in enumerate(nums):
            intMap[item] = idx
        # now that we created our mapping, we can then 
        # iterate over it once more in order to find the Solution

        for item in nums:
            if target-item in intMap.keys():
                return [intMap[item], intMap[target-item]]

        # it's impossible but place it here anyways just incase
        return [-1, -1]

# So we should check it with some testcases

nums = [1,2,3,99] 
target = 5
# returns [1,2]
# since it's guarenteed to have atleast one solution with two numbers adding up to it, we are fine here.

obj = Solution()
print(obj.twoSum(nums, target))

