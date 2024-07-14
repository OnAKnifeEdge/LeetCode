class Solution:
    def numTilings(self, n: int) -> int:
        # f(k)=f(k−1)+f(k−2)+2∗p(k−1)
        # p(k)=p(k−1)+f(k−2)
        MOD = 10**9 + 7

        if n <= 2:
            return n

        # p = [0] * (n + 1)
        # f = [0] * (n + 1)


        # f[1] = 1
        # f[2] = 2
        # p[2] = 1

        # for k in range(3, n + 1):
        #     f[k] = (f[k - 1] + f[k - 2] + 2 * p[k - 1]) % MOD
        #     p[k] = (p[k - 1] + f[k - 2]) % MOD

        # return f[n]

        f_two_back = 1
        f = 2
        p = 1
        for k in range(3, n + 1):
            temp = f
            f = (f + f_two_back + 2 * p) % MOD
            p = (p + f_two_back) % MOD
            f_two_back = temp
        return f
