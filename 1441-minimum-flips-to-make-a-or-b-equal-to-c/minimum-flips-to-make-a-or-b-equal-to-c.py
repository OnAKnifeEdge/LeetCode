class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = ((a | b) ^ c).bit_count()
        count += (a & b & ((a | b) ^ c)).bit_count()
        return count
