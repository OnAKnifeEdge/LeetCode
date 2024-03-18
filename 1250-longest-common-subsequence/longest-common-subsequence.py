class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # m, n = len(text1), len(text2)
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # # 竖着的是 text1, 横着的是 text2t
        # for r in reversed(range(m)):
        #     for c in reversed(range(n)):
        #         if text1[r] == text2[c]:
        #             dp[r][c] = 1 + dp[r + 1][c + 1]
        #         else:
        #             dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])

        # return dp[0][0]
        
        # space optimaztion
        
        # text1 短， text2 长

        m, n = len(text1), len(text2)

        if n < m:
            text1, text2 = text2, text1
            m, n = n, m

        previous = [0] * (n + 1) # 给 text1 

        for c in reversed(range(n)):
            current = [0] * (n + 1)
            for r in reversed(range(m)):
                if text2[c] == text1[r]:
                    current[r] = 1 + previous[r + 1]
                else:
                    current[r] = max(previous[r], current[r + 1])
            previous = current

        return previous[0]
