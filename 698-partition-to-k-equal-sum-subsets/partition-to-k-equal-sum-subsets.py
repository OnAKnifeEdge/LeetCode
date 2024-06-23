class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        target = s // k
        n = len(nums)
        nums.sort(reverse=True)  # descending order
        # used = [False] * n
        used = 0
        memo = {}

        def use(i):
            nonlocal used
            used |= 1 << i

        def reverse_use(i):
            nonlocal used
            used ^= 1 << i

        def has_used(i):
            nonlocal used
            return (used >> i) & 1

        def backtrack(bucket, k, start):
            if k == 0:
                return True

            if bucket == target:
                result = backtrack(0, k - 1, 0)
                memo[used] = result
                return result

            if used in memo:
                # 避免冗余计算
                return memo[used]

            for i in range(start, n):
                num = nums[i]
                if has_used(i):
                    continue
                if bucket + num > target:
                    continue

                use(i)
                if backtrack(bucket + num, k, i + 1):
                    return True
                reverse_use(i)
            memo[used] = False
            return False

        return backtrack(0, k, 0)
