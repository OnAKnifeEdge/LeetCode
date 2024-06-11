class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])

        # min health needed reaching i, j
        # Initialize the dp array with infinity along the bottom and right edges
        dp = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[ROWS][COLS - 1] = dp[ROWS - 1][COLS] = 1
        # Base case initialization

        for i in reversed(range(ROWS)):
            for j in reversed(range(COLS)):
                min_health = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(min_health - dungeon[i][j], 1)

        return dp[0][0]
