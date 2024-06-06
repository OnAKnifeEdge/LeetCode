class Solution:

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [float("inf") for _ in range(COLS)]

        dp = matrix[0]

        for i in range(1, ROWS):
            prev_dp = dp[:]
            for j in range(COLS):
                if j == 0:
                    dp[j] = min(prev_dp[j], prev_dp[j + 1]) + matrix[i][j]
                elif j == COLS - 1:
                    dp[j] = min(prev_dp[j], prev_dp[j - 1]) + matrix[i][j]
                else:
                    dp[j] = min(prev_dp[j], prev_dp[j - 1], prev_dp[j + 1]) + matrix[i][j]

        return min(dp)

    def minFallingPathSum_bottomup(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[float("inf") for _ in range(COLS)] for _ in range(ROWS)]

        dp[0] = matrix[0]

        for i in range(1, ROWS):
            for j in range(COLS):
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                elif j == COLS - 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + matrix[i][j]
                else:
                    dp[i][j] = (
                        min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1])
                        + matrix[i][j]
                    )

        return min(dp[ROWS - 1])

    def minFallingPathSum_bottomup(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[float("inf") for _ in range(COLS)] for _ in range(ROWS)]

        dp[0] = matrix[0]

        for i in range(1, ROWS):
            for j in range(COLS):
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                elif j == COLS - 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + matrix[i][j]
                else:
                    dp[i][j] = (
                        min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1])
                        + matrix[i][j]
                    )

        return min(dp[ROWS - 1])

    def minFallingPathSum_topdown(self, matrix: List[List[int]]) -> int:
        # 对于 matrix[i][j]
        # 只有可能从 matrix[i-1][j], matrix[i-1][j-1], matrix[i-1][j+1] 这三个位置掉下来

        @cache
        def dp(i, j):
            if j < 0 or j == len(matrix):
                return float("inf")

            if i == 0:
                return matrix[i][j]

            return min(dp(i - 1, j), dp(i - 1, j - 1), dp(i - 1, j + 1)) + matrix[i][j]

        result = float("inf")
        for j in range(len(matrix)):
            s = dp(len(matrix) - 1, j)
            result = min(result, s)

        return result
