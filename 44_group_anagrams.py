from typing import List


class Solution:
    def convert_word(self, word: str):
        words = [0] * 26
        for letter in word:
            index = ord(letter) - ord('a')
            words[index] = words[index] + 1
        return ','.join(map(str, words))

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        look_up = {}
        for value in strs:
            word = self.convert_word(value)
            positions = look_up.get(word, [])
            positions.append(value)
            look_up[word] = positions
        return list(look_up.values())


if __name__ == '__main__':
    solution = Solution()
    input_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.group_anagrams(input_1))
    input_2 = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
    print(solution.group_anagrams(input_2))
