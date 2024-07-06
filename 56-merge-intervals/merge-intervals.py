class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: (x[0], -x[1]))
        print(intervals)

        merged = []

        for a, b in intervals:
            if not merged:
                merged.append((a, b))

            start, end = merged[-1]
            if a <= end:
                b = max(b, end)
                merged[-1] = (start, b)

            else:
                merged.append((a, b))

        return merged
