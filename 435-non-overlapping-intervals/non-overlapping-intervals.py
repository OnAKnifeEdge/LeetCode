class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # sort intervals by end time
        intervals.sort(key=lambda x: [x[1]])
        result = 0
        earliest_end = float("-inf")
        for start, end in intervals:
            if start >= earliest_end:
                earliest_end = end
            else:
                result += 1
        return result
