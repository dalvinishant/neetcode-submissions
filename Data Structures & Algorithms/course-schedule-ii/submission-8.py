class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = {}
        for c, p in prerequisites:
            if c not in edges:
                edges[c] = [p]
            else:
                edges[c].append(p)
        
        res = []
        visited = set()

        for i in range(numCourses):
            if i not in edges and i not in visited:
                res.append(i)
                visited.add(i)
            else:
                if not self.dfs(i, edges, visited, set(), res):
                    return []
        return res
    
    def dfs(self, node, edges, visited, trace, res):
        # print(node, visited, trace, res)
        if node in visited:
            # print('return since visited')
            return True
        
        if node in trace:
            # print('cycle detected')
            return False
        
        if node not in edges:
            visited.add(node)
            res.append(node)
            # print('no edges', res)
            return True
        
        adj_nodes = edges[node]
        trace.add(node)

        for n in adj_nodes:
            if not self.dfs(n, edges, visited, trace, res):
                return False
        
        visited.add(node)
        res.append(node)
        # print(node, res)
        return True


