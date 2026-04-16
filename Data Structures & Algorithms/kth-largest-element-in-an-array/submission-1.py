import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        i = 0
        heapq.heapify(nums)
        pops = len(nums) - k
        while i <= pops:
            res = heapq.heappop(nums)
            i += 1
        
        return res