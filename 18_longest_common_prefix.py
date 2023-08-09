# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = strs[0]
        for i in range(0, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[0:len(prefix)-1]
                if not prefix:
                    return ''
        return prefix
