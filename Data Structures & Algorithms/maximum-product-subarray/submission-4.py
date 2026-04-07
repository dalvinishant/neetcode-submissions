class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = nums[0]
        n = len(nums)
        for i in range(n):
            mul = 1
            for j in range(i, n):
                mul *= nums[j]
                max_p = max(mul, max_p)
        
        return max_p