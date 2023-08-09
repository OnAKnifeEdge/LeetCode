# There are multiple applications of String Matching, and that's why a lot of research has been done in this field. Multiple algorithms have been devised to solve this problem. Some of the application includes:
#
# Spell Checker
# Plagiarism Detection
# Text Editors
# Spam Filters
# Digital Forensics
# Matching DNA Sequences
# Intrusion Detection
# Search Engines
# Bioinformatics and Cheminformatics
# Information Retrieval System
# Language Syntax Checker

# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle:
            return -1
        if len(needle) > len(haystack):
            return -1
        m = len(needle)
        n = len(haystack)

        for window_start in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start
        return -1
