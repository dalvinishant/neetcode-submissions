class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums)]
        res = []
        i = 0
        while len(nums) >= i+k:
            window = nums[i:i+k]
            if not window:
                break
            res.append(max(window))
            i+=1
        
        return res
