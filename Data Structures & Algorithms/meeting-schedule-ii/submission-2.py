"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap = []
        maxRooms = 0

        for interval in intervals:
            # lazily close all meeting rooms by this start time
            while len(heap) and heap[0] <= interval.start:
                heapq.heappop(heap)
            
            # accomodate meeting room for the current
            heapq.heappush(heap, interval.end)

            # count max parallel rooms
            maxRooms = max(maxRooms, len(heap))
        
        return maxRooms

            