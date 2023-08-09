# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = [False for _ in range(len(s)+1)]
        memo[0] = True
        # penpie , [pen,pie]
        # memo = [-1,-1,1,-1,-1,1], idx = 2, 5, 5-len(pen)

        for i in range(1, len(s)+1):
            for word in wordDict:
                if i-len(word) >= 0:
                    
                    if memo[i] == True:
                        break

                    if s[i-len(word):i] == word:
                        memo[i] = memo[i-len(word)]
        return memo[-1]

        # s="penpen", worddict = ["pie", "pen"]
        # memo=[1,-1,-1,-1,-1,-1]
        # 
