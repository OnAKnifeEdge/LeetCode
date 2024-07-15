class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[float("inf")] * COLS for _ in range(ROWS)]
        dp[-1] = matrix[-1]
        for i in reversed(range(ROWS - 1)):
            for j in range(COLS):
                group = [dp[i + 1][j]]
                if j > 0:
                    group.append(dp[i + 1][j - 1])
                if j + 1 < COLS:
                    group.append(dp[i + 1][j + 1])
                dp[i][j] = min(group) + matrix[i][j]
        return min(dp[0])
