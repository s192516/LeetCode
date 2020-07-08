#-*- coding:utf-8 -*-
#@Date   : 2019/1/9
#@Author : suyifan
#@File   : 419. Battleships in a Board.py

board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
board = [["X","X","X"]]

class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        height = len(board)
        width = len(board[0])

        ans = 0
        for i in range(height):
            for j in range(width):
                if board[i][j] == "." or (i>0 and board[i-1][j] == "X") or (j>0 and board[i][j-1] == "X"):
                    continue
                else:
                    ans += 1


        return ans

a = Solution()
q = a.countBattleships(board)
print("q =",q)