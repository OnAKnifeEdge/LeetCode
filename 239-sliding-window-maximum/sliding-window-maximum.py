class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # stores idx of nums. [7, 6, 5]
        # mono_queue[0] will be the max

        mono_queue = deque()
        result = []
        for i, num in enumerate(nums):
            # if window ends at i -> start = i - k + 1
            left = i - k + 1
            # 把 window 外的 pop 掉
            if mono_queue and mono_queue[0] < left:
                mono_queue.popleft()
            # 把比自己小的都 pop 掉
            while mono_queue and num > nums[mono_queue[-1]]:
                mono_queue.pop()
            mono_queue.append(i)
            if left >= 0:
                result.append(nums[mono_queue[0]])
        return result
