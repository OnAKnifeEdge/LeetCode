class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def split_nums(nums: List[int], limit: int) -> int:
            partitions, total = 1, 0
            for num in nums:
                if total + num > limit:
                    total = 0
                    partitions += 1
                total += num
            return partitions

        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low + high) // 2
            partitions = split_nums(nums, mid)
            if partitions <= k:
                high = mid
            else:
                low = mid + 1
        return low


        