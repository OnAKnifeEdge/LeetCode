class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return
            # if it is water or visited
            if grid[i][j] != "1":
                return
            # mark as visited
            grid[i][j] = "-1"
            for dx, dy in DIRECTIONS:
                di = i + dx
                dj = j + dy
                dfs(di, dj)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
