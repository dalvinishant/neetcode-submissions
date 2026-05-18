class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(set)
        for s, t in edges:
            adj_list[s].add(t)
            adj_list[t].add(s)

        visited = set()
        if not self.dfs(0, adj_list, visited, -1):
            return False
        # print('final : ', n, visited)
        return n == len(visited)
        
    def dfs(self, node: int, edges: dict[int: set], visited: set(int), par) -> bool:
        # print(node, edges, visited)
        if node in visited:
            return False

        visited.add(node)

        if node not in edges:
            return True
        
        adj_list = edges[node]

        for n in adj_list:
            if n == par:
                continue
            if not self.dfs(n, edges, visited, node):
                return False
            
        return True