class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])

        for word in words[1:]:
            word_counter = Counter(word)
            for c in counter:
                counter[c] = min(word_counter[c], counter[c])
        result = []
        for c, freq in counter.items():
            result.extend([c] * freq)
        return result
