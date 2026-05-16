class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        result = []

        for i in range(rows):
            for j in range(cols):
                # if rows-1 > i > 0 and cols-1 > j > 0:
                #     continue
                self.p, self.a = False, False
                if i == 0 or j == 0:
                    self.p = True
                
                if i == rows-1 or j == cols-1:
                    self.a = True

                if not (self.p and self.a):
                    self.canCrossOcean(set(), i, j, heights, heights[i][j])
                if self.p and self.a:
                    result.append([i,j])
                # break
            # break
        return result
    
    def canCrossOcean(self, v, i, j, heights, prev):
        if i < 0 or j < 0:
            # print('reached p', self.a)
            self.p = True
            return
        
        if i >= len(heights) or j >= len(heights[0]):
            # print('reached at', self.p)
            self.a = True
            return
        
        if (i, j) in v:
            return

        # print(heights[i][j], prev, v, self.p, self.a)
        if heights[i][j] <= prev:
            v.add((i, j))
            # print('going', v)
            self.canCrossOcean(v, i+1, j, heights, heights[i][j])
            self.canCrossOcean(v, i, j+1, heights, heights[i][j])
            self.canCrossOcean(v, i-1, j, heights, heights[i][j])
            self.canCrossOcean(v, i, j-1, heights, heights[i][j])
