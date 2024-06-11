class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Create a dictionary mapping each character in the ring to its indexes
        ring_dict = defaultdict(list)
        for i, c in enumerate(ring):
            ring_dict[c].append(i)

        # 计算圆盘指针在 ring[i]，输入 key[j..] 的最少操作数
        @lru_cache(maxsize=None)
        def dp(i, j):
            # If we have processed the entire key, no more steps are needed
            if j == len(key):
                return 0

            n = len(ring)
            # Initialize the minimum number of steps to a large number
            min_steps = float("inf")

            # Iterate through all the positions of the current key character in the ring
            for k in ring_dict[key[j]]:
                steps = min(abs(k - i), n - abs(k - i))

                # Add the rotation steps for remaining characters
                min_steps = min(min_steps, steps + dp(k, j + 1))

            return 1 + min_steps

        return dp(0, 0)
