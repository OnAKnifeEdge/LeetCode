class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = [None] * 1001
        for idx, val in nums1:
            d[idx] = val
        for idx, val in nums2:
            if d[idx] is not None:
                d[idx] += val
            else:
                d[idx] = val
        return [[idx, num] for idx, num in enumerate(d) if num is not None]
        