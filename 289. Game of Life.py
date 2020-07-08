#-*- coding:utf-8 -*-
#@Date   : 2018/11/8
#@Author : suyifan
#@File   : 289. Game of Life.py

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        list1 = []

        height = len(board)
        width = len(board[0])
        if height * width != 0:
            for i in range(height):
                for j in range(width):
                    count = 0
                    for ii in range(i - 1, i + 2):
                        for jj in range(j - 1, j + 2):

                            if not (ii == i and jj == j):
                                if not (ii < 0 or ii >= height or jj < 0 or jj >= width):
                                    if board[ii][jj] == 1:
                                        count += 1
                    print(count, end=" ")
                    if board[i][j] == 1 and (count < 2 or count > 3):
                        # board[i][j] = 0
                        list1.append([i,j])
                    elif board[i][j] == 0 and count == 3:
                        list1.append([i,j])
                        # board[i][j] = 1
        for l in list1:
            i,j = l[0],l[1]
            if board[i][j] == 1:
                board[i][j] = 0
            else:
                board[i][j] = 1
        print("----")

print("board =",board)
a = Solution()
q = a.gameOfLife(board)
print("q=",board)