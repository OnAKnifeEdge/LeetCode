class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        maxq = [(-val, i) for i, val in enumerate(nums2)]
        heapify(maxq)

        left, right = 0, len(nums1) - 1
        result = [0] * len(nums1)

        while maxq:
            val, i = heappop(maxq)
            max_val = - val

            if max_val < nums1[right]: # 打得过，咱就打
                result[i] = nums1[right]
                right -= 1
            else: # 打不过，咱就跑
                result[i] = nums1[left]
                left += 1
        
        return result