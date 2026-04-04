class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        return max(self.robHouse(0, nums[:-1], {}), self.robHouse(0, nums[1:], {}))
    
    def robHouse(self, i, nums, mem):
        if i >= len(nums):
            return 0
        
        if i in mem:
            return mem[i]
        
        res = max(nums[i] + self.robHouse(i+2, nums, mem), self.robHouse(i+1, nums, mem))

        mem[i] = res
        return res