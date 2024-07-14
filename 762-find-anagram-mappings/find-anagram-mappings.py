class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i, num in enumerate(nums2):
            d[num] = i
        result = []
        for num in nums1:
            result.append(d[num])
        return result
