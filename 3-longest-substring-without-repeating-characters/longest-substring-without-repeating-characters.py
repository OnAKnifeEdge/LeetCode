class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        result = 0
        d = {}

        for right, c in enumerate(s):
            if c in d and d[c] >= left:
                left = d[c] + 1
            result = max(result, right - left + 1)
            d[c] = right

        return result

