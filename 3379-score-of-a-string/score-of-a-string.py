class Solution:
    def scoreOfString(self, s: str) -> int:
        if not s:
            return 0
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))
        return score
