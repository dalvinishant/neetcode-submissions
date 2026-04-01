class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '1':
                    self.checkAdjoining(i, j, grid)
                    islands += 1

        return islands
    
    def checkAdjoining(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == "1":
            grid[i][j] = '#'
            self.checkAdjoining(i+1, j, grid)
            self.checkAdjoining(i, j+1, grid)
            self.checkAdjoining(i, j-1, grid)
            self.checkAdjoining(i-1, j, grid)
        
        