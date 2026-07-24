"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda x: x.start)
        # intervals.sort(key=lambda pair: pair[0])
        room = 1
        prevEnd = intervals[0].end
        for iv in intervals[1:]:
            start, end = iv.start, iv.end
            if start>=prevEnd:
                prevEvd = end
            else:
                room += 1
                prevEnd = min(prevEnd, end)
        return room
        