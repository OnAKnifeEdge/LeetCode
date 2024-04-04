class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # https://leetcode.com/problems/ugly-number-iii/solutions/723589/python3-inconsistent-definition-of-ugly-numbers/
        ab = a*b//gcd(a, b)
        bc = b*c//gcd(b, c)
        ca = c*a//gcd(c, a)
        abc = ab*c//gcd(ab, c)
        
        lo, hi = 1, n*min(a, b, c)
        while lo < hi: 
            mid = lo + hi >> 1
            if mid//a + mid//b + mid//c - mid//ab - mid//bc - mid//ca + mid//abc < n: 
                lo = mid + 1
            else: hi = mid 
        return lo 