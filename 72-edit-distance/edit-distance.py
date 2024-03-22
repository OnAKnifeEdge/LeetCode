class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for c in range(len(word2) + 1):
            # 最后一行
            dp[len(word1)][c] = len(word2) - c
        for r in range(len(word1) + 1):
            # 最后一列
            dp[r][len(word2)] = len(word1) - r

        for r in reversed(range(len(word1))):
            for c in reversed(range(len(word2))):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    insert_case = dp[r + 1][c]
                    delete_case = dp[r][c + 1]
                    replace_case = dp[r + 1][c + 1]
                    dp[r][c] = 1 + min(insert_case, delete_case, replace_case)
        return dp[0][0]
