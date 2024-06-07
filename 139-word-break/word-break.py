class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def dp(i):  # if s[i:] can be segemented
            if i == len(s):
                return True
            for word in wordDict:
                if s[i:].startswith(word) and dp(i + len(word)):
                    return True
            return False

        return dp(0)
