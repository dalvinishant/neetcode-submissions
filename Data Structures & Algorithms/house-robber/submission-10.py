class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        dp = [0]*(n+1)
        dp[1] = nums[0]
        dp[2] = nums[1]
        for i in range(3,n+1):
            dp[i] = max(dp[i-1], nums[i-1] + max(dp[i-2], dp[i-3]))
        print(dp)
        return dp[n]
    
    def robHouse(self, i, nums, mem):
        
        if i >= len(nums):
            return 0
        
        if i in mem:
            return mem[i]
        
        max_rob = nums[i] + max(self.robHouse(i+2, nums, mem), self.robHouse(i+3, nums, mem))

        mem[i] = max_rob

        return max_rob
        

