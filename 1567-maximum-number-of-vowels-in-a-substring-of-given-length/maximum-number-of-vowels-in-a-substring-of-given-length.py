class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        running_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                running_vowels += 1
        max_vowels = running_vowels
        for i in range(k, len(s)):
            if s[i] in vowels:
                running_vowels += 1
            if s[i - k] in vowels:
                running_vowels -= 1
            max_vowels = max(running_vowels, max_vowels)
        return max_vowels


