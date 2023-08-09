# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return intervals

        res = []
        intervals.sort(key= lambda x: x[0])

        for i in range(len(intervals)):
            if not res or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        
        return res





        # need to ask is [1,4], [4,5] overlapping or not
        # for questions like these, draw it out bascially and enumate every overlap case