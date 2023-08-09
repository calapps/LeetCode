# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        myHeap = []
        for x,y in points:
            myHeap.append([(x-0)**2 + (y-0)**2, x, y])
        
        heapq.heapify(myHeap)
        
        for _ in range(k):
            dist, x, y = heapq.heappop(myHeap)
            res.append([x,y])
        
        return res 
            