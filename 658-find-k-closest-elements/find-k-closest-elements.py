class Solution:
    # This index represents the position of the first element in the array 
    # that is >= x or the length of the array if x is greater than all elements. 
    def left_bound(self, arr: List[int], x: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= x:
                right = mid
            else: 
                left = mid + 1
        return left

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = self.left_bound(arr, x)
        left = right - 1

        while k > 0:
            # If the left index goes out of bounds, we can only go right.
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif (x - arr[left] <= arr[right] - x):
                left -= 1
            else:
                right += 1
            k -= 1
        return arr[left + 1:right]