class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(arr, k):
            pivot = random.choice(arr)
            left, mid, right = [], [], []

            for num in arr:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quick_select(left, k)

            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))

            return pivot

        return quick_select(nums, k)
