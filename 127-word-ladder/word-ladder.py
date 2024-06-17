class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words_set = set(wordList)
        if endWord not in words_set:
            return 0
        q = deque([(beginWord, 1)])
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i + 1:]
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = prefix + c + suffix
                    if new_word in words_set:
                        words_set.remove(new_word)
                        q.append((new_word, length + 1))
        return 0
