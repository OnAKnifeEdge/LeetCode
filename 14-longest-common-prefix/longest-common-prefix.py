class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        for i, c in enumerate(prefix):
            for s in strs[1:]:
                if i == len(s) or s[i] != c:
                    return prefix[:i]
        return prefix
