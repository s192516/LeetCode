#-*- coding:utf-8 -*-
#@Date   : 2018/11/30
#@Author : suyifan
#@File   : 37. Sudoku Solver.py


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return False
        # self.n = len(board)
        self.solve(board)
        return board

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for c in range(1,10):
                        if self.valid(board, i, j, str(c)):
                            board[i][j] = str(c)
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    def valid(self, board, i, j, c):

        for idx in range(9):
            # print(board[idx][j]==c,type(board[i][j]),type(c))
            if board[idx][j] == c:
                return False
            if board[i][idx] == c:
                return False
            if board[i // 3 * 3 + idx % 3][j // 3 * 3 + idx % 3] == c:  # and  board[i//3*3 + i//3 ][j//3*3 + i//3] == c:
                return False
        return True

a = Solution()
q = a.solveSudoku(board)
print("q =",q)