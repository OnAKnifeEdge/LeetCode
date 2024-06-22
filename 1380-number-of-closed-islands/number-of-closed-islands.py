class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return
            # if it is water or visited
            if grid[i][j] != 0:
                return
            # mark as visited
            grid[i][j] = -1
            for dx, dy in DIRECTIONS:
                x, y = i + dx, j + dy
                dfs(x, y)

        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS - 1)

        for j in range(COLS):
            dfs(0, j)
            dfs(ROWS - 1, j)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1

        return count
