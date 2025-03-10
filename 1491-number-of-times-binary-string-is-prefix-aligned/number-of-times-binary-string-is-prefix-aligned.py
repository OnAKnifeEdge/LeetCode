class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)  # 1-based indexing

    def _lsb(self, i):
        return i & (-i)

    def update(self, i, value):
        while i <= self.size:
            self.tree[i] += value
            i += self._lsb(i)

    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= self._lsb(i)
        return total

class Solution:
    def numTimesAllBlue(self, flips):
        n = len(flips)
        bit = FenwickTree(n)
        count = 0

        for i, flip in enumerate(flips, start=1):  # i is the step number
            bit.update(flip, 1)  # Mark this bit as flipped

            # Check if the number of flipped bits in range [1, i] equals i
            if bit.query(i) == i:
                count += 1

        return count
