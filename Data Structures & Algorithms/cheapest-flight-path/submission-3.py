class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        INF = float("inf")
        adj_list = defaultdict(list)
        dist = [[INF] * (k + 5) for _ in range(n)]
        for u, v, p in flights:
            adj_list[u].append((v, p))
        
        minHeap = [(0, src, -1)]
        dist[src][0] = 0
        while minHeap:
            p, v, d = heapq.heappop(minHeap)
            print(p, v, k, d)
            if v == dst:
                return p
            if d == k or dist[v][d+1] < p:
                continue
            for v1, p1 in adj_list[v]:
                next_p = p + p1
                next_d = d + 1
                if dist[v1][next_d+1] > next_p:
                    dist[v1][next_d+1] = next_p
                    heapq.heappush(minHeap, (next_p, v1, next_d))
        
        return -1