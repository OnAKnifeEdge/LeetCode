class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lcs_length = self.lcs(word1, word2)
        return len(word1) - lcs_length + len(word2) - lcs_length

    def lcs(self, word1, word2):

        dp = [0] * (len(word1) + 1)
        for i in reversed(range(len(word2))):
            prev_dp = dp[:]
            for j in reversed(range(len(word1))):
                if word2[i] == word1[j]:
                    dp[j] = prev_dp[j + 1] + 1
                else:
                    dp[j] = max(prev_dp[j], dp[j + 1])
        return dp[0]


