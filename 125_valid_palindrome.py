# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def is_palindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i = i + 1
            while i < j and not s[j].isalnum():
                j = j - 1
            if s[i].lower() != s[j].lower():
                return False
            i = i + 1
            j = j - 1
        return True

    def is_palindrome_2(self, s: str) -> bool:
        s = [c for c in s.lower() if c.isalnum()]
        return all(s[i] == s[~i] for i in range(len(s) // 2))
