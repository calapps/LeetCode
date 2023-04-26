# https://leetcode.com/problems/longest-palindrome/

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:

        if not s:
            return 0
        
        maxLen = 0
        dictS = Counter(s)
        
        oddBool = False

        for val in dictS.values():
            if val % 2 == 0:
                maxLen += val
            elif val % 2 == 1:
                maxLen += val-1
                if oddBool == False:
                    maxLen += 1
                    oddBool = True

        return maxLen

        # if palindrome is even then there are an even amount used by each side
        # if palindrome is odd then there is an even amount used by each size + 1
        # s = "aab" => "aba"
        # s1 = "aabb" => "aabb"
        # s = {a:2, b:2} if val%2 == 0 then we can use it
        # can account for odd is the real issue here

        # s = "abccccdd" => dictS = {a:1, b:1, c:4, d:2}
        # 1 and oddBool = True, 1, 5, 7
        # s = "a"
        # 1 

        # I made a mistake because I misread the problem. I thought if we have an odd amount like 3, we can't use any of it
        # if we already used an odd amount, but it turns out we can use 2 out of the 3 chars from it, and can use
        # the 3rd char is we never added an odd number onto our count in the first place
        # s = "aabbbcccdd" would be "adcbbbcda" instead of "adbbbda"
