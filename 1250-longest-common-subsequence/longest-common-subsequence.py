class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)
        if m > n:
            m, n = n, m
            text1, text2 = text2, text1

        previous = [0] * (m + 1)

        for c in reversed(range(n)): # loop long text2
            current = [0] * (m + 1)
            for r in reversed(range(m)):
                if text2[c] == text1[r]:
                    current[r] = 1 + previous[r + 1]
                else:
                    current[r] = max(previous[r], current[r + 1])

            previous = current

        return current[0]


        