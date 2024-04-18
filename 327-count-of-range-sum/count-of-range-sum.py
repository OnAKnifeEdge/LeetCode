class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1] 

        def merge_sort(l, r):
            if l == r:
                return 0

            mid = (l + r) // 2
            count = merge_sort(l, mid) + merge_sort(mid + 1, r)

            i = j = mid + 1

            for left in prefix_sum[l: mid + 1]:
                while i <= r and prefix_sum[i] - left < lower:
                    i += 1 # i is the start index so that the range_sum >= lower
                while j <= r and prefix_sum[j] - left <= upper:
                    j += 1 # j is the end index so that the range_sum > upper that means the previous ones are <= upper
                count += j - i

            prefix_sum[l: r + 1] = sorted(prefix_sum[l: r + 1])
            return count

        return merge_sort(0, n)