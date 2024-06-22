class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if i < 0 or j < 0 or i == ROWS or j == COLS:
                return 0
            # skip water or visited
            if grid[i][j] != 1:
                return 0
            # mark land as visited:
            grid[i][j] = -1
            area = 1
            for dx, dy in DIRECTIONS:
                area += dfs(i + dx, j + dy)
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area
