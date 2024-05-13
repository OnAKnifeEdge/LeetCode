class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_queue = deque()  # stores indices
        result = []
        for i, num in enumerate(nums):
            if mono_queue and mono_queue[0] < i - k + 1:  # window starts at (i - k + 1)
                mono_queue.popleft()

            while mono_queue and nums[mono_queue[-1]] < num:
                mono_queue.pop()

            mono_queue.append(i)

            if i >= k - 1:  # reaches window size:
                result.append(nums[mono_queue[0]])
        return result
