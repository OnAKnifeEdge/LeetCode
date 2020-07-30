from typing import List


class Solution:

    # https://leetcode.com/problems/minimum-path-sum/
    def min_path_sum(self, grid: List[List[int]]) -> int:
        x = len(grid)
        y = len(grid[0])
        for i in range(1, x):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, y):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, x):
            for j in range(1, y):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]
