from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # need keeps a count of all the unique characters in t.
        need = defaultdict(int)
        for c in t:
            need[c] = need.get(c, 0) + 1

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(need)

        left, right = 0, 0

        # keep track of how many unique characters in t are present in the current window in its desired frequency.
        formed = 0

        have = defaultdict(int)

        # for result
        l, start = float('inf'), 0

        while right < len(s):
            c = s[right]
            have[c] += 1

            if c in need and need[c] == have[c]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while left <= right and formed == required:
                c = s[left]

                # Save the smallest window until now.
                if right - left + 1 < l:
                    start = left
                    l = right - left + 1

                have[c] -= 1

                if c in need and have[c] < need[c]:
                    formed -= 1

                left += 1
            
            right += 1

        return s[start: start + l] if l != float('inf') else ""