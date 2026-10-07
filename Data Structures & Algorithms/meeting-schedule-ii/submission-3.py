"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = defaultdict(int)
        for interval in intervals:
            count[interval.start] += 1
            count[interval.end] -= 1
        
        curr = res = 0
        for i in sorted(count.keys()): # this is the key
            curr += count[i]
            res = max(res, curr)
        
        return res

            