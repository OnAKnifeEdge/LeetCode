class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0]:
            return 0
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        dp[0][0] = 1

        for j in range(1, COLS):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, ROWS):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, ROWS):
            for j in range(1, COLS):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
