class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        closings_needed = 0
        openings_needed = 0
        for c in s:
            if c == '(':
                closings_needed += 1
            elif c == ')':
                closings_needed -=1
                if closings_needed == -1:
                    closings_needed = 0
                    openings_needed +=1
        return closings_needed + openings_needed

        