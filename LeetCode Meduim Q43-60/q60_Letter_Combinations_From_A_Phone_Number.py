lass Solution:
# 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        num2let = {}
        num2let["2"] = {"a","b","c"}
        num2let["3"] = {"d", "e", "f"}
        num2let["4"] = {"g","h","i"}
        num2let["5"] = {"j", "k", "l"}
        num2let["6"] = {"m","n","o"}
        num2let["7"] = {"p", "q", "r", "s"}
        num2let["8"] = {"t","u","v"}
        num2let["9"] = {"w", "x", "y", "z"}

        res = []
        stack = []

        if not digits:
            return []
            
        def backtracking(idx):
            
            # we are at the root node we want
            if idx == len(digits):
                res.append("".join(stack.copy()))
                return
            
            if idx < len(digits):

                for char in num2let[str(digits[idx])]:
                    stack.append(char)
                    backtracking(idx + 1)
                    stack.pop()

        backtracking(0)

        return res                   
            
