class Solution:
    def minInsertions(self, s: str) -> int:
        # 516 https://leetcode.com/problems/longest-palindromic-subsequence/description/
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for r in reversed(range(n)):
            for c in range(r + 1, n):
                if s[r] == s[c]:
                    dp[r][c] = dp[r + 1][c - 1]
                else:
                    dp[r][c] = min(dp[r + 1][c], dp[r][c - 1]) + 1
        return dp[0][-1]
