class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
        longest = 0
        pairs.sort(key=lambda x: x[1])
        right = float("-inf")
        for start, end in pairs:
            if start > right:
                right = end
                longest += 1

        return longest
