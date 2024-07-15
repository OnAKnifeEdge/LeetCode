class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        ROWS, COLS = len(matrix), len(matrix[0])
        # dp = [[float("inf")] * COLS for _ in range(ROWS)]
        # dp[-1] = matrix[-1][:]
        # for i in reversed(range(ROWS - 1)):
        #     for j in range(COLS):
        #         best = dp[i + 1][j]
        #         if j > 0:
        #             best = min(best, dp[i + 1][j - 1])
        #         if j + 1 < COLS:
        #             best = min(best, dp[i + 1][j + 1])
        #         dp[i][j] = best + matrix[i][j]
        # return min(dp[0])

        dp = matrix[-1][:]

        for i in reversed(range(ROWS - 1)):
            new_dp = dp[:]
            for j in range(COLS):
                best = dp[j]
                if j > 0:
                    best = min(best, dp[j - 1])
                if j + 1 < COLS:
                    best = min(best, dp[j + 1])
                new_dp[j] = matrix[i][j] + best
            dp = new_dp

        return min(dp)
