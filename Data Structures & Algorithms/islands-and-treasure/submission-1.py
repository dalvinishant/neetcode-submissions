
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        
        while q:
            i, j, d = q.pop(0)
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                continue
            if grid[i][j] == -1:
                continue
            if grid[i][j] < d:
                continue
            grid[i][j] = min(grid[i][j], d)
            q.append((i+1, j, d+1))
            q.append((i-1, j, d+1))
            q.append((i, j+1, d+1))
            q.append((i, j-1, d+1))
        
