class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = [0] * len(w)
        for i, num in enumerate(w):
            if i == 0:
                self.prefix_sum[0] = num
            else:
                self.prefix_sum[i] = num + self.prefix_sum[i - 1]

    def pickIndex(self) -> int:
        target = random.random() * self.prefix_sum[-1]
        return bisect_left(self.prefix_sum, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
