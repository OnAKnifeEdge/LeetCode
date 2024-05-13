class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mono_q = MonotonicQueue()
        left = 0
        longest = 0

        for right in range(len(nums)):
            mono_q.push(nums[right])
            while abs(mono_q.max() - mono_q.min()) > limit:
                mono_q.pop(nums[left])
                left += 1
            longest = max(longest, right - left + 1)

        return longest


class MonotonicQueue:
    """
    maintains a sorted order so that we can get max and min value in constant time

    """

    def __init__(self):
        self.max_q = deque()
        self.min_q = deque()

    def push(self, x):
        # non-increasing order:
        # pop all the elements that are smaller than x (everything before is >= x)
        while self.max_q and self.max_q[-1] < x:
            self.max_q.pop()
        self.max_q.append(x)

        # non-decreasing order:
        # pop all the elements that are bigger than x (everything before is <= x)
        while self.min_q and self.min_q[-1] > x:
            self.min_q.pop()
        self.min_q.append(x)

    def pop(self, x):
        if self.max_q and self.max_q[0] == x:
            self.max_q.popleft()
        if self.min_q and self.min_q[0] == x:
            self.min_q.popleft()

    def max(self):
        return self.max_q[0] if self.max_q else None

    def min(self):
        return self.min_q[0] if self.min_q else None
