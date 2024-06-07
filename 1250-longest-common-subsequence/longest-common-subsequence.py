class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # Top Down Approach
        # @cache
        # def dp(i, j):  # s[i:], s[j:] -> LCS
        #     if i == len(text1) or j == len(text2):
        #         return 0
        #     if text1[i] == text2[j]:
        #         return dp(i + 1, j + 1) + 1
        #     else:
        #         return max(dp(i + 1, j), dp(i, j + 1))

        # return dp(0, 0)

        # Bottom Up Approach

        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for i in reversed(range(len(text2))):
            for j in reversed(range(len(text1))):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                    
        return dp[0][0]
