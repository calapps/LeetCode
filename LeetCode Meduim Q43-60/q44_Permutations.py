# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def backtracking(stack, length, visited):
            
            if length == len(nums):
                res.append(stack.copy())
                return 
            
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    stack.append(nums[i])
                    backtracking(stack, length+1, visited)
                    visited.remove(i)
                    stack.pop()
            

        backtracking([], 0, visited)
        return res