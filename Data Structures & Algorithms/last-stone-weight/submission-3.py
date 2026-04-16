import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        if len(stones) < 2:
            return abs(stones[0])

        if len(stones) < 3:
            x, y = stones[0], stones[1]
            return abs(x-y)

        while len(stones) > 1:
            x, y = heapq.heappop(stones) * - 1, heapq.heappop(stones) * -1
            if x == y:
                continue
            
            heapq.heappush(stones, abs(x-y)*-1)

        return stones[0]*-1 if stones else 0