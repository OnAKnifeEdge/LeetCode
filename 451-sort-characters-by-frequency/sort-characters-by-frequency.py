class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = defaultdict(int)
        for c in s:
            frequency[c] += 1

        bucket = [[] for _ in range(len(s) + 1)]
        for v, f in frequency.items():
            bucket[f].append(v)

        result = []

        for f in reversed(range(len(s) + 1)):
            for c in bucket[f]:
                result.append(c * f)
        return "".join(result)
