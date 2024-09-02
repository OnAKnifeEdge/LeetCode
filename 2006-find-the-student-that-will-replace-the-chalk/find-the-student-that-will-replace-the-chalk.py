class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        k = k % s
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c

        return -1
