class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        # dp[i][j] = length of LCS of str1[0:i] and str2[0:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Build LCS table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:  # Characters match, extend LCS
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  # No match, take longer subsequence
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Construct SCS by backtracking
        scs = []
        i, j = n, m
        while i > 0 or j > 0:  # Until we exhaust both strings
            if (
                i > 0 and j > 0 and str1[i - 1] == str2[j - 1]
            ):  # Matching chars, use once
                scs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif j == 0 or (i > 0 and dp[i - 1][j] >= dp[i][j - 1]):  # Take from str1
                scs.append(str1[i - 1])
                i -= 1
            else:  # Take from str2
                scs.append(str2[j - 1])
                j -= 1

        # Reverse since we built it backwards
        return "".join(scs[::-1])
