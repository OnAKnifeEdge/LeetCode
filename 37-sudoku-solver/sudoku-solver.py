class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)

        # if x can be filled in board[i][j]
        def is_valid(i, j, val):
            for idx in range(n):
                # if x is in any cell with row = i
                if board[i][idx] == val:
                    return False
                # if x is in any cell with col = j
                if board[idx][j] == val:
                    return False
                # if x is in any 3x3
                # (r // 3) * 3 and (c // 3) * 3 determine
                # the top-left corner of the subgrid that contains (r, c)
                x, y = (i // 3) * 3, (j // 3) * 3
                dx, dy = divmod(idx, 3)
                if board[x + dx][y + dy] == val:
                    return False
            return True

        def backtrack(i, j):
            if j == n:
                # 穷举到最后一列的话就换到下一行重新开始。
                return backtrack(i + 1, 0)
            if i == n:
                # 找到！
                return True

            if board[i][j] != ".":
                # 已经有数字了，下一个
                return backtrack(i, j + 1)

            for c in range(1, 10):
                x = str(c)
                if not is_valid(i, j, x):
                    continue
                # 做选择
                board[i][j] = x

                if backtrack(i, j + 1):
                    return True
                # 撤销选择
                board[i][j] = "."

        return backtrack(0, 0)
