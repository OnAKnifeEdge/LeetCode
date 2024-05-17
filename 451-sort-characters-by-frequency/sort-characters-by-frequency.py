class Solution:
    def frequencySort(self, s: str) -> str:

        # frequency = Counter(s)
        # sorted_chars = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        # return ''.join([char * freq for char, freq in sorted_chars])

        frequency = defaultdict(int)
        for c in s:
            frequency[c] += 1

        buckets = [[] for _ in range(len(s) + 1)]
        for char, freq in frequency.items():
            buckets[freq].extend(char * freq)

        return "".join("".join(bucket) for bucket in reversed(buckets) if bucket)

        # for v, f in frequency.items():
        #     bucket[f].append(v)

        # result = []

        # for f in reversed(range(len(s) + 1)):
        #     for c in bucket[f]:
        #         result.append(c * f)
        # return "".join(result)
