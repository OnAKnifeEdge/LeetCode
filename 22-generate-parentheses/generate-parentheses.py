class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(left, right, path):
            if left > right:
                return
            if left < 0 or right < 0:
                return
            if left == 0 and right == 0:
                result.append(''.join(path))
                return

            path.append("(")
            backtrack(left - 1, right, path)
            path.pop()

            path.append(")")
            backtrack(left, right - 1, path)
            path.pop()

        backtrack(n, n, [])
        return result
