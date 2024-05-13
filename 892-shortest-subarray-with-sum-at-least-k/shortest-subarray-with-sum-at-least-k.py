class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # 1. prefix_sum
        # 2. mono_q on top of prefix_sum: diff >= k
        # 3. smallest window
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        mono_q = deque()
        # stores indices of prefix_sum so that it is increasing (including equals )
        # eg: nums = [3, -1, 2, 1, -1, 2] and k = 5.
        # prefix_sum [0, 3, 2, 4, 5, 4, 6]
        # if 5 -2 does not meet condition, 5 - 3 won't meet condition for sure.
        # the smallest will be prefix_sum val bigger than 2
        left = 0
        shortest = float("inf")
        for right in range(len(nums) + 1):
            while mono_q and prefix_sum[right] - prefix_sum[mono_q[0]] >= k:
                left = mono_q.popleft()
                shortest = min(shortest, right - left)

            while mono_q and prefix_sum[mono_q[-1]] > prefix_sum[right]:
                mono_q.pop()

            mono_q.append(right)
        return shortest if shortest != float("inf") else -1


"""
The usage of left = mono_q.popleft() over a manual increment like left += 1 is key to understanding how this algorithm effectively finds the shortest subarray that meets the condition (having a sum of at least k). This method revolves around managing a deque (mono_q) to track indices in the prefix_sum array rather than directly manipulating window boundaries with left and right.
Why left = mono_q.popleft() Instead of left += 1?
Dynamic Window Boundaries: The sliding window's left boundary in this context is not a simple sequential move from left to right. Instead, the left boundary should jump to positions that might potentially lead to finding a valid subarray faster. Each index in mono_q represents a starting point of a subarray (from prefix_sum[i] to prefix_sum[right]) that we consider as a candidate for satisfying the sum condition.
Queue vs. Simple Increment: Using mono_q, we effectively store potential start points (left) for the subarrays by their indices. When we do left = mono_q.popleft(), we are not just incrementing left by one but actually jumping to the next most promising starting point (based on the already computed prefix sums). This allows us to skip over several elements that wouldn't contribute to a valid subarray, thus optimizing our search for the shortest subarray.
Efficiently Finding the Starting Point: This approach efficiently finds the shortest subarray with a sum >= k by leveraging the properties of the prefix sum and utilizing the deque to access these starting points quickly. Directly incrementing left would not allow for this level of flexibility and would necessitate checking many subarrays that don't meet the condition, thus increasing the time complexity.
Improvement:
The existing implementation efficiently leverages the deque (mono_q) for managing dynamic subarray start points. Regarding "improvement about 'left'", considering the algorithm's logic, it's crucial to understand that left as a separate variable isn't inherently meaningful in iterating through the prefix_sum. Instead, mono_q's front represents the current left boundary of our subarray. So, the improvement would not be in changing how left is handled but ensuring that the algorithm remains clear and maintainable, which it achieves well with the current approach.
The algorithm indeed doesn't explicitly require managing left beyond mono_q.popleft(), since all necessary adjustments for finding the shortest subarray with a sum of at least k happen through the manipulation of indices in the mono_q.
Thus, the current use of left is already aligned with the algorithm's purposes, and the key to improvement lies not in changing how it's incremented but in ensuring the rest of the code effectively supports this dynamic boundary management.
"""
