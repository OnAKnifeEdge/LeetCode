class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = len(nums) // 2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        i, j = 0, 0
        r = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                r.append(left[i])
                i += 1
            else:
                r.append(right[j])
                j += 1
        r.extend(left[i:])
        r.extend(right[j:])
        return r
