class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        for bracket in s:
            if bracket == "[":
                count += 1
            else:
                if count > 0:
                    # decrement only if count is positive.
                    count -= 1
        return (count + 1) // 2
