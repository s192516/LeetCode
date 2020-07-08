#-*- coding:utf-8 -*-
#@Date   : 2018/9/23
#@Author : suyifan
#@File   : 498.py


matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
matrix = [[i for i in range(1,7)] for j in range(1,6)]
# print(matrix)


class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        rtype = []

        if matrix == []:
            return []
        if matrix == [[]]:
            return []

        height = len(matrix) - 1
        width = len(matrix[0]) - 1

        i = j = 0
        rtype.append(matrix[i][j])
        probe = 1
        while i + j < height + width :
            if i == 0 and j < width:
                j += 1
                rtype.append(matrix[i][j])
                probe *= -1

                while j != 0 and i < height:
                    i += 1
                    j -= 1
                    rtype.append(matrix[i][j])

            if j == 0 and i < height:
                i += 1
                rtype.append(matrix[i][j])
                probe *= -1

                while i != 0 and j < width:
                    i -= 1
                    j += 1
                    rtype.append(matrix[i][j])


            if i == height and j < width:
                j += 1
                rtype.append(matrix[i][j])
                while i > 0 and j < width:
                    i -= 1
                    j += 1
                    rtype.append(matrix[i][j])

            if j == width and i < height:
                i += 1
                rtype.append(matrix[i][j])
                while i < height and j > 0:
                    i += 1
                    j -= 1
                    rtype.append(matrix[i][j])
            # print(i,j)



        return rtype



a = Solution()
q = a.findDiagonalOrder(matrix)
print("q= ",q)