# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # since we want to process the string, a stack should do
        # use a stack in O(n) time

        stack = []
        ops = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            
            elif token in ops:
                rightval = stack.pop()
                leftval = stack.pop()

                if token == "+":
                    stack.append(leftval + rightval)
                
                if token == "-":
                    stack.append(leftval - rightval)

                if token == "*":
                    stack.append(leftval * rightval)
                
                if token == "/":
                    stack.append(int(leftval / rightval))
        
        return stack.pop()

        