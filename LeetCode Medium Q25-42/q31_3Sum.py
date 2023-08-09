# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        counterDict = Counter(nums)
        res = set()

        for i in range(len(nums)):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b = nums[j]
                c = -1*(a+b)

                if c not in counterDict.keys():
                    continue
                
                have_c = counterDict[c]

                if c == a:
                    have_c -= 1

                if c == b:
                    have_c -= 1

                addTriplet = [a,b,c]
                addTriplet.sort()
                addTriplet = tuple(addTriplet)

                if have_c > 0:
                    res.add(addTriplet)

        return res

        # this is the extension of the two sum problem where in two sum we are given
        # a target number and want to find the two numbers that sum up to this one!
        # For twosum, we use a dict to check if we are on a then if b does exists, return their indicies
        # else if it doesn't then add it to the dict and continue. FOR THIS PROBLEM WE ALSO USE A DICTIONARY TO FIND
        # THE THIRD NUMBER