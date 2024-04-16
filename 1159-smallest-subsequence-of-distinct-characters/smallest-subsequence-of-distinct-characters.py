class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # 316  https://leetcode.com/problems/remove-duplicate-letters/description/
        stack = []  # keep track of the characters in the result string.
        seen = set() 

        # maps each character to its last occurrence in the string. 
        last_occurence = {c: i for i, c in enumerate(s)} 
        for i, c in enumerate(s):
            if c in seen:
                continue

            while stack and c < stack[-1] and i < last_occurence[stack[-1]]:
                seen.discard(stack.pop())
            seen.add(c)
            stack.append(c)
        return ''.join(stack)     
        