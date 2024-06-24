class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.prefix_sum = [0] * n
        for i in range(n):
            # [1, 2, 3]
            # [0, 1, 3, 6]
            if i == 0:
                self.prefix_sum[i] = w[i]
            else:
                self.prefix_sum[i] = w[i] + self.prefix_sum[i - 1]
        self.random = random.Random()

    def pickIndex(self) -> int:
        target = self.random.randint(1, self.prefix_sum[-1])
        return bisect_left(self.prefix_sum, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
