class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        # dp[i][j] means min # of operations to convert word1[0..i) to word2[0..j)
        
        for i in range(1, l1 + 1):
            dp[i][0] = i # 第一列

        for j in range(1, l2 + 1):
            dp[0][j] = j # 第一行

        for r in range(1, l1 + 1):
            for c in range(1, l2 + 1):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    insert_case = dp[r - 1][c]
                    delete_case = dp[r][c - 1]
                    replace_case = dp[r - 1][c - 1]
                    dp[r][c] = 1 + min(insert_case, delete_case, replace_case)
        return dp[l1][l2]
