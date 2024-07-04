class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        nums = 0
        p = 0
        for i, c in enumerate(abbr):
            if c.isdigit():
                if nums == 0 and c == "0":  # Check for leading zeros
                    return False
                nums = nums * 10 + int(c)
            else:
                p += nums
                if p >= len(word) or word[p] != c:
                    return False
                p += 1
                nums = 0

        if nums > 0:
            p += nums

        return p == len(word)
