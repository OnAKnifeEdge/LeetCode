class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        return sorted(cnt1.keys()) == sorted(cnt2.keys()) and sorted(cnt1.values()) == sorted(cnt2.values())


        