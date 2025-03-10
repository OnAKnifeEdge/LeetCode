# class FenwickTree:

#     def __init__(self, size):
#         self.size = size
#         self.tree = [0] * (size + 1)

#     def _lsb(self, i):
#         return i & (-i)

#     def update(self, i, value):
#         while i <= self.size:
#             self.tree[i] += value
#             i += self._lsb(i)

#     def query(self, i):
#         total = 0
#         while i > 0:
#             total += self.tree[i]
#             i -= self._lsb(i)


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:

        max_flipped = 0  # Track the maximum flipped index so far
        count = 0  # Count of prefix-aligned moments

        for i, flip in enumerate(flips, start=1):  # Step starts from 1
            max_flipped = max(max_flipped, flip)
            if max_flipped == i:  # Check if prefix is aligned
                count += 1

        return count
