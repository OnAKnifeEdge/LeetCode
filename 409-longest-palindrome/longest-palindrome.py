class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = set()
        longest = 0

        for c in s:
            if c in chars:
                chars.remove(c)
                longest += 2
            else:
                chars.add(c)

        if chars:
            longest += 1

        return longest
