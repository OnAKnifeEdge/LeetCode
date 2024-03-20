class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)
        if m > n:
            m, n = n, m
            text1, text2 = text2, text1

        previous = [0] * (m + 1)

        for r in reversed(range(n)): # loop long text2
            current = [0] * (m + 1)
            for c in reversed(range(m)):
                if text2[r] == text1[c]:
                    current[c] = 1 + previous[c + 1]
                else:
                    current[c] = max(previous[c], current[c + 1])

            previous = current

        return current[0]


        