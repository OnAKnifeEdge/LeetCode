class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, depth = q.popleft()

            if word == endWord:
                return depth

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i + 1 :]
                    if new_word in word_set:
                        q.append((new_word, depth + 1))
                        word_set.remove(new_word)

        return 0
