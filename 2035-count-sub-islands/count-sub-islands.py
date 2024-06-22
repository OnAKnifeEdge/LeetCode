class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid1), len(grid1[0])
        count = 0

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i == ROWS or j == COLS:
                return
            # skip water or visited
            if grid[i][j] != 1:
                return

            # mark visited
            grid[i][j] = -1

            for dx, dy in DIRECTIONS:
                dfs(grid, i + dx, j + dy)

        for i in range(ROWS):
            for j in range(COLS):
                # 如果 grid1 里是水，grid2 里是陆地，那么 flood
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(grid2, i, j)

        for i in range(ROWS):
            for j in range(COLS):
                # grid2 里剩下的陆地都是 sub-island
                if grid2[i][j] == 1:
                    dfs(grid2, i, j)
                    count += 1
        return count

        # 1. Traverse grid2 to start DFS on each land cell (1).
        # 2. For each DFS run, check if the entire island found in grid2 can be found in grid1.
        # If any part of this island in grid2 doesn't exist in grid1, it's not a sub-island.
        # 3. Count only those islands in grid2 that are entirely contained in grid1.
