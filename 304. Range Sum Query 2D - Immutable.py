#-*- coding:utf-8 -*-
#@Date   : 2018/10/28
#@Author : suyifan
#@File   : 304. Range Sum Query 2D - Immutable.py

# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        height = len(matrix)
        width = len(matrix[0])
        self.list1 = [[0] * width for i in range(height)]
        self.list1[0][0] = matrix[0][0]
        for i in range(1, width):
            self.list1[0][i] = self.list1[0][i - 1] + matrix[0][i]
        for i in range(1, height):
            self.list1[i][0] = self.list1[i - 1][0] + matrix[i][0]
        for i in range(1, height):
            for j in range(1, width):
                self.list1[i][j] = matrix[i][j] + self.list1[i - 1][j] + self.list1[i][j - 1] - self.list1[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # return self.list1[row2,col2] - self.list1[max(row1 -1,0)][col2] - self.list1[ row2,max(col2 -1,0)] + self.list1[max(0,row1-1),max(0
        num1 = self.list1[row2][col2]
        if row1 == 0:
            num2 = 0
        else:
            num2 = self.list1[row1 - 1][col2]
        if col1 == 0:
            num3 = 0
        else:
            num3 = self.list1[row2][col1 - 1]

        if row1 == 0 or col1 == 0:
            num4 = 0
        else:
            num4 = self.list1[row1 - 1][col1 - 1]
        return num1 - num2 - num3 + num4

        # Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

a = NumMatrix(matrix)
q = a.sumRegion(2,1,4,3)
print("q =",q)