class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        insert_left = 0
        need_right = 0
        for c in s:
            if c == "(":
                need_right += 1
            elif c == ")":
                need_right -= 1
                if need_right == -1:
                    need_right = 0
                    insert_left += 1
        return insert_left + need_right
