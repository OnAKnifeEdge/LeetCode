class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] is the longest palindrome sub seq for [i: j + 1]
        # if (s[i] == s[j]):
        # # 它俩一定在最长回文子序列中
        #     dp[i][j] = dp[i + 1][j - 1] + 2;
        # else:
        # # s[i+1..j] 和 s[i..j-1] 谁的回文子序列更长？
        # dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
        # return dp[0][n - 1]
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for r in reversed(range(n)):
            for c in range(r + 1, n):
                if s[r] == s[c]:
                    dp[r][c] = dp[r + 1][c - 1] + 2
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c - 1])
        return dp[0][-1]
