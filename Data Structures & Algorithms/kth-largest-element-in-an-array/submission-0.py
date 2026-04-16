import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k > 0:
            res = -heapq.heappop(nums)
            if k == 1:
                return res
            k-=1