class Solution:
    def reorganizeString(self, s: str) -> str:
        #  > ceil(len(s)/2)
        n = len(s)
        counter = Counter(s)
        c, max_count = counter.most_common(1)[0]

        if max_count > ceil(n / 2):
            # impossible to match
            return ""

        result = [''] * n

        idx = 0

        while counter[c] > 0:
            result[idx] = c
            idx += 2
            counter[c] -= 1

        for letter, count in counter.items():
            while count > 0:
                if idx >= n:
                    idx = 1
                result[idx] = letter
                idx += 2
                count -= 1

        return "".join(result)
