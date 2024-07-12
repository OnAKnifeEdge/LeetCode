class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        #  it's optimal to always remove the substring that gives more points first.
        first, second = ("ab", "ba") if x >= y else ("ba", "ab")
        x, y = max(x, y), min(x, y)
        s = list(s)

        def remove_substrings(s, target, points):
            write_idx = 0
            gain = 0
            for read_idx in range(len(s)):
                s[write_idx] = s[read_idx]
                if write_idx > 0 and s[write_idx - 1] + s[write_idx] == target:
                    write_idx -= 1
                    gain += points
                else:
                    write_idx += 1
            return s[:write_idx], gain

        # First pass: remove the higher point substring
        s, gain_first = remove_substrings(s, first, x)

        # Second pass: remove the lower point substring
        s, gain_second = remove_substrings(s, second, y)

        return gain_first + gain_second
