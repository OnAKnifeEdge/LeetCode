class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix_sum = [0] + list(itertools.accumulate(nums))

        @functools.lru_cache(None)
        def dp(i, cnt):
            if cnt == 1:
                return prefix_sum[n] - prefix_sum[i]
            
            min_max_sum = prefix_sum[n]

            for j in range(i, n - cnt + 1):
                first = prefix_sum[j + 1] - prefix_sum[i]

                largest = max(first, dp(j + 1, cnt - 1))

                min_max_sum = min(min_max_sum, largest)

                if first >= min_max_sum:
                    break

            return min_max_sum

        return dp(0, k)
        