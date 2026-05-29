class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            idx = abs(i) - 1
            if nums[idx] < 0:
                return abs(i)
            nums[idx] *= -1
        return -1