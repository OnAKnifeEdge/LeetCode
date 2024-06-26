from collections import defaultdict

class Solution:
    # https://leetcode.com/problems/minimum-window-substring/ 76
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 and not s2:
            return True
        if not s1:
            return True
        if len(s1) > len(s2):
            return False

        have, need = defaultdict(int), defaultdict(int)
        for c in s1:
            need[c] += 1

        left, right = 0, 0

        formed = 0

        while right < len(s2):
            c = s2[right]
            if c in need:
                have[c] += 1
                
                if have[c] == need[c]:
                    formed += 1

            right += 1
            
            if (right - left) >= len(s1):
                if formed == len(need):
                    return True

                d = s2[left]


                if d in need:
                    if have[d] == need[d]:
                        formed -= 1
                    have[d] -= 1

                
                left += 1
        return False

                

        