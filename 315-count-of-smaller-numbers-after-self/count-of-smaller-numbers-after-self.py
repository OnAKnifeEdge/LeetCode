class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        arr = [(v, i) for i, v in enumerate(nums)]

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
            while i < len(left) and j < len(right):

                left_value, left_idx = left[i]
                right_value, _ = right[j]

                if left_value <= right_value:
                    merged.append(left[i])
                    count[left_idx] += j
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            for l in left[i:]:
                _, idx = l
                count[idx] += j
                merged.append(l)
            
            merged.extend(right[j:])

            return merged
        
        merge_sort(arr)
        return count
    


        