# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # stack processing in O(n)
        stack = []
        parMap = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in parMap.values():
                stack.append(c)
            elif c in parMap.keys():
                if stack[-1] == parMap[c]:
                    stack.pop() 
                else:
                    return False 

        return True if not stack else False

string1 = "(){}[]" # return True, stack = []
string2 = "({["    # return False, stack = [({[]
string3 = "(}[)"   # return False, stack = [(]

obj = Solution()

print(obj.isValid(string1))
print(obj.isValid(string2))
print(obj.isValid(string3))
