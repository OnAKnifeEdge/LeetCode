class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        start, end = intervals[0]

        overlapped = 0

        for i in range(1, n):
            left, right = intervals[i]
            if left <= end and right <= end:
                overlapped += 1
            elif right > end:
                end = right

        return n - overlapped
