class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: (x[0], -x[1]))

        merged = []
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            a, b = intervals[i]
            if a <= end:
                end = max(b, end)

            else:
                merged.append((start, end))
                start, end = a, b

        merged.append((start, end))

        return merged
