class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.sumWays(0, 0, target, nums, {})
    
    def sumWays(self, i, c_s, t, n, mem):
        if i == len(n):
            if c_s == t:
                return 1
            return 0
        if (i, c_s) in mem:
            return mem[(i, c_s)]
        pos = self.sumWays(i+1, c_s + n[i], t, n, mem)
        neg = self.sumWays(i+1, c_s - n[i], t, n, mem)
        mem[(i, c_s)] = pos+neg
        return pos+neg