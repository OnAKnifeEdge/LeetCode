class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        k %= R * C

        vals = list(itertools.chain(*grid))
        vals = iter(vals[-k:] + vals[:-k])

        return [[next(vals) for c in range(C)] for r in range(R)]
