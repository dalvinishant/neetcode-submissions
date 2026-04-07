class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = nums[0]
        currMax = nums[0]
        maxProd = nums[0]
        for i in range(1, len(nums)):
            t = max(nums[i], nums[i]*currMax, nums[i]*currMin)
            currMin = min(nums[i], nums[i]*currMax, nums[i]*currMin)
            currMax = t
            maxProd = max(maxProd, currMax)
        return maxProd