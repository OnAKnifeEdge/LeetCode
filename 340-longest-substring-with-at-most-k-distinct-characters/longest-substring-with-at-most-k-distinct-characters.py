class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = collections.Counter()
        left = 0
        result = 0
        for right in range(len(s)):
            c = s[right]
            counter[c] += 1
            while len(counter) > k:
                d = s[left]
                counter[d] -= 1
                if counter[d] == 0:
                    del counter[d]
                left += 1
            result = max(result, right - left + 1)
        return result


        