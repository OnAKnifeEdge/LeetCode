from sortedcontainers import SortedList


class Solution:
    def __init__(self):
        self.intervals = SortedList()

    def insert(self, interval):
        start, end = interval

        # Find the insertion point
        idx = self.intervals.bisect_right((start, float("inf")))

        # Check for merge with previous interval
        if idx > 0 and self.intervals[idx - 1][1] >= start:
            idx -= 1
            start = min(start, self.intervals[idx][0])
            end = max(end, self.intervals[idx][1])
            self.intervals.pop(idx)

        # Merge with subsequent intervals
        while idx < len(self.intervals) and self.intervals[idx][0] <= end:
            end = max(end, self.intervals[idx][1])
            self.intervals.pop(idx)

        # Insert the merged interval
        self.intervals.add((start, end))

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        self.intervals.clear()  # Clear existing intervals
        for interval in intervals:
            self.insert(interval)
        return list(self.intervals)
