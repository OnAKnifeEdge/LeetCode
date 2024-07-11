class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        longest = 0
        n = len(word)
        right = n - 1

        for left in reversed(range(n)):
            for k in range(left, min(left + 10, right + 1)):
                if word[left : k + 1] in forbidden_set:
                    right = k - 1
                    break
            longest = max(longest, right - left + 1)
        return longest
