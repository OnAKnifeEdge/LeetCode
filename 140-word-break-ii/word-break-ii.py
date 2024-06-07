class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        n = len(s)

        # Now, dp[i] will store all possible sentences from s[i:].
        dp = [[] for _ in range(n + 1)]

        # Base case: empty string at the end can make an empty list
        dp[n] = [""]

        for i in reversed(range(n)):
            for j in range(i, n):
                # If a valid word is found and there exists segmentations for the rest.
                if s[i:j + 1] in words and dp[j + 1]:
                    for sentence in dp[j + 1]:
                        if sentence:
                            dp[i].append(s[i:j + 1] + " " + sentence)
                        else:
                            dp[i].append(s[i:j + 1])

        # The final result will be stored in dp[0], the beginning of the string.
        return dp[0]


# 139
# def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#     dp = [False] * (len(s) + 1)
#     dp[-1] = True  # base case: empty string is always breakable
#     words = set(wordDict)
#     for i in reversed(range(len(s))):
#         for j in range(i, len(s)):
#             if s[i:j + 1] in words and dp[j + 1]:
#                 dp[i] = True
#                 break

#     return dp[0]
