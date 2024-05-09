class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1[i] + nums1[j] > nums2[i] + nums2[j] is equivalent to
        # (nums1[i] - nums2[i]) + (nums1[j] - nums2[j]) > 0
        difference = [a - b for a, b in zip(nums1, nums2)]
        difference.sort()
        count = 0
        i, j = 0, len(difference) - 1
        while i < j:
            if difference[i] + difference[j] > 0:
                count += j - i
                j -= 1
            else:
                i += 1
        return count
