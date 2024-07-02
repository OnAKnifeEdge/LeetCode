class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # c1 = Counter(nums1)
        # c2 = Counter(nums2)
        # result = []
        # for k, v in c1.items():
        #     count = min(v, c2.get(k, 0))
        #     if count == 0:
        #         continue
        #     result.extend([k] * count)

        # return result
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1

        return result
