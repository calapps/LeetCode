# https://leetcode.com/problems/valid-anagram/

from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False 
        
        counterS = Counter(s)
        counterT = Counter(t)

        # can also do
        # counterS = [0] * 26
        # counterT = [0] * 26

        # for c in s:
        #     counterS[ord(c) - ord("a")] += 1

        # for c in t:
        #     counterT[ord(c) - ord("a")] += 1

        if counterS == counterT:
            return True 

        return False 

obj = Solution()

a = "rat"
b = "tar"
print(obj.isAnagram(a,b))

c = "asdfsfds"
d = "wefhthr"
print(obj.isAnagram(c,d))

c = "asdfsfds"
d = "wefhthri"
print(obj.isAnagram(c,d))