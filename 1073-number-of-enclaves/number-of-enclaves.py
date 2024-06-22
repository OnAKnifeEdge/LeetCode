class Solution:
    # https://leetcode.com/problems/number-of-closed-islands/
    def numEnclaves(self, grid: List[List[int]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if i < 0 or j < 0 or i == ROWS or j == COLS:
                return
            # if water or visited
            if grid[i][j] != 1:
                return
            # mark land as visited
            grid[i][j] = -1
            for dx, dy in DIRECTIONS:
                dfs(i + dx, j + dy)

        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS - 1)

        for j in range(COLS):
            dfs(0, j)
            dfs(ROWS - 1, j)

        for i in range(ROWS):
            for j in range(COLS):
                # if it is land
                if grid[i][j] == 1:
                    count += 1

        return count
