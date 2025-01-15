class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        result = [0] * len(queries)
        vowels = {"a", "e", "i", "o", "u"}
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            word = words[i - 1]
            prefix_sum[i] = prefix_sum[i - 1] + bool(word[0] in vowels and word[-1] in vowels)
        for i, (start, end) in enumerate(queries):
            result[i] = prefix_sum[end + 1] - prefix_sum[start]
        return result