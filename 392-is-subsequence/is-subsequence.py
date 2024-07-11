class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lookup = defaultdict(list)
        for i, c in enumerate(t):
            lookup[c].append(i)

        i = 0
        for c in s:
            if c not in lookup:
                return False
            idx_list = lookup[c]
            found = bisect_left(idx_list, i)
            if found == len(idx_list):
                return False
            i = idx_list[found] + 1

        return True
