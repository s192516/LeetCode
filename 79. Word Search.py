#-*- coding:utf-8 -*-
#@Date   : 2018/10/23
#@Author : suyifan
#@File   : 79. Word Search.py


board = [["A","B","C","D"]]
word = "BC"
board = [[""],["B"],["C"],[""]]
word = "BC"

board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word = "BCCEE"
word = "BC"

board = [["a","a"]]
word = "aaa"

board = [["a","b"]]
word = "ba"

board = [["a","b"],["c","d"]]
word = "cdba"

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
# board = [["A","B","C","E"],["S","F","E","S"]]

word = "ABCESEEEFd"
# word = "AB"
# class Solution:
#     # def __init__(self):
#     #     self.temp = []
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         # word = list(word)
#         height = len(board)
#         width = len(board[0])
#         if height * width < len(word):
#             return  False
#         # 这里没有考虑 1行或者1列的情况,等下补充
#         if (height == 0 or width == 0) and not word:
#             return True
#         if (height == 0 or width == 0) and word:
#             return False
#
#         if height == 1 and width == 1 and len(word) == 1:
#             if board[0][0] == word:
#                 return True
#             else:
#                 return False
#         elif height == 1 and width == 1 and (len(word)) != 1:
#             return False
#         elif height == 1:
#             for j in range(width):
#                 if board[0][j] == word[0]:
#                     list1 = [False for i in range(width)]
#                     if self.solve1(board[0], list1, word, width - 1, j):
#                         return True
#             return False
#
#         elif width == 1:
#             for i in range(height):
#                 if board[i][0] == word[0]:
#                     list1 = [False for i in range(height)]
#                     if self.solve2(board, list1, word, height - 1, i):
#                         return True
#             return False
#
#         for i in range(height):
#             for j in range(width):
#                 if board[i][j] == word[0]:
#                     list1 = [[False for i in range(width)] for i in range(height)]
#                     if self.solve(board, list1, word, height - 1, width - 1, i, j):
#                         return True
#         return False
#
#     def solve1(self, board, list1, word, width, j):
#         if not word:
#             return True
#         char = word[0]
#         # print("list1=",list1,type(list1))
#         # print("board =",board,type(board),"###60")
#         # print("char =",char,"j=",j)
#         # if not list1[j]:
#         #     print("yes")
#         # if char == board[j]:
#         print("j= ",j)
#         if not list1[j] and char == board[j]:
#             word = word[1:]
#
#             list1[j] = True
#             if j == 0:
#                 return self.solve1(board, list1, word, width, j + 1)
#             if j == width:
#                 return self.solve1(board, list1, word, width, j - 1)
#             else:
#                 return self.solve1(board, list1, word, width, j + 1) or self.solve1(board, list1, word, width, j - 1)
#         else:
#             return False
#
#     def solve2(self, board, list1, word, height, i):
#         if not word:
#             return True
#         char = word[0]
#         if not list1[i] and char == board[i][0]:
#             word = word[1:]
#
#             list1[i] = True
#             if i == 0:
#                 return self.solve2(board, list1, word, height, i + 1)
#             elif i == height:
#                 return self.solve2(board, list1, word, height, i - 1)
#             else:
#                 return self.solve2(board, list1, word, height, i + 1) or self.solve2(board, list1, word, height, i - 1)
#
#     def solve(self, board, list1, word, height, width, i, j):
#         # list1[i][j] == True
#         # for char in word:
#         # list1 = list1[:]
#         import copy
#         if not word:
#             return True
#         char = word[0]
#         if not list1[i][j] and char == board[i][j]:
#             list1[i][j] = True
#             # self.temp .append([i,j])
#             # list1 = copy.deepcopy(list1)
#             word = word[1:]
#             if i == 0 and j == 0:
#                 # list1[i][j] = True
#                 is1 = self.solve(board, list1, word,height, width,i + 1, j)
#
#                 is2 = self.solve(board, list1, word,height, width, i, j + 1)
#                 if not (is1 or is2):
#                     list1[i][j] =True
#                     return False
#                 return  True
#             elif i == 0 and j < width:
#                 # list1[i][j] = True
#                 return self.solve(board, list1, word,height, width, i + 1, j) or self.solve(board, list1, word,height, width, i,j + 1) or self.solve(board,list1,word, height, width,i, j - 1)
#             elif i == 0 and j == width:
#                 # list1[i][j] = True
#                 return self.solve(board, list1, word,height, width, i + 1, j) or self.solve(board, list1, word,height, width, i, j - 1)
#             elif i < height and j == 0:
#                 return self.solve(board, list1, word,height, width, i - 1, j) or self.solve(board, list1, word, height, width,i + 1,j) or self.solve(board, list1,word,height, width,i , j + 1)
#             elif i < height and j < width:
#                 return self.solve(board, list1, word,height, width, i - 1, j) or self.solve(board, list1, word,height, width, i + 1, j) or self.solve(board, list1, word,height, width, i,j - 1) or self.solve(board, list1, word, height, width,i, j + 1)
#             elif i < height and j == width:
#                 return self.solve(board, list1, word, height, width,i - 1, j) or self.solve(board, list1, word,height, width, i + 1, j) or self.solve(board, list1, word, height, width,i,  j - 1)
#             elif i == height and j == 0:
#                 return self.solve(board, list1, word, height, width,i - 1, j) or self.solve(board, list1, word, height, width,i, j + 1)
#             elif i == height and j < width:
#                 return self.solve(board, list1, word, height, width,i - 1, j) or self.solve(board, list1, word, height, width,i,   j - 1) or self.solve(board, list1, word, height, width,i, j + 1)
#             else:
#                 return self.solve(board, list1, word,height, width, i - 1, j) or self.solve(board, list1, word,height, width, i, j - 1)
#             list1[i][j] = False
#         else:
#             # list1[i][j] = False
#             return False
#
# print(board)
# print(word)
# a = Solution()
# q = a.exist(board,word)
# print("Q = ",q)


