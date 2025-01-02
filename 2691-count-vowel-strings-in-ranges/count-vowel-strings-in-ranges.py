class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = [0] * len(queries)
        vowels = {"a", "e", "i", "o", "u"}
        prefix_sum = [0] * len(words)
        s = 0

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                s += 1
            prefix_sum[i] = s

        for i, query in enumerate(queries):
            start, end = query
            if start > 0:
                # why
                result[i] = prefix_sum[end] - prefix_sum[start - 1]
            else:
                result[i] = prefix_sum[end]

        return result
