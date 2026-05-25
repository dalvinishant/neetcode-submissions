from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(c, n) for n,c in count.items()]
        heapq.heapify(heap)
        k_freq = [n for _,n in heapq.nlargest(k, heap)]
        return k_freq
            