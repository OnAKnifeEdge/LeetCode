from collections import defaultdict
import bisect

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lookup = defaultdict(list)
        for i, c in enumerate(t):
            lookup[c].append(i)

        current_pos = 0
        for char in s:
            if char not in lookup:
                return False
            idx_list = lookup[char]
            found = bisect.bisect_left(idx_list, current_pos)
            if found == len(idx_list):
                return False
            current_pos = idx_list[found] + 1

        return True

# Example usage:
sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))  # Output: True
print(sol.isSubsequence("axc", "ahbgdc"))  # Output: False
