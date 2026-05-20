class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        removals = 0
        print(intervals)
        for i, j in intervals[1:]:
            print((i, j), prevEnd)
            if i >= prevEnd:
                prevEnd = j
            else:
                removals += 1
                prevEnd = min(j, prevEnd)
        
        return removals
