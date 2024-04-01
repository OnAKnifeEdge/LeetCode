class Solution:
# https://leetcode.com/problems/merge-two-sorted-lists/description/
# https://leetcode.com/problems/count-primes/description/

    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 1, 1, 1
        product2, product3, product5 = 1, 1, 1
        ugly = [0] * (n + 1)

        i = 1

        while i <= n:
            m = min(product2, product3, product5)
            ugly[i] = m
            i += 1
            if m == product2:
                product2 = 2 * ugly[i2]
                i2 += 1
            if m == product3:
                product3 = 3 * ugly[i3]
                i3 += 1
            if m == product5: 
                product5 = 5 * ugly[i5]
                i5 += 1
        return ugly[n]