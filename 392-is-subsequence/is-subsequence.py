class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        def recurse(s_idx, t_idx):
            if s_idx == m:
                return True
            if t_idx == n:
                return False
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1

            return recurse(s_idx, t_idx)

        return recurse(0, 0)
