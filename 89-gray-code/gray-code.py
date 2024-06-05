class Solution:
    def grayCode(self, n: int) -> List[int]:
        # n = 2
        #  00, 01, 11, 10
        # n = 3
        # 000, 001, 011, 010: add 0 to the front
        # 110, 111, 101, 100: reverse graycode of (n -1) and add 1 to the front

        """
        To generate the sequence for n,
        we take the sequence for (n - 1),
        add 0 to the front of each item in the sequence,
        add 1 to the front of each of the items from the reversed sequence of (n - 1)
        This ensures that all adjacent items differ by exactly one bit,
        and the first and last items also differ by exactly one bit.

        """
        if n == 0:
            return [0]
        sequence = self.grayCode(n - 1)
        return sequence + [(1 << (n - 1)) + x for x in reversed(sequence)]
