#-*- coding:utf-8 -*-
#@Date   : 2018/9/28
#@Author : suyifan
#@File   : 832. Flipping an Image.py

A = [[1,1,1],[1,0,1],[0,0,0]]


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(A)
        # rtype = [[] for i in range(length)]

        for i in range(length):
            for j in range(length-1,-1,-1):
                if A[i][j] == 1:
                    A[i].append(0)
                else:
                    A[i].append(1)
        # print(A)
        rtype = [i[length:] for i in A]
        return  rtype

a = Solution()
q = a.flipAndInvertImage(A)
print("q = ",q)