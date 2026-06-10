class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj_list = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append((dist, j))
                adj_list[j].append((dist, i))

        v = set()
        minH = [[0, 0]]
        res = 0
        while len(v) < n:
            cost, i = heapq.heappop(minH)
            if i in v:
                continue
            res += cost
            v.add(i)
            for nei_cost, nei in adj_list[i]:
                if nei not in v:
                    heapq.heappush(minH, [nei_cost, nei])

        return res