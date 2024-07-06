class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False

        r = 0

        while x > r:
            last_digit = x % 10
            r = r * 10 + last_digit
            x //= 10

        return x == r or x == r // 10
