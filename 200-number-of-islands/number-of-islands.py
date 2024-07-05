class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS:
                return
            if grid[i][j] != "1":
                return
            grid[i][j] = "#"
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i + dx, j + dy)

        count = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count
