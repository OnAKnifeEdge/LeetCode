class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)

        result = []

        for c in order:
            if c in counter and counter[c] > 0:
                result.append(c * counter[c])
                del counter[c]

        for c, f in counter.items():
            result.append(c * f)

        return "".join(result)
