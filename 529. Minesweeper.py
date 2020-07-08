#-*- coding:utf-8 -*-
#@Date   : 2019/1/10
#@Author : suyifan
#@File   : 529. Minesweeper.py

board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]

"""

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
"""


class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m = len(board)
        n = len(board[0])
        # list1 = [[None for i in range(n)]for j in range(m)]
        #
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] != "M":
        #             list1[i][j] = self.count(i,j,m,n,board)



        x,y = int(click[0]),int(click[1])
        if not ((0<=x<m) and (0<=y<n)):
            return board
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        else:

            self.dfs(board,x,y,m,n)
        return board
    def dfs(self,borad,x,y,m,n):
        if borad[x][y] == "E":
            count = 0
            for i,j in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                q,w = x+i,y+j
                if ((0<=q<m) and (0<=w<n) )and borad[q][w] == "M":
                    count += 1
            if count == 0:
                borad[x][y] = "B"
                for i, j in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    q, w = x + i, y + j
                    if (0<=q<m) and (0<=w<n):
                        self.dfs(borad,q,w,m,n)
            else:
                borad[x][y] = str(count)
                return borad


a = Solution()
q = a.updateBoard(board,click)
print("q =",q)