class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        n = len(edges)
        indegree = [0] * (n+1)

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        q = []
        for i in range(1, n+1):
            if indegree[i] == 1:
                q.append(i)
        
        while q:
            node = q.pop(0)
            indegree[node] -= 1
            for n in adj_list[node]:
                indegree[n] -= 1
                if indegree[n] == 1:
                    q.append(n)

        for a,b in reversed(edges):
            if indegree[a] == 2 and indegree[b]:
                return [a,b]
        return []


        