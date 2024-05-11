class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for i in reversed(range(len(nums2))):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                d[nums2[i]] = stack[-1]
            else:
                d[nums2[i]] = -1
            stack.append(nums2[i])

        return [d[num] for num in nums1]
