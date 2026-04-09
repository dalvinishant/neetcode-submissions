class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = None
        n = len(nums)
        i = 0
        while i < n:
            ci = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[ci]:
                nums[i], nums[ci] = nums[ci], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1

        return n+1