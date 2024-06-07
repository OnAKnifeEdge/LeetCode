class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # @cache
        # def dp(i):  # if s[i:] can be segemented
        #     if i == len(s):
        #         return True
        #     for word in wordDict:
        #         if s[i:].startswith(word) and dp(i + len(word)):
        #             return True
        #     return False

        # return dp(0)

        # dp[i]: if s[i:] can be segemented
        dp = [False] * (len(s) + 1)
        dp[-1] = True  # base case: empty string is always breakable

        for i in reversed(range(len(s) + 1)):
            for word in wordDict:
                if dp[i]:
                    break
                word_length = len(word)
                # if s[i:].startswith(word):
                if s[i:i + word_length] == word:
                    if (i + word_length) <= len(s) and dp[i + word_length]:
                        dp[i] = True

        return dp[0]
