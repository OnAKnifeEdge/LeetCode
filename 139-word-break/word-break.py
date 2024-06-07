class TrieNode:
    """A node in the trie structure."""

    def __init__(self):
        self.is_word = False
        self.children = {}


def buildTrie(wordDict: List[str]) -> TrieNode:
    """Builds a trie from the list of words for efficient prefix matching."""
    root = TrieNode()
    for word in wordDict:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    return root


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True  # base case: empty string is always breakable
        words = set(wordDict)
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i:j + 1] in words and dp[j + 1]:
                    dp[i] = True
                    break

        return dp[0]

    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:

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

        for i in reversed(range(len(s))):
            for word in wordDict:
                if dp[i]:
                    break
                word_length = len(word)
                # if s[i:].startswith(word):
                if s[i:i + word_length] == word:
                    if (i + word_length) <= len(s) and dp[i + word_length]:
                        dp[i] = True
                        break

        return dp[0]


    def wordBreak_trie(self, s: str, wordDict: List[str]) -> bool:

        root = buildTrie(wordDict)

        # dp[i]: if s[i:] can be segemented
        dp = [False] * (len(s) + 1)
        dp[-1] = True  # base case: empty string is always breakable

        # Iteratively fill dp from the end to the start
        for i in reversed(range(len(s))):
            node = root
            for j in range(i, len(s)):
                # Starting at startIdx,
                # we iterate forward through the string with j
                # to check if the substring s[i:j + 1] is a word.
                if s[j] in node.children:
                    node = node.children[s[j]]
                    if node.is_word and dp[j + 1]:
                        dp[i] = True
                        break  # Found a valid word break, no need to check further
                else:
                    break  # Current character doesn't match, move to next start index

        return dp[0]

