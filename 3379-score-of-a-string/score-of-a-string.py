class Solution:
    def scoreOfString(self, s: str) -> int:
        if not s:
            return 0
        return sum(abs(ord(a) - ord(b)) for a, b in pairwise(s))
