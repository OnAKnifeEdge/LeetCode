class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        less = 0
        equal = 0
        for num in nums:
            if num < pivot:
                less += 1
            elif num == pivot:
                equal += 1
        result = [0] * n
        a = 0
        b = less
        c = less + equal
        for num in nums:
            if num < pivot:
                result[a] = num
                a += 1
            elif num == pivot:
                result[b] = num
                b += 1
            else:
                result[c] = num
                c += 1
        return result
