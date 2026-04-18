class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False  # Cannot partition into two equal sums
        
        target = total_sum // 2
        # DP: dp[s] means if we can achieve sum s with a subset
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: empty subset sums to 0
        
        for num in nums:
            # Iterate backwards to avoid using the same number multiple times
            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True
                    if dp[target]:  # Early exit if target is reached
                        return True
                        
        return dp[target]
