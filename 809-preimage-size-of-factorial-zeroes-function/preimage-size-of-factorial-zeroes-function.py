class Solution:
    def preimageSizeFZF(self, k: int) -> int:

        def atMost_k(k: int) -> int:
            left, right = 0, 5 * k + 4
            while left <= right:
                mid = (left + right) // 2
                count = self.trailingZeroes(mid)  # Use extracted function
                if count <= k:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        return atMost_k(k) - atMost_k(k - 1)

    def trailingZeroes(self, n: int) -> int:
        """Calculates the number of trailing zeroes in the factorial of n."""
        zeroes = 0
        while n > 0:
            n //= 5
            zeroes += n
        return zeroes
