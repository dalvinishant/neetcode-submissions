import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            d = sqrt(x**2 + y**2)
            heapq.heappush(distances, (d,(x,y)))
        
        return [c for _, c in heapq.nsmallest(k, distances)]

