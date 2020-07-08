#-*- coding:utf-8 -*-
#@Date   : 2018/9/20
#@Author : suyifan
#@File   : 905. Sort Array By Parity.py

A = [2,1,3,4]

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        idx = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[idx] ,A[i] = A[i],A[idx]
                idx += 1


        return A

a = Solution()
q = a.sortArrayByParity(A)
print("q=",q)