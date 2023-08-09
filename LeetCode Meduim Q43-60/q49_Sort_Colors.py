# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bucket sort ez
        colors = [0, 0, 0]

        for i in range(len(nums)):
            colors[nums[i]] += 1
        
        index = 0
        for idx, val in enumerate(colors):
            for i in range(val):
                nums[index+i] = idx
            index += val
         
        return 

        # here we use bucket sort. since we know there is only 0,1,2 as colors, we can just count the number of 0,1,2's and then
        # fill them up in the array