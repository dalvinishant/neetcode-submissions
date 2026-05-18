class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)
        
        visited = set()
        comp = 0
        for i in range(n):
            if i in visited:
                continue
            
            self.dfs(i, adj_list, visited)
            comp += 1
        
        return comp
    
    def dfs(self, node, edges, visited):
        if node in visited: 
            return 
        
        visited.add(node)

        adj_list = edges[node]
        for n in adj_list:
            self.dfs(n, edges, visited)

        