class Solution:
    # def __init__(self):
    #     self.temp = []
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # word = list(word)
        height = len(board)
        width = len(board[0])
        if height * width < len(word):
            return  False
        # 这里没有考虑 1行或者1列的情况,等下补充
        if (height == 0 or width == 0) and not word:
            return True
        if (height == 0 or width == 0) and word:
            return False

        if height == 1 and width == 1 and len(word) == 1:
            if board[0][0] == word:
                return True
            else:
                return False
        elif height == 1 and width == 1 and (len(word)) != 1:
            return False
        elif height == 1:
            for j in range(width):
                if board[0][j] == word[0]:
                    list1 = [False for i in range(width)]
                    if self.solve1(board[0], list1, word, width - 1, j):
                        return True
            return False

        elif width == 1:
            for i in range(height):
                if board[i][0] == word[0]:
                    list1 = [False for i in range(height)]
                    if self.solve2(board, list1, word, height - 1, i):
                        return True
            return False

        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    list1 = [[False for i in range(width)] for i in range(height)]
                    if self.solve(board, list1, word, height - 1, width - 1, i, j):
                        return True
        return False

    def solve1(self, board, list1, word, width, j):
        if not word:
            return True
        char = word[0]
        # print("list1=",list1,type(list1))
        # print("board =",board,type(board),"###60")
        # print("char =",char,"j=",j)
        # if not list1[j]:
        #     print("yes")
        # if char == board[j]:
        print("j= ",j)
        if not list1[j] and char == board[j]:
            word = word[1:]

            list1[j] = True
            if j == 0:
                return self.solve1(board, list1, word, width, j + 1)
            if j == width:
                return self.solve1(board, list1, word, width, j - 1)
            else:
                return self.solve1(board, list1, word, width, j + 1) or self.solve1(board, list1, word, width, j - 1)
        else:
            return False

    def solve2(self, board, list1, word, height, i):
        if not word:
            return True
        char = word[0]
        if not list1[i] and char == board[i][0]:
            word = word[1:]

            list1[i] = True
            if i == 0:
                return self.solve2(board, list1, word, height, i + 1)
            elif i == height:
                return self.solve2(board, list1, word, height, i - 1)
            else:
                return self.solve2(board, list1, word, height, i + 1) or self.solve2(board, list1, word, height, i - 1)

    def solve(self, board, list1, word, height, width, i, j):
        # list1[i][j] == True
        # for char in word:
        # list1 = list1[:]
        import copy
        if not word:
            return True
        char = word[0]
        if not list1[i][j] and char == board[i][j]:
            list1[i][j] = True
            # self.temp .append([i,j])
            # list1 = copy.deepcopy(list1)
            word = word[1:]
            if i == 0 and j == 0:
                # list1[i][j] = True
                is1 = self.solve(board, list1, word,height, width,i + 1, j) or self.solve(board, list1, word,height, width, i, j + 1)
                # if not (is1 or is2):
                #     list1[i][j] =False
                #     return False
                # return  True
            elif i == 0 and j < width:
                # list1[i][j] = True
                is1 = self.solve(board, list1, word,height, width, i + 1, j) or self.solve(board, list1, word,height, width, i,j + 1) or self.solve(board,list1,word, height, width,i, j - 1)
                # if not (is1 or is2 or is3):
                # list1[i][j] = False
                #     return
            elif i == 0 and j == width:
                # list1[i][j] = True
                is1 = self.solve(board, list1, word,height, width, i + 1, j) or self.solve(board, list1, word,height, width, i, j - 1)
                # list1 = False
            elif i < height and j == 0:
                is1 = self.solve(board, list1, word,height, width, i - 1, j) or self.solve(board, list1, word, height, width,i + 1,j) or self.solve(board, list1,word,height, width,i , j + 1)
            elif i < height and j < width:
                is1 = self.solve(board, list1, word,height, width, i - 1, j) or self.solve(board, list1, word,height, width, i + 1, j) or self.solve(board, list1, word,height, width, i,j - 1) or self.solve(board, list1, word, height, width,i, j + 1)
            elif i < height and j == width:
                is1 = self.solve(board, list1, word, height, width,i - 1, j) or self.solve(board, list1, word,height, width, i + 1, j) or self.solve(board, list1, word, height, width,i,  j - 1)
            elif i == height and j == 0:
                is1 = self.solve(board, list1, word, height, width,i - 1, j) or self.solve(board, list1, word, height, width,i, j + 1)
            elif i == height and j < width:
                is1 = self.solve(board, list1, word, height, width,i - 1, j) or self.solve(board, list1, word, height, width,i,   j - 1) or self.solve(board, list1, word, height, width,i, j + 1)
            else:
                is1 = self.solve(board, list1, word,height, width, i - 1, j) or self.solve(board, list1, word,height, width, i, j - 1)
            list1[i][j] = False
            return is1
        else:
            # list1[i][j] = False
            return False
        return True

print(board)
print(word)
a = Solution()
q = a.exist(board,word)
print("Q = ",q)
