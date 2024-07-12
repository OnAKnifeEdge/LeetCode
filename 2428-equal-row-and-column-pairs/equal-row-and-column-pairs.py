class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        pairs = 0
        for row in grid:
            d[tuple(row)] += 1

        for col in zip(*grid):
            if d[tuple(col)] > 0:
                pairs += d[tuple(col)]

        return pairs
