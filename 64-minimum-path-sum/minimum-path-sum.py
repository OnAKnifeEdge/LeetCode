class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        result = [[float('inf')] * (COLS + 1) for _ in range(ROWS + 1)]
        result[ROWS - 1][COLS] = 0
        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                result[r][c] = grid[r][c] + min(result[r + 1][c], result[r][c + 1])
        
        return result[0][0]