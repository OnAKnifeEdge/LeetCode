class Solution:
    # https://leetcode.com/problems/sort-an-array/ quick sort
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left: int, right: int) -> int:
            idx = random.randint(left, right)
            pivot = nums[idx]
            nums[left], nums[idx] = nums[idx], nums[left]

            lt = left
            gt = right
            i = left

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    i += 1
                    lt += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1
            return lt, gt

        def quick_select(left, right, idx):
            if left == right:
                return nums[left]

            lt, gt = partition(left, right)

            if idx >= lt and idx <= gt:
                return nums[idx]
            elif idx < lt:
                return quick_select(left, lt - 1, idx)
            else:
                return quick_select(gt + 1, right, idx)

        return quick_select(0, len(nums) - 1, len(nums) - k)
