class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def helper(k):
            # 3355
            diff = [0] * n

            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                if r + 1 < n:
                    diff[r + 1] -= v

            s = 0
            for i in range(n):
                s += diff[i]
                if s < nums[i]:  # 数字更大，说明减不完
                    return False
            return True


        left, right = 0, len(queries)

        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if left <= len(queries) else -1