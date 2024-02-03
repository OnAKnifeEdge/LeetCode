# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

class Solution:
    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        def valid(k):
            d1, m1 = divmod(len1, k)
            d2, m2 = divmod(len2, k)
            if m1 or m2:
                return False
            base = str1[:k]
            return str1 == d1 * base and str2 == d2 * base

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
