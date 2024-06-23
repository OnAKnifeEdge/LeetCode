class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[1][1] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i - 1][j - 1] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
