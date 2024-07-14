class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n <= 2:
            return n

        # Initialize with the first three values
        a, b, c = 1, 2, 5

        if n == 3:
            return c

        for _ in range(4, n + 1):

            # Shift the values
            a, b, c = b, c, (2 * c + a) % MOD

        return c
