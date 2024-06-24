class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        i = 5
        while n >= i:
            zero_count += n // i
            i *= 5
        return zero_count
