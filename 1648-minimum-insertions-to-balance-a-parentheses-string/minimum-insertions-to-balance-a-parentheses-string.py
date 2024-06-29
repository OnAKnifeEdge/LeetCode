class Solution:
    def minInsertions(self, s: str) -> int:
        inserted_left = 0
        right_needed = 0
        for c in s:
            if c == "(":
                right_needed += 2

                if right_needed % 2 == 1:
                    right_needed -= 1
                    inserted_left += 1

            elif c == ")":
                right_needed -= 1
                if right_needed < 0:
                    inserted_left += 1
                    right_needed = 1
        return inserted_left + right_needed
