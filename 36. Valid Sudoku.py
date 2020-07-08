#-*- coding:utf-8 -*-
#@Date   : 2018/9/27
#@Author : suyifan
#@File   : 36. Valid Sudoku.py


board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

# board = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        list1 = [set() for i in range(27) ]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in list1[i]:
                    return False
                else:
                    list1[i].add(board[i][j])

                temp = j + 9
                if board[i][j] in list1[temp]:
                    return False
                else:
                    list1[temp].add(board[i][j])

                temp = (i // 3) * 3 + j // 3 + 18
                if board[i][j] in list1[temp]:
                    return False
                else:
                    list1[temp].add(board[i][j])
        return True
for i in range(9):
    print(board[i])
a = Solution()
q = a.isValidSudoku(board)
print("q = ",q)