class Solution:
    def minInsertions(self, s: str) -> int:
        if not s:
            return 0
        insertions = 0
        required_closings = 0
        for c in s:
            if c == "(":
                required_closings += 2
                if required_closings % 2 == 1:
                    insertions += 1
                    required_closings -= 1
            elif c == ")":
                required_closings -= 1
                if required_closings == -1:
                    insertions += 1
                    required_closings = 1
        return insertions + required_closings
