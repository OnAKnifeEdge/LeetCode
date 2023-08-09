# https://leetcode.com/problems/isomorphic-strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i, j in zip(s, t):
            if i not in s_dict and j not in t_dict:
                s_dict[i] = j
                t_dict[j] = i
            elif s_dict.get(i) != j or t_dict.get(j) != i:
                return False
        return True
