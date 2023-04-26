# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # preprocess to make a new string
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += (c.lower())

        if not newStr:
            return True 
        
        strLen = len(newStr)
        
        left, right = 0, 0
        if strLen % 2 == 0:
            # 4 => [0,1,2,3]
            left = (strLen // 2) - 1
            right = strLen // 2
        else:
            # 5 => [0,1,2,3,4]
            left = (strLen // 2) - 1
            right = (strLen // 2) + 1
        
        while left >= 0 and right < strLen:
            if not newStr[left] == newStr[right]:
                return False
            left -= 1
            right += 1
        
        return True 

obj = Solution()
str1 = "a bB  a"
str2 = "ab c ba"
str3 = "@# F #$g $@"

print(obj.isPalindrome(str1))
print(obj.isPalindrome(str2))
print(obj.isPalindrome(str3))
