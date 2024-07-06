class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # make sure nums1 is the smaller one
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m

        half = (m + n + 1) // 2
        # 如果多一个，给 left

        is_even = (m + n) % 2 == 0

        while lo <= hi:
            cut1 = (lo + hi) // 2
            cut2 = half - cut1  # ensures cut1 + cut2 = half

            # nums1: [... left1 | right1 ...] m
            # nums2: [... left2 | right2 ...] n
            # left1 <= right2 and left2 <= right1

            left1 = nums1[cut1 - 1] if cut1 > 0 else float("-inf")
            left2 = nums2[cut2 - 1] if cut2 > 0 else float("-inf")

            right1 = nums1[cut1] if cut1 < m else float("inf")
            right2 = nums2[cut2] if cut2 < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                # found the case
                if is_even:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                hi = cut1 - 1
            else:
                lo = cut1 + 1


