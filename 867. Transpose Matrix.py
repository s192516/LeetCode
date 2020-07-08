#-*- coding:utf-8 -*-
#@Date   : 2018/9/13
#@Author : suyifan
#@File   : 867. Transpose Matrix.py


####注意生成空列表时候的问题,虽然我现在也不太明白
A = [[1,2,3],[4,5,6]]
A = [[3]]

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        length_i = len(A)
        length_j = len(A[0])
        rtype = [[0]*length_i for x in range(length_j)]

        i = j = 0
        while i < length_i :
            while j < length_j:
                print(i,j, rtype)
                rtype[j][i] = A [i][j]
                j += 1
            i += 1
            j = 0
        return rtype


a = Solution()
q = a.transpose(A)
print("q=",q)