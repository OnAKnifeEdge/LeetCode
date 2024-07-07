class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return [
            c
            for c in set(words[0])
            for _ in range(min(word.count(c) for word in words))
        ]
