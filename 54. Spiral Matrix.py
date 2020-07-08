#-*- coding:utf-8 -*-
#@Date   : 2018/9/21
#@Author : suyifan
#@File   : 54. Spiral Matrix.py

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1]]
# matrix = []
# matrix = [[1],[2]]
# matrix =[
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
print(len(matrix),"m0",matrix[0])
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        if m == 1:
            return matrix[0]
        n = len(matrix[0])
        # if m == 0:
        #     return []
        # if m == 1:
        #     return matrix[0]
        # rtype = [None for i in range(n * m)]
        rtype = [None for i in range(m * n)]
        count = 0

        i = j = 0
        while count < n * m:

            while j < n and matrix[i][j] != None:
                rtype[count] = matrix[i][j]
                matrix[i][j] = None
                count += 1
                j += 1
            j -= 1
            i += 1
            while i < m and matrix[i][j] != None:
                rtype[count] = matrix[i][j]
                matrix[i][j] = None
                count += 1
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and matrix[i][j] != None:
                rtype[count] = matrix[i][j]
                matrix[i][j] = None
                count += 1
                j -= 1
            j += 1
            i -= 1
            while i > 0 and matrix[i][j] != None:
                rtype[count] = matrix[i][j]
                matrix[i][j] = None
                count += 1
                i -= 1
            i += 1
            j += 1

        return rtype

a = Solution()
q = a.spiralOrder(matrix)
print("q= ", q)