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
        d = defaultdict(int)
        
        for num in nums:
            # The current prefix sum
            prefix_sum += num
            
            # Situation 1:
            # Continuous subarray starts 
            # from the beginning of the array
            if prefix_sum == k:
                count += 1
            
            # Situation 2:
            # The number of times the curr_sum − k has occurred already, 
            # determines the number of times a subarray with sum k 
            # has occurred up to the current index
            count += d[prefix_sum - k]
            
            # Add the current sum
            d[prefix_sum] += 1
                
        return count

        