# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        i = 0
        length = 0

        for j in range(len(s)):
            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1
            
            charSet.add(s[j])
            length = max(length, j-i+1)
        
        return length