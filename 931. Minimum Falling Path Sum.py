#-*- coding:utf-8 -*-
#@Date   : 2018/10/29
#@Author : suyifan
#@File   : 931. Minimum Falling Path Sum.py

A = [[1,2,3],[4,5,6],[7,8,9]]

class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        # height = width = 0
        # i = j = 0

        list2 = [[0] * n for i in range(n)]
        list1 = [0] * n
        for i in range(n):
            list1[i] = self.solve(A, list2,n,n-1, i)
        return min(list1)

    def solve(self, A, list2,n, i, j):
        if j < 0 or j == n :
            return 9999999999

        if i == 0:
            list2[0][j] =  A[0][j]
            return A[0][j]
        # if i == n:
        #     return list2[i - 1][j]  ###

        # print(list2[i][j])
        # print(i,j)
        if list2[i][j] != 0:
            return list2[i][j]
        list2[i][j] = A[i][j] + min(self.solve(A, list2,n,i - 1, j - 1), self.solve(A, list2,n, i - 1, j), self.solve(A,  list2,n,i - 1, j + 1))

        return list2[i][j]
a = Solution()
q = a.minFallingPathSum(A)
print("q =",q)