import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_k = right
        while left <= right: 

            mid = (left + right) // 2

            time_spent = sum([math.ceil(x/mid) for x in piles])
            
            if time_spent > h:
                left = mid + 1
            else:
                min_k = mid
                right = mid - 1
        
        return min_k