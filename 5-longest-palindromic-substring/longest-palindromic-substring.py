class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#" + "#".join(s) + "#"
        n = len(t)
        center, right = 0, 0
        p = [0] * n  # p[i] means radius of palindrome centered at i
        for i in range(n):
            mirror = 2 * center - i
            if i < right:
                p[i] = min(right - i, p[mirror])

            # Attempt to expand palindrome centered at i
            start, end = i - (1 + p[i]), i + (1 + p[i])
            while end < n and start >= 0 and t[start] == t[end]:
                p[i] += 1
                start -= 1
                end += 1

            if i + p[i] > right:
                center, right = i, i + p[i]

        longest, center_idx = max((n, i) for i, n in enumerate(p))
        start = (center_idx - longest) // 2
        return s[start:start+longest]
