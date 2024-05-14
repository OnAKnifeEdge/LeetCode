class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for idx, c in enumerate(s):
            if d[c] == 1:
                return idx
        return -1
