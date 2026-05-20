class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for ix in range(len(intervals)):
            (i,j) = intervals[ix]
            ni, nj = newInterval
            if nj < i:
                res.append(newInterval)
                return res + intervals[ix:]
            elif ni > j:
                res.append(intervals[ix])
            else:
                newInterval = [min(ni, i), max(nj, j)]
        
        res.append(newInterval)
        # print(res)
        return res