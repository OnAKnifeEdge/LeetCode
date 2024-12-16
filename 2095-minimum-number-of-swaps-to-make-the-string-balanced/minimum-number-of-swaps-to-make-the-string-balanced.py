class Solution:
    def minSwaps(self, s: str) -> int:
        unmatched_open_brackets = 0
        for c in s:
            if c == "[":
                unmatched_open_brackets += 1
            elif c == "]":
                if unmatched_open_brackets > 0:
                    unmatched_open_brackets -= 1
        return (unmatched_open_brackets + 1) // 2  # 也可以用 ceil
