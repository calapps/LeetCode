# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, idx, path, res):
        res.append(path)  
        for i in range(idx, len(nums)):
            self.dfs(nums, i+1, path + [nums[i]], res)

        
        # [1,2,3]
        # [[], [1], [2], [3], [1,2], [1,3], [1,2,3], [2,3]]
        # For this question, the computation is done within the dfs function, where we append a num to the current path
        # it would look like newPath = path.append(nums[i])

#==========================

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        if not nums:
            return [[]]
        
        arrLen = len(nums) # 3 with input [1,2,3]

        # iterating over all permuations of i [0,8]
        for i in range(2**arrLen): # [0,1,2,3,4,5,6,7]
            
            tmpArr = [0 for _ in range(arrLen)] # same as above but with 0
            tmpRes = []
            for j in range(arrLen): # for 0,1,2
                if (i>>j) & 1 == 1: # if 1 & i == 1, meaning both bits are 1 at that index [0,1,0]
                                      # so for example, 3 would be [1,1,0] and we would make tmparr[1,1,0] enumerate to 1,2
                    tmpArr[j] = 1
            for k in range(len(tmpArr)): # iterate over the tmp array we made 
                if tmpArr[k] == 1: # if that index is 1
                    tmpRes.append(nums[k]) # append that index on nums to tmp arr
            
            res.append(tmpRes) # append it to the end

        return res
