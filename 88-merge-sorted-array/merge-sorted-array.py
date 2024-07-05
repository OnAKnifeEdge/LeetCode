class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        # nums1 is longer
        i, j = m - 1, n - 1

        for p in reversed(range(m + n)):
            if j < 0:
                break
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1