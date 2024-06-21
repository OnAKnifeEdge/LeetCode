class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # sort intervals by end time
        intervals.sort(key=lambda x: [x[1]])
        count = 0  # non overlapping intervals
        earliest_end = float("-inf")
        for start, end in intervals:
            if start >= earliest_end:
                earliest_end = end
                count += 1
        return len(intervals) - count
