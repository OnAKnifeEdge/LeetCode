class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        ROWS, COLS = len(s1), len(s2)
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for c in reversed(range(COLS)):
            dp[ROWS][c] = dp[ROWS][c + 1] + ord(s2[c])

        for r in reversed(range(ROWS)):
            dp[r][COLS] = dp[r + 1][COLS] + ord(s1[r])

        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                if s1[r] == s2[c]:
                    dp[r][c] = dp[r + 1][c + 1]

                else:
                    deleteFromS1 = dp[r + 1][c] + ord(s1[r])
                    deleteFromS2 = dp[r][c + 1] + ord(s2[c])
                    dp[r][c] = min(deleteFromS1, deleteFromS2)

        return dp[0][0]

