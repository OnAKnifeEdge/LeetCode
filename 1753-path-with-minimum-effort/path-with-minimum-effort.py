class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        ROWS = len(heights)
        COLS = len(heights[0])
        q = [(0, 0, 0)]  # abs(difference), i, j
        visited = set()

        def get_neighbors(i, j):
            neighbors = []
            for d_x, d_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x, y = i + d_x, j + d_y
                if x < 0 or x >= ROWS or y < 0 or y >= COLS:
                    continue
                neighbors.append((x, y))
            return neighbors

        while q:
            effort, i, j = heappop(q)
            if (i, j) in visited:
                continue
            if (i, j) == (ROWS - 1, COLS - 1):
                return effort
            visited.add((i, j))
            neighbors = get_neighbors(i, j)
            for x, y in neighbors:
                if (x, y) in visited:
                    continue
                new_effort = max(effort, abs(heights[x][y] - heights[i][j]))
                heappush(q, (new_effort, x, y))

        return -1
