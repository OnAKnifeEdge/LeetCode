class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # https://leetcode.com/problems/max-consecutive-ones-iii/ 1004
        left = 0
        d = collections.defaultdict(int)
        max_frequency = 0
        result = 0
        for right in range(len(s)):
            c = s[right]
            d[c] += 1

            max_frequency = max(max_frequency, d[c])


            is_valid = (right - left + 1 - max_frequency) <= k

            if not is_valid:
                c = s[left]
                d[c] -= 1
                left += 1
            
            result = right - left + 1

        return result

        
        