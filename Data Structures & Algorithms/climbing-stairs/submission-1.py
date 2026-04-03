class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb(n, {})

    def climb(self, n, m):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n in m:
            return m[n]
        
        step_1 = self.climb(n-1, m)
        step_2 = self.climb(n-2, m)
        m[n] = step_1+step_2
        return m[n]

