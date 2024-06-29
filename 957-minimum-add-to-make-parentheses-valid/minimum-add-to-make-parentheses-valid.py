class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        insertions = 0
        need_right = 0
        for c in s:
            if c == "(":
                need_right += 1
            elif c == ")":
                need_right -= 1
                if need_right == -1:
                    need_right = 0
                    insertions += 1
        return insertions + need_right
