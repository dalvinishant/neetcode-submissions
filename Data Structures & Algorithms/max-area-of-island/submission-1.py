class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.calculateArea(i, j, grid))
        return max_area
    
    def calculateArea(self, i, j, grid):
        area = 0
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[0] == 0:
            return 0
        if grid[i][j] == 1:
            grid[i][j] = "#"
            area = 1
            area += self.calculateArea(i+1, j, grid)
            area += self.calculateArea(i, j+1, grid)
            area += self.calculateArea(i-1, j, grid)
            area += self.calculateArea(i, j-1, grid)
        return area
