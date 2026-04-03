class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        dist = self.minDist(0, 0, grid, memo)
        return dist
    
    def minDist(self, i, j, grid, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]
        
        if i == len(grid) - 1:
            res = grid[i][j] + self.minDist(i, j+1, grid, memo)
        elif j == len(grid[0]) - 1:
            res = grid[i][j] + self.minDist(i+1, j, grid, memo)
        else:
            res = grid[i][j] + min(self.minDist(i+1, j, grid, memo), self.minDist(i, j+1, grid, memo))
        
        memo[(i, j)] = res
        return res