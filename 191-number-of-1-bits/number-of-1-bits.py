class Solution(object):
    def hammingWeight(self, n):
        s = 0
        while n:
            n = n & (n - 1)
            s += 1
        return s