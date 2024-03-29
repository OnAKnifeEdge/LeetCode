class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        result = 0
        k = float('-inf')

        for x, y in intervals:
            if x >= k:
                k = y
            else:
                result += 1
        return result
        