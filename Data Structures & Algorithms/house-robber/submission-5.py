class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return max(self.robHouse(0, nums, {}), self.robHouse(1, nums, {}))
    
    def robHouse(self, i, nums, mem):
        
        if i >= len(nums):
            return 0
        
        if i in mem:
            return mem[i]
        
        max_rob = nums[i] + max(self.robHouse(i+2, nums, mem), self.robHouse(i+3, nums, mem))

        mem[i] = max_rob

        return max_rob
        

