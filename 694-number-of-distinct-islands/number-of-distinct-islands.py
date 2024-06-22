class Solution:
    """
    1, 1, 0
    0, 1, 1
    0, 0, 0
    1, 1, 1
    0, 1, 0

    R -> D -> R

    有撤回了话：
    R -> D -> R -> E -> E -> E

    R -> D -> E -> R -> E -> E
    """

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = {"u": (-1, 0), "d": (1, 0), "r": (0, 1), "l": (0, -1)}
        islands = set()

        def dfs(i, j, path, direction):
            if i < 0 or j < 0 or i == ROWS or j == COLS:
                return
            # skip water or visited land
            if grid[i][j] != 1:
                return
            # mark visited
            grid[i][j] = -1
            # Add direction to path
            path.append(direction)
            for d, (dx, dy) in DIRECTIONS.items():
                dfs(i + dx, j + dy, path, d)
            path.append("e")  # ?

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, path, "s")  # ?
                    islands.add("".join(path))
        print(islands)
        return len(islands)
