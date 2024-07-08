class Solution:
    MOD = 10**9 + 7
    P = 31
    PMOD = 496822652529863993

    def numberOfWays(self, s: str, t: str, k: int) -> int:
        # https://leetcode.com/problems/string-transformation/
        # 完全看不懂
        n = len(s)

        sHash = 0
        for c in s:
            sHash *= Solution.P
            sHash += ord(c) - ord("a")
            sHash %= Solution.PMOD

        tHash = 0
        for c in t:
            tHash *= Solution.P
            tHash += ord(c) - ord("a")
            tHash %= Solution.PMOD

        # Rabin-Karp
        res = 0
        largestPower = pow(Solution.P, n - 1, Solution.PMOD)
        fk1 = (pow((n - 1), k, Solution.MOD) - (-1) ** k) * pow(
            n, -1, Solution.MOD
        )  # f(k, 1)
        for i, c in enumerate(t):
            # cyclic substring found
            if sHash == tHash:
                res += fk1 if i != 0 else fk1 + (-1) ** k
                res %= Solution.MOD

            # shift t
            intC = ord(c) - ord("a")
            tHash -= largestPower * intC
            tHash = (tHash % Solution.PMOD + Solution.PMOD) % Solution.PMOD

            tHash *= Solution.P
            tHash += intC
            tHash %= Solution.PMOD

        return res


"""
We first find the initial offset needed to transform s into t. This is done by rotating s until it matches t.
If we can't find a match, we return 0 as it's impossible to transform s into t.
We then check if it's possible to reach t in exactly k operations:

If k is less than the initial offset, it's impossible.
If (k - offset) % n == 0, it means we can reach t and then perform additional full rotations to reach exactly k operations.


If it's possible to reach t in k operations, we calculate the number of ways using the formula: (n-1)^((k-offset)/n).

This is because for each full rotation (n operations), we have n-1 choices (we can't choose the suffix of length n as that would not change the string).


We use binary exponentiation (pow_mod function) to efficiently calculate (n-1)^((k-offset)/n) mod MOD.

This solution has a time complexity of O(n + log k) and a space complexity of O(1), making it very efficient even for large inputs.
"""
