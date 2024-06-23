class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        target = s // k
        n = len(nums)
        nums.sort(reverse=True)  # Sort in descending order
        key = 0
        memo = {}

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
                memo[(key, start)] = result  # Memoize with 'start' as well 
                return result

            if (key, start) in memo: # Check memo with 'start'
                return memo[(key, start)]  

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
            memo[(key, start)] = False
            return False

        return backtrack(0, k, 0)