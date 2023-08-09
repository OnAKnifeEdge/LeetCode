# https://leetcode.com/problems/ransom-note
import collections


class Solution:
    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        if not magazine:
            return False
        if not ransomNote:
            return True
        if len(magazine) < len(ransomNote):
            return False
        ransom_dict = {}
        magazine_dict = {}
        for r in ransomNote:
            ransom_dict[r] = ransom_dict.get(r, 0) + 1
        for m in magazine:
            magazine_dict[m] = magazine_dict.get(m, 0) + 1
        for k, v in ransom_dict.items():
            if magazine_dict.get(k, 0) < v:
                return False
        return True

    def can_construct_2(self, ransomNote: str, magazine: str) -> bool:
        if not magazine:
            return False
        if not ransomNote:
            return True
        if len(magazine) < len(ransomNote):
            return False
        magazine_counts = collections.Counter(magazine)
        for r in ransomNote:
            if magazine_counts.get(r, 0) <= 0:
                return False
            magazine_counts[r] = magazine_counts[r] - 1
        return True
