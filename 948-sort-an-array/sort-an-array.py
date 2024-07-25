class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        lt, gt = self.partition(nums, left, right)
        self.quick_sort(nums, left, lt - 1)
        self.quick_sort(nums, gt + 1, right)

    def partition(self, nums, left, right):
        idx = random.randint(left, right)
        pivot = nums[idx]
        nums[idx], nums[left] = nums[left], nums[idx]

        lt = left
        gt = right

        i = left

        while i <= gt:
            if nums[i] < pivot:
                nums[i], nums[lt] = nums[lt], nums[i]
                i += 1
                lt += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1
        return lt, gt
