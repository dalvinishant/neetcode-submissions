class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # tickets.sort()
        adj_list = defaultdict(list)
        for source, destination in sorted(tickets)[::-1]:
            adj_list[source].append(destination)
            # adj_list[source].sort()
        
        visited = []
        print(adj_list)
        def dfs(src):
            while adj_list[src]:
                dfs(adj_list[src].pop())
            visited.append(src)

        dfs("JFK")
        return visited[::-1]