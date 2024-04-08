class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # The set will contain all unique characters in the string
        uniques = len(set(s))
        max_length = 0
        
        # Iterate from 1 to the total number of unique characters in s
        for unique in range(1, uniques + 1):
            # Initialize window pointers and dict to keep track of character frequency within the window
            left, right = 0, 0
            frequency = collections.defaultdict(int)
            unique_count = 0
            count_at_least_k = 0
            
            # Process the string with the sliding window
            while right < len(s):
                c = s[right]
                # Update frequency for the current character
                if frequency[c] == 0:
                    unique_count += 1
                frequency[c] += 1
                
                # If this character has hit the k mark, update our count_at_least_k
                if frequency[c] == k:
                    count_at_least_k += 1

                # Expand the window by moving the right pointer
                right += 1

                # If we've exceeded the number of unique characters desired, contract from the left
                while unique_count > unique:
                    d = s[left]
                    if frequency[d] == k:
                        count_at_least_k -= 1
                    frequency[d] -= 1
                    
                    # If the character frequency falls to zero, reduce unique count
                    if frequency[d] == 0:
                        unique_count -= 1

                    left += 1
                
                # Only update max_length if all current unique characters in the window
                # meet or exceed k and the unique characters count matches our target
                if unique_count == unique and unique_count == count_at_least_k:
                    max_length = max(max_length, right - left)

        return max_length

        # Divide and Conquor
        # if len(s) < k:
        #     return 0

        # # Count the frequency of each character in the string
        # frequency = {}
        # for char in s:
        #     frequency[char] = frequency.get(char, 0) + 1

        # # Loop through the string and split it at the first character
        # # which frequency is less than k
        # for i in range(len(s)):
        #     if frequency[s[i]] < k:
        #         # The string is split into two parts around the character with frequency < k
        #         left_part = self.longestSubstring(s[:i], k)
        #         right_part = self.longestSubstring(s[i+1:], k)
        #         # Return the max length from left and right parts
        #         return max(left_part, right_part)

        # # If we didn't return inside the loop, it means every character appears at least k times
        # return len(s)

                
