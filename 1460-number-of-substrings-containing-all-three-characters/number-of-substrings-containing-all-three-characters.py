class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_position = [-1] * 3
        total = 0

        for i, c in enumerate(s):
            last_position[ord(c) - ord("a")] = i
            total += 1 + min(last_position)

        return total
