from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, have = defaultdict(int), defaultdict(int)
        for c in p:
            need[c] += 1

        formed = 0
        left, right = 0, 0 
        result = []

        while right < len(s):
            c = s[right]

            if c in need:
                have[c] += 1
                if have[c] == need[c]:
                    formed += 1
            right += 1

            while right - left >= len(p):
                if formed == len(need):
                    result.append(left)

                d = s[left]

                if d in need:
                    if need[d] == have[d]:
                        formed -= 1
                    have[d] -= 1
                left += 1

        return result
        
        