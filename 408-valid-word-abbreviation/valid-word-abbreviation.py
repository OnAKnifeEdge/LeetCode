class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        n = len(word)

        while i < n and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            else:
                if i >= len(word):
                    return False
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == n and j == len(abbr)
