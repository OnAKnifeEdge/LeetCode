class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = defaultdict(int)
        for a, b in zip(s, t):
            counter[a] += 1
            counter[b] -= 1
        for v in counter.values():
            if v != 0:
                return False
        return True
