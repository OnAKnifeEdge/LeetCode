from collections import defaultdict

class Solution:
    # https://leetcode.com/problems/permutation-in-string/
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        have = defaultdict(int)
        need = defaultdict(int) # need keeps a count of all the unique characters in t.
        for c in t:
            need[c] += 1
        
        # number of unique characters in t, which need to be present in the desired window.
        required = len(need)
        # keep track of how many unique characters in t are present in the current window in its desired frequency.
        formed = 0
        

        # for window
        left, right = 0, 0

        # for smallerst window
        l, start = float('inf'), 0

        while right < len(s):
            c = s[right]
            if c in need:
                have[c] += 1
                if need[c] == have[c]:
                    formed += 1

            right += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while left < right and formed == required:
                c = s[left]

                # Save the smallest window until now.
                if right - left < l:
                    start = left
                    l = right - left

                if c in need:
                    if have[c] == need[c]:
                        formed -= 1
                    have[c] -= 1


                left += 1
            

        return s[start: start + l] if l != float('inf') else ""