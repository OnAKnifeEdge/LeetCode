class Solution:
    def trailingZeroes(self, n: int) -> int:

        zero_count = 0
        for i in range(5, n + 1, 5):
            power_of_5 = 5
            while i % power_of_5 == 0:
                zero_count += 1
                power_of_5 *= 5

        return zero_count