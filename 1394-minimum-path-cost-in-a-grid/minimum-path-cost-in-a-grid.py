class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        for i in reversed(range(ROWS - 1)):  # from last row
            for j in range(COLS):
                grid[i][j] += min(
                    moveCost[grid[i][j]][y] + grid[i + 1][y] for y in range(COLS)
                )

        return min(grid[0])
