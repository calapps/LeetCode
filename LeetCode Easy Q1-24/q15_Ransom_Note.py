# https://leetcode.com/problems/ransom-note/

from collections import Counter 
class Solution:
    def canConstruct(self, ransomNote, magazine):

        if not magazine and ransomNote:
            return False
        
        magDict = Counter(magazine)
        ranDict = Counter(ransomNote)

        for ranKey in ranDict.keys():
            if ranKey not in magDict.keys():
                return False 
            if ranDict[ranKey] > magDict[ranKey]:
                return False 
        
        return True 

# ransomNote = "abc"
# magazine = "aabccd"
# ranDict = {a:1, b:1, c:1}
# magDict = {a:2, b:1, c:2, d:1}

# rN = "a"
# m = "b"
# rD = {a:1}
# mD = {b:1}

# m = ""
# rn = "f"
