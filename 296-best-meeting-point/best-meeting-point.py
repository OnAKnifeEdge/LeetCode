class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        rows, cols = [], []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)

        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    cols.append(j)

        def get_distance(points):
            start, end = 0, len(points) - 1
            distance = 0
            while start < end:
                distance += points[end] - points[start]
                start += 1
                end -= 1
            return distance

        return get_distance(rows) + get_distance(cols)
