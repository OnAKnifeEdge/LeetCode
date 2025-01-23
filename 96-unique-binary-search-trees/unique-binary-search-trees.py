class Solution:
    def numTrees(self, n: int) -> int:

        @cache
        def count(lo, hi):
            if lo > hi:
                return 1
            result = 0
            for i in range(lo, hi + 1):
                result += count(i + 1, hi) * count(lo, i - 1)
            return result
        return count(1, n)