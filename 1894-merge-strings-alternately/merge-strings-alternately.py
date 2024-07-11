class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = []
        n = len(word1)
        m = len(word2)
        for c1, c2 in zip(word1, word2):
            s.append(c1)
            s.append(c2)

        if n > m:
            s.append(word1[m:])
        else:
            s.append(word2[n:])

        return ''.join(s)
