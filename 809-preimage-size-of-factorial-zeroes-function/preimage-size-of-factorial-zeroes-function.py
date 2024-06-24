class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        l, r = 0, 2**63 - 1
        while l < r:
            mid = (l + r) // 2
            if self.trailingZeroes(mid) < K:
                l = mid + 1
            else:
                r = mid
        return 5 - l % 5 if self.trailingZeroes(l) == K else 0

    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        while n > 0:
            n //= 5
            zero_count += n
        return zero_count
