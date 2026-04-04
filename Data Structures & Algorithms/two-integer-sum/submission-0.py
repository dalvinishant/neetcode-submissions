class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem_sum = {}
        for i, n in enumerate(nums):
            temp_target = target - n
            if temp_target in rem_sum:
                return [rem_sum[temp_target], i]
            rem_sum[n] = i
        return []