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
            # First, let's count the reverse pairs before merging
            while i < len(left) and j < len(right):
                if left[i] <= 2 * right[j]:
                    i += 1
                else:
                    # Every item left in left[] forms a reverse pair with right[j]
                    count += len(left) - i
                    j += 1
            # Reset counters for merging purposes
            i, j = 0, 0
            # Now proceed with actual merge logic
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:]) 
            merged.extend(right[j:])  
            # while i < len(left):
            #     merged.append(left[i])
            #     i += 1
            # while j < len(right):
            #     merged.append(right[j])
            #     j += 1

            return merged

        merge_sort(nums)
        return count 
               