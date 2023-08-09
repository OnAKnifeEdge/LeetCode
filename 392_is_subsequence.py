# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = len(s)
        r = len(t)
        pl = pr = 0
        while pl < l and pr < r:
            if s[pl] == t[pr]:
                pl = pl + 1
            pr = pr + 1
        return pl == l
