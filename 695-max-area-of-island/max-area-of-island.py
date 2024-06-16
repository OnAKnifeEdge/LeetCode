class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def is_valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c):
            if not is_valid(r, c):
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        return max(dfs(r, c) for r in range(ROWS) for c in range(COLS))
