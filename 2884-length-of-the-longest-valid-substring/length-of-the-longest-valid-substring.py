class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        max_length = 0
        n = len(word)
        right = n - 1  # track the right boundary of the current valid window

        for left in reversed(range(n)):
            for k in range(left, min(left + 10, right + 1)):
                if word[left:k + 1] in forbidden_set:
                    # If found, the right boundary is updated to k - 1
                    # shrinks the current valid window from the right side
                    right = k - 1
                    break
            max_length = max(max_length, right - left + 1)
        return max_length
