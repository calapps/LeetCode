# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numLen = len(nums)

        numsDict = Counter(nums)

        for key, value in numsDict.items():
            if value > numLen // 2:
                return key

        return -1

# a = [2,2,3] => {2:2, 3:1}, 3//2 == 1, so > not >=