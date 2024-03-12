class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        LETTERS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if len(digits) == 0:
            return []

        def backtrack(i, path):
            if len(path) == len(digits):
                results.append(''.join(path))
                return
            possible_letters = LETTERS[digits[i]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(i + 1, path)
                path.pop()
        results = []
        backtrack(0, [])
        return results
        