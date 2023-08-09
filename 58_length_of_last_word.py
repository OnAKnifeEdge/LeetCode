# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        if s.isspace():
            return 0
        return len(s.split()[-1])
