"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ## Sort the array by start time
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                ## Overlap
                return False
        return True


        
