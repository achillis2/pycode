# 130. 被围绕的区域
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# https://segmentfault.com/a/1190000012898131


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        # 一开始是常规的代码
        m = len(board)
        if m == 0:
            return
        n = len(board[0])

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for row in range(m):
            self.__dfs(board, row, 0, m, n, directions)
            self.__dfs(board, row, n - 1, m, n, directions)

        for col in range(1, n - 1):
            self.__dfs(board, 0, col, m, n, directions)
            self.__dfs(board, m - 1, col, m, n, directions)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'

    def __dfs(self, board, i, j, m, n, directions):
        # 把 'O' 变成一个别的符号，然后扩散开来
        # 这里相当于 marked
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = '-'
            for direction in directions:
                new_x = i + direction[0]
                new_y = j + direction[1]
                self.__dfs(board, new_x, new_y, m, n, directions)


if __name__ == '__main__':
    # board = [['X', 'X', 'X', 'X'],
    #          ['X', 'O', 'O', 'X'],
    #          ['X', 'X', 'O', 'X'],
    #          ['X', 'O', 'X', 'X']]
    # board = [['O', 'O', 'O'],
    #          ['O', 'O', 'O'],
    #          ['O', 'O', 'O']]

    board = [["X", "O", "X", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "X"],
             ["X", "O", "X", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "X"]]
    solution = Solution()
    solution.solve(board)
    for row in board:
        print(row)
