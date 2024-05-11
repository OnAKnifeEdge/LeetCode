class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = [0] * len(heights)
        mono_stack = []
        for i in reversed(range(n)):
            count = 0
            while mono_stack and heights[mono_stack[-1]] <= heights[i]:
                mono_stack.pop()
                count += 1
            if mono_stack:
                count += 1
            result[i] = count
            mono_stack.append(i)
        return result
