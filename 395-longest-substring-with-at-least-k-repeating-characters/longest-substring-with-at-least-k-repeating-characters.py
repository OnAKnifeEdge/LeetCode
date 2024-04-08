class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        # Count the frequency of each character in the string
        frequency = {}
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        # Loop through the string and split it at the first character
        # which frequency is less than k
        for i in range(len(s)):
            if frequency[s[i]] < k:
                # The string is split into two parts around the character with frequency < k
                left_part = self.longestSubstring(s[:i], k)
                right_part = self.longestSubstring(s[i+1:], k)
                # Return the max length from left and right parts
                return max(left_part, right_part)

        # If we didn't return inside the loop, it means every character appears at least k times
        return len(s)

                
