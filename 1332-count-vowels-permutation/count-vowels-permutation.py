class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # a = eCount + iCount + uCount
        # e = aCount + iCount
        # i = eCount + oCount
        # o = iCount
        # u = iCount + oCount

        a_cnt = e_cnt = i_cnt = o_cnt = u_cnt = 1
        MOD = 10**9 + 7

        for j in range(1, n):
            a = (e_cnt + i_cnt + u_cnt) % MOD
            e = (a_cnt + i_cnt) % MOD
            i = (e_cnt + o_cnt) % MOD
            o = i_cnt % MOD
            u = (i_cnt + o_cnt) % MOD

            a_cnt, e_cnt, i_cnt, o_cnt, u_cnt = a, e, i, o, u

        return (a_cnt + e_cnt + i_cnt + o_cnt + u_cnt) % MOD
