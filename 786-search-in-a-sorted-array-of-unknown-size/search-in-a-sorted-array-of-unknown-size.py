# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # If the target is the first element
        if reader.get(0) == target:
            return 0

        # First, let's find the bounds where 'target' could be.
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1  # Exponentially increase the index.

        while left <= right:
            mid = (left + right) // 2  
            num = reader.get(mid)

            if num == target:
                return mid
            elif num > target:  
                right = mid - 1
            else: 
                left = mid + 1

        return -1

        