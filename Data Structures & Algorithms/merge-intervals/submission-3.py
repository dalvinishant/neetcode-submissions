class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        overlapInterval = intervals[0]
        print(intervals)
        for ix in range(1,len(intervals)):

            ni, nj = overlapInterval
            i,j = intervals[ix]
            if nj < i: 
                res.append([ni, nj])
                overlapInterval = [i, j]
            elif ni > j:
                res.append([i,j])
            else:
                overlapInterval = [min(ni, i), max(nj, j)]
        
        res.append(overlapInterval)
        return res
                