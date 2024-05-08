class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
        if not s:
            return 0
        insertions = 0
        required_closings = 0
        for c in s:
            if c == "(":
                required_closings += 1
            elif c == ")":
                required_closings -= 1
                if required_closings == -1:
                    insertions += 1
                    required_closings = 0
        return insertions + required_closings
