import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((v, t))
        
        visited = set()
        minHeap = [(0, k)]
        t = 0

        while minHeap:
            w, v = heapq.heappop(minHeap)
            if v in visited:
                continue
            visited.add(v)
            t = w

            for v1, w1 in adj_list[v]:
                if v1 not in visited:
                    heapq.heappush(minHeap, (w1+w, v1))
        
        return t if len(visited) == n else -1