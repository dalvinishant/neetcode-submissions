
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        
        while q:
            i, j, d = q.pop(0)
            self.calculateDistance(i, j, grid, d, q)

    def calculateDistance(self, i, j, grid, dist, q):
        if i<0 or i>= len(grid) or j<0 or j >=len(grid[0]) or grid[i][j] == -1 or grid[i][j] < dist:
            return
        grid[i][j] = dist
        q.append((i+1, j, dist+1))
        q.append((i, j+1, dist+1))
        q.append((i-1, j, dist+1))
        q.append((i, j-1, dist+1))