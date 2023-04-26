# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left = 1
        right = n
        res = -1

        while left <= right:
            middle = left + (right-left)//2
            
            if isBadVersion(middle) == False:
                left = middle + 1
            
            if isBadVersion(middle) == True:
                right = middle - 1
                res = middle
        
        return res
        
        # n = 5, [T,T,T,F,F]
        # l=1,r=5,m=3, => l=4,r=5,m=4 res=4, l=4,r=4,m=4, res=4, returns index 4 
        # n=2, [F,F]
        # l=1,r=2,m=1, res=1 => l=1,r=1,m=1, res=1, returns index 1