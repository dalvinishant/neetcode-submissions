class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.reach(0, 0, triangle, {})
    
    def reach(self, i, j, nums, mem):
        if i >= len(nums):
            return 0
        
        if (i,j) in mem:
            return mem[(i, j)]

        mem[(i, j)] = nums[i][j] + min(self.reach(i+1, j, nums, mem), self.reach(i+1, j+1, nums, mem))

        return mem[(i, j)]