# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total+candidates[i])
            curr.pop()
            dfs(i+1, curr, total)
        
        dfs(0, [], 0)
        return res

        # first miskae was mistaking k for target
        # second mistake was a semantic one where you did x = stack.sort(), where it sorts itself
        # and doesn't return a sotred stak
        # third is some random tuple shit you don't
        # I AM CONFUSED WHY IT DOESN'T HIT THE 333333 CASE FOR CASE 4

        # IT TURNS OUT THAT THE WAY YOU DO BACKTRACKING IS ALL WRONG IN THSI CASE BECAUSE WE GO THROUGH
        # EVERY COMBO, LOOK AT THIS VIDEO
        # https://www.youtube.com/watch?v=GBKI9VSKdGg
        # so bascially we have the choice to either include candidates[i] or not include candidates[i]
        # and do that 