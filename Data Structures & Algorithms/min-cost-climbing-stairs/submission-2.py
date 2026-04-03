class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        m = {}
        return min(self.climb(0, cost, m), self.climb(1, cost, m))
    
    def climb(self, i, cost, m):
        if i >= len(cost):
            return 0

        # if i == len(cost) - 1 :
        #     return 1
        
        if i in m:
            return m[i]
        
        step_1 = cost[i] + self.climb(i+1, cost, m)
        step_2 = cost[i] + self.climb(i+2, cost, m)
        m[i] = min(step_1, step_2)

        return m[i]