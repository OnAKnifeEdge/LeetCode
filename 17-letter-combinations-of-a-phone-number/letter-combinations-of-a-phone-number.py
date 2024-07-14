class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        LETTERS = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)
        result = []

        def backtrack(path, i):
            if len(path) == n:
                result.append("".join(path))
                return
            letters = LETTERS[digits[i]]
            for c in letters:
                path.append(c)
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return result
