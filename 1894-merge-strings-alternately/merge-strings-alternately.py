class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        max_length = max(m, n)
        result = []
        for i in range(max_length):
            if i < m:
                result.append(word1[i])
            if i < n:
                result.append(word2[i])
        return ''.join(result)
