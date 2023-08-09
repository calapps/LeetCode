# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        
        # strip all whitespace
        listInt = list(s.strip())
        # if empty then return false
        if len(listInt) == 0:
            return 0
        # setup variables
        i, res, carry, sign = 0, 0, 1, 1

        # take account of the - or + sign
        if listInt[0] == "-":
            sign = -1
            i = 1
        if listInt[0] == "+":
            i = 1
        
        # trim the string down even more from left to right since we are
        # iterating right to left
        newStr = ""
        end = 0
        for k in range(i, len(listInt)):
            if listInt[k].isdigit():
                end = k
            else:
                break
        
        newStr = listInt[0:end+1]

        # iterate and calculate the total int value
        for j in range(len(newStr)-1, i-1, -1):
            if not newStr[j].isdigit():
                break 
            num = int(newStr[j])
            res += num * carry
            carry *= 10

        res = sign*res

        # check if its in bounds, else clamp it
        minNum = -2**31
        maxNum = 2**31-1
        if res < minNum:
            res = minNum
        elif res > maxNum:
            res = maxNum
        
        return res