class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        @cache
        def dp(i, j):

            if j == len(p):
                result = i == len(s)
            else:
                first_match = i < len(s) and p[j] in {s[i], "."}
                if j + 1 < len(p) and p[j + 1] == "*":
                    result = dp(i, j + 2) or first_match and dp(i + 1, j)
                else:
                    result = first_match and dp(i + 1, j + 1)
            memo[i, j] = result
            return memo[i, j]

        return dp(0, 0)
