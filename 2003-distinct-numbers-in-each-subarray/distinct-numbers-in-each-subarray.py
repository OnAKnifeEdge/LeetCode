class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        frequency = {}
        result = []
        for i in range(n):
            num = nums[i]
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
            if i == k - 1:
                result.append(len(frequency))
                continue
            if i < k:
                continue
            to_be_deleted = nums[i - k]
            frequency[to_be_deleted] -= 1
            if frequency[to_be_deleted] == 0:
                del frequency[to_be_deleted]
            result.append(len(frequency))
        return result
