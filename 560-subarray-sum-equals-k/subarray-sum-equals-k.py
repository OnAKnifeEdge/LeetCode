class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        prefix_sum = 0
        cnt = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum == k:
                cnt += 1
            
            # If there is a previous prefix sum such that current_sum - previous_sum = k,
            # add the number of occurrences of that previous_sum to count.
            if (prefix_sum - k) in d:
                cnt += d[prefix_sum - k]

            # Update the occurrences of the prefix sum.
            if prefix_sum in d:
                d[prefix_sum] += 1
            else:
                d[prefix_sum] = 1

        return cnt