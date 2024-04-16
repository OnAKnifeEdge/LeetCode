class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 如果走势下行（nums[mid] > nums[mid+1]），说明 mid 本身就是峰值或其左侧有一个峰值，所以需要收缩右边界（right = mid）；
        # 如果走势上行（nums[mid] < nums[mid+1]），则说明 mid 右侧有一个峰值，需要收缩左边界（left = mid + 1）。
        # 因为题目说了 nums 中不存在相等的相邻元素，所以不用考虑 nums[mid] == nums[mid+1] 的情况，依据以上分析即可写出代码。
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
        return left

        