class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        def expand(left, right) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            # When the while loop ends, it implies s[left] != s[right]. 
            # Therefore, we need (right - left + 1)) subtract 2. Return right - left - 1
            return s[left + 1: right]
        result = ""
        for i in range(len(s) - 1):
            odd = expand(i, i)
            even = expand(i, i + 1)
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        return result

        