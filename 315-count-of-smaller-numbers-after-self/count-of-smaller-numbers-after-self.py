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


        # The crucial part where the logic for counting smaller numbers is implemented. 
        # As left and right halves are merged, for each element in left that is placed into the merged list, 
        # the number of elements already placed from right indicates how many smaller elements there are to the right.
        #  This number is recorded in the count array using the original indices stored alongside each number.

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
    


        