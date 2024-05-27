class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])

        def get_neighbors(x, y):
            r = []
            for delta_x, delta_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                xx, yy = x + delta_x, y + delta_y
                if xx < 0 or yy < 0 or xx >= ROWS or yy >= COLS:
                    continue
                r.append((xx, yy))
            return r

        visited = set()
        q = [(0, 0, 0)]  # difference, i, j

        while q:
            diff, x, y = heappop(q)
            if (x, y) in visited:
                continue
            if x == ROWS - 1 and y == COLS - 1:  # reach destination
                return diff

            visited.add((x, y))

            neighbors = get_neighbors(x, y)
            for xx, yy in neighbors:
                if (xx, yy) in visited:
                    continue
                new_diff = max(diff, abs(heights[x][y] - heights[xx][yy]))
                heappush(q, (new_diff, xx, yy))
