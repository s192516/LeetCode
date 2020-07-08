#-*- coding:utf-8 -*-
#@Date   : 2018/12/29
#@Author : suyifan
#@File   : 835. Image Overlap.py

A = [[1,1,0],[1,1,0],[0,0,1]]
B = [[1,0,0],[0,1,1],[0,1,1]]

A = [[0,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,1,0,0,1]]
B = [[1,0,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[1,0,1,1,1]]
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = len(A)
        ans = 0
        for i in range(n):
            for j in range(n):
                sum1 = 0
                for q in range(n):
                    if i + q < n:
                        for w in range(n):
                            if j + w < n:
                                if A[q][w] == 1 and B[q+i][w+j] == 1:
                                    sum1 += 1
                                    if sum1 > ans:
                                        ans = sum1
                                        # print(i, j,q,w)
                            else:
                                break
                    else:
                        break
        for i in range(n):
            for j in range(n):
                sum1 = 0
                for q in range(n):
                    if q - i >= 0:
                        for w in range(n):
                            if w - j >= 0:
                                if A[q][w] == 1 and B[q-i][w-j] == 1:
                                    sum1 += 1
                                    if sum1 > ans:
                                        ans = sum1
                                        # print(i, j)
                            else:
                                continue
                    else:
                        continue
        return ans

a = Solution()
q = a.largestOverlap(A,B)
print("q =",q)