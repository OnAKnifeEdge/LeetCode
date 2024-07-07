class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        y = 0
        while x:
            x, digit = divmod(x, 10)
            y = y * 10 + digit
            if y >= (2 << 31 - 1):
                return 0
        return -y if is_negative else y
