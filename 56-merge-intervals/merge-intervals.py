class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort(key=lambda x: (x[0], -x[1]))

        merged = []
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            left, right = intervals[i]

            if left <= end:
                end = max(end, right)
            else:
                merged.append((start, end))
                start, end = left, right

        merged.append((start, end))

        return merged
