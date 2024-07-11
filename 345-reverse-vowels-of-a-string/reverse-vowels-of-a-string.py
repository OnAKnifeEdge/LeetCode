class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        n = len(s_list)
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        start, end = 0, n - 1
        while start < end:
            if s_list[start] in vowels and s_list[end] in vowels:
                s_list[start], s_list[end] = s_list[end], s_list[start]
                start += 1
                end -= 1
            elif s_list[start] not in vowels:
                start += 1
            elif s_list[end] not in vowels:
                end -= 1
        return "".join(s_list)
