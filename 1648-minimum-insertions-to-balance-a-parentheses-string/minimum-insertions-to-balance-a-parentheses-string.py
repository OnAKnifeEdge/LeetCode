class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        right_needed = 0
        for c in s:
            if c == "(":
                right_needed += 2

                if right_needed % 2 == 1:
                    right_needed -= 1
                    insertions += 1

            elif c == ")":
                right_needed -= 1
                if right_needed < 0:
                    insertions += 1
                    right_needed = 1
        return insertions + right_needed
