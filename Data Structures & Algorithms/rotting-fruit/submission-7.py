class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        max_depth = 0
        max_rott = 0
        fresh = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    max_rott -= 1
                if grid[i][j] == 1:
                    fresh+=1
        if not q and not fresh:
            return 0
        while q:
            i, j, depth = q.pop(0)
            c_count = self.rottOranges(i, j, depth, q, grid)
            if c_count:
                max_rott += c_count
                max_depth = max(max_depth, depth)
        return max_depth if max_rott - fresh == 0 else -1

        
    def rottOranges(self, i, j, d, q, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0 or grid[i][j] == "X":
            return 0
        grid[i][j] = "X"
        q.append((i+1, j, d+1))
        q.append((i, j+1, d+1))
        q.append((i, j-1, d+1))
        q.append((i-1, j, d+1))
        return 1