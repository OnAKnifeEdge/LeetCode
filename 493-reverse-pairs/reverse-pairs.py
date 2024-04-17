class Solution:
    # https://leetcode.com/problems/count-of-smaller-numbers-after-self/
    def reversePairs(self, nums: List[int]) -> int:
        count = 0

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = len(arr) // 2
            left = merge_sort(arr[:pivot])
            right = merge_sort(arr[pivot:])
            return merge(left, right)

        def merge(left, right):
            merged = []
            i, j = 0, 0
            nonlocal count

            while i < len(left) and j < len(right):
                if left[i] <= 2 * right[j]:
                    i += 1
                else:

                    count += len(left) - i
                    j += 1

            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:]) 
            merged.extend(right[j:])  
            return merged

        merge_sort(nums)
        return count 
               