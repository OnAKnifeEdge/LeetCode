class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(left, right, path):
            if left < right:
                return
            if left > n or right > n:
                return
            if left == n and right == n:
                result.append("".join(path))
                return

            path.append("(")
            backtrack(left + 1, right, path)
            path.pop()

            path.append(")")
            backtrack(left, right + 1, path)
            path.pop()

        backtrack(0, 0, [])
        return result
