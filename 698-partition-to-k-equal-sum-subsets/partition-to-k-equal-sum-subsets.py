class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        target = s // k
        n = len(nums)
        # Optimization: bitmask
        key = 0
        # Optimization: memoorization
        memo = {}
        # Optimization: make it faster by pruning and fail early
        nums.sort(reverse=True)

        def use(i):
            nonlocal key
            key |= 1 << i

        def reverse_use(i):
            nonlocal key
            key ^= 1 << i

        def has_used(i):
            nonlocal key
            return (key >> i) & 1

        def backtrack(bucket, k, start):
            if k == 0:
                return True

            if bucket == target:
                result = backtrack(0, k - 1, 0)
                memo[key] = result
                return result

            if key in memo:
                # 避免冗余计算
                return memo[key]

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

                # Optimization
                if bucket == 0:
                    memo[key] = False
                    return False

            memo[key] = False
            return False

        return backtrack(0, k, 0)
