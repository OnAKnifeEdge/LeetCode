class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dp = [float("inf")] * COLS
        dp[0] = 0

        for i in range(ROWS):
            for j in range(COLS):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]

    def minPathSum_dp(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dp = [[float("inf")] * (COLS) for _ in range(ROWS)]
        dp[0][0] = grid[0][0]

        for i in range(1, ROWS):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, COLS):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, ROWS):
            for j in range(1, COLS):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]
