class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()  # ascending
        max_q = [(-val, i) for i, val in enumerate(nums2)]
        heapify(max_q)

        result = [None] * len(nums1)
        left, right = 0, len(nums1) - 1

        while max_q:
            val, i = heappop(max_q)
            max_val = -val  # nums2 里最能打的
            if nums1[right] > max_val:  # nums1 里最能打的能打得过，咱就打！
                result[i] = nums1[right]
                right -= 1
            else:  # 打不过，咱就跑
                result[i] = nums1[left]
                left += 1
        return result
