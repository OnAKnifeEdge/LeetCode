class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # https://leetcode.com/problems/subarray-sum-equals-k/solutions/3777004/why-sum-k-read-this-to-understand/
        # # d[sum] -> OccuranceCount
        # d = {0: 1}
        # s, count = 0, 0
        # for num in nums:
        #     s += num
        #     if s - k in d:
        #         count += d[s - k]
        #     d[s] = d.get(s, 0) + 1
        # return count

        count, prefix_sum = 0, 0
        d = {}
        
        for num in nums:
            prefix_sum += num

            if prefix_sum == k:
                count += 1
            
            count += d.get(prefix_sum - k, 0)
            
            d[prefix_sum] = d.get(prefix_sum, 0) + 1
                
        return count

        