# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s) - 1
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while l < r:
            if s[l] in v and s[r] in v:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] not in v:
                l += 1

            elif s[r] not in v:
                r -= 1
        return ''.join(s)
