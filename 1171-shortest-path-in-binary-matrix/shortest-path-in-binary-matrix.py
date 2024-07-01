class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] or grid[-1][-1]:
            return -1
        source = (0, 0)
        destination = (ROWS - 1, COLS - 1)

        def get_neighbors(i, j):
            neighbors = []
            for row_offset in [-1, 0, 1]:
                for col_offset in [-1, 0, 1]:
                    if row_offset == 0 and col_offset == 0:
                        continue
                    x, y = i + row_offset, j + col_offset
                    if 0 <= x < ROWS and 0 <= y < COLS and not grid[x][y]:
                        neighbors.append((x, y))
            return neighbors

        visited = {source}
        q = deque([source])
        clear_path = 1
        while q:
            n = len(q)

            for _ in range(n):
                i, j = q.popleft()
                if (i, j) == destination:
                    return clear_path

                for x, y in get_neighbors(i, j):
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    q.append((x, y))

            clear_path += 1

        return -1
