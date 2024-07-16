class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#" + "#".join(s) + "#"
        n = len(t)
        center, right = 0, 0
        dp = [0] * n  # dp[i] means radius of palindrome centered at i
        for i in range(n):
            mirror = 2 * center - i
            if i < right:
                dp[i] = min(right - i, dp[mirror])

            # Attempt to expand palindrome centered at i
            start, end = i - (1 + dp[i]), i + (1 + dp[i])
            while end < n and start >= 0 and t[start] == t[end]:
                dp[i] += 1
                start -= 1
                end += 1

            if i + dp[i] > right:
                center, right = i, i + dp[i]

        longest, center_idx = max((n, i) for i, n in enumerate(dp))
        start = (center_idx - longest) // 2
        return s[start:start+longest]
