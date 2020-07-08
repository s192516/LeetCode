#-*- coding:utf-8 -*-
#@Date   : 2018/7/16
#@Author : huali
#@File   : __init__.py.py




class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        height = len(board)
        width = len(board[0])
        # 这里没有考虑 1行或者1列的情况,等下补充
        if (height == 0 or width == 0) and not word:
            return True
        if (height == 0 or width == 0) and word:
            return False

        # if height == 1:
        # for i in board[0]:
        # if i == word[0]:
        # list1 = [false for i in range(width)]
        # if self.solve1(board,list1,word,0,widht,0,j)

        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    list1 = [[False for i in range(width)] for i in range(height)]
                    if self.solve(board, list1, word, height - 1, width - 1, i, j):
                        return True
        return False

    def solve(self, board, list1, word, height, width, i, j):
        # list1[i][j] == True
        # for char in word:
        if not word:
            return True
        char = word[0]
        if not board[i][j] and char == board[i][j]:
            board[i][j] = True
            word = word[1:]

            if i == height and j == width:
                return self.solve(board, list1, word, i - 1, j) or self.solve(board, list1, word, i, j - 1)
            elif i == height and j == 0:
                return self.solve(board, list1, word, i - 1, j) or self.solve(board, list1, word, i, j + 1)
            elif i == height and j < width:
                return self.solve(board, list1, word, i - 1, j) or self.solve(board, list1, word, i,
                                                                              j - 1) or self.solve(board, list1, word,
                                                                                                   i, j + 1)
            elif i == 0 and j == width:
                return self.solve(board, list1, word, i + 1, j) or self(board, list1, word, i, j - 1)
            elif i == 0 and j == 0:
                return self.solve(board, list1, word, i + 1, j) or self.solve(board, list1, word, i, j + 1)
            elif i == 0 and j < width:
                return self.solve(board, list1, word, i + 1, j) or self.solve(board, list1, word, i,
                                                                              j + 1) or self.sovle(board, list1, word,
                                                                                                   i, j - 1)
            elif i < height and j == 0:
                return self.solve(board, list1, word, i - 1, j) or self.solve(board, list1, word, i + 1,
                                                                              j) or self.solve(board, list1, word,
                                                                                               i - 1, j + 1)
            elif i < height and j < width:
                return self.solve(board, list1, word, i - 1, j) or self.solve(board, list1, word, i + 1,
                                                                              j) or self.solbe(board, list1, word, i,
                                                                                               j - 1) or self.solve(
                    board, list1, word, i, j + 1)
            elif i < height and j == width:
                return self.solve(board, list1, word, i - 1, j) or self.solve(board, list1, word, i + 1,
                                                                              j) or self.solve(board, list1, word, i,
                                                                                               j - 1)
        else:
            return False