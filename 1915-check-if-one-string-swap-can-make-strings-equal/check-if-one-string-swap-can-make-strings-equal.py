class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = [(x, y) for x, y in zip(s1, s2) if x != y]
        # not diff: empty
        if not diff:
            return True
        if len(diff) == 2:
            [(a, b), (c, d)] = diff
            if (a, b) == (d, c):
                return True
        return False
