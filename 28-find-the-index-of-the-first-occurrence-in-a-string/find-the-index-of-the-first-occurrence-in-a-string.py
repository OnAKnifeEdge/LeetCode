class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, N = len(needle), len(haystack)
        if L == 0:
            return 0
        for i in range(N - L + 1):
            if haystack[i: i + L] == needle:
                return i
        return -1
        