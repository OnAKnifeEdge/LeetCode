class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ld = defaultdict(int)
        for i, c in enumerate(order):
            ld[c] = i
        return "".join(sorted(s, key=lambda x: ld[x]))
