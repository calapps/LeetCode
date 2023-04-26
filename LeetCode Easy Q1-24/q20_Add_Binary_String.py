# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # set listA to be the longer of the two
        listA = list(a) if len(a) >= len(b) else list(b)
        listB = list(b) if len(b) <= len(a) else list(a)

        # want to padd it out with an extra 0 in front just incase
        listA = ["0"] + listA
        listB = ["0"] * (len(listA) - len(listB)) + listB
        
        # transfer every item into an int
        for i in range(len(listA)):
            listA[i] = int(listA[i])
            listB[i] = int(listB[i])

        # set the carry and the return result
        remainder = 0
        res = [0] * len(listA)

        # iterate backwards since binary goes from right to left (lsb to msb) and calculate
        for i in range(len(listA)-1, -1, -1):
            # if we have a 0 or 1
            if remainder + listA[i] + listB[i] < 2:
                res[i] = remainder + listA[i] + listB[i]
                remainder = 0

            # if we have a 2 or 3
            elif remainder + listA[i] + listB[i] >= 2:
                res[i] = (remainder + listA[i] + listB[i]) % 2
                remainder = 1

        # make the array into a string again
        for i in range(len(res)):
            res[i] = str(res[i])

        # join the string as one
        res = "".join(res)
        
        # shave off the frontal zeroes
        while res[0] == "0" and len(res) > 1:
            res = res[1:]

        return res