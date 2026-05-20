"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda i: i.start)
        print([(i.start, i.end) for i in intervals])
        overlaping = intervals[0]
        for i in intervals[1:]:
            if overlaping.end > i.start:
                return False
            else:
                if overlaping.end < i.end:
                    overlaping = i
        
        return True
