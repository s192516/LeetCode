# -*- coding:utf-8 -*-
# @Date   : 2018/9/16
# @Author : suyifan
# @File   : 62. Unique Paths.py


m = 3
n = 4

m = 7
n = 3

n = 1
m = 1

n = 5
m = 1

# class Solution(object):
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         list1 = [[ 1 for i in range(n)] for j in range(m)]
#         # a = b = 1
#
#
#         for i in range(1,m):
#             for j in range(1,n):
#                 list1[i][j] = list1[i-1][j]+list1[i][j-1]
#         return list1[m-1][n-1]
#
#
#
# a = Solution()
# q = a.uniquePaths(m,n)
# print("q=",q)


n = 10
m = 10


# class Solution(object):
#     my_list = [[0 for i in range(n)] for j in range(m)]
#
#     def uniquePaths(self, i, j):
#         if (i < 0) or (j < 0):  # 越界
#             return 0
#         elif (i >= m) or (j >= n):  # 越界
#             return 0
#         elif (i == 0) or (j == 0):  # 1 种走法
#             self.my_list[i][j] = 1
#             return 1
#         elif 0 == self.my_list[i][j]:  # 说明没有被计算过,需要计算.
#             self.my_list[i][j] = self.uniquePaths(i - 1, j) + self.uniquePaths(i, j - 1)
#             return self.my_list[i][j]
#         else:
#             return self.my_list[i][j]
#
#
# a = Solution()
# q = a.uniquePaths(4 - 1, 5 - 1)
# print("q =", q)
# print(list1[][3])



n = 1
m = 1

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (n == 0) or (m == 0):
            return 0

        if (n == 1) or (m == 1):
            return 1

        list1 = [[1 for i in range(n)] for i in range(m)]

        if list1[m-1][n-1] != 1:
            return list1[m-1][n-1]



        return self.uniquePaths(n-1,m) + self.uniquePaths(n,m-1)


a = Solution()
q = a.uniquePaths(m, n)
print("q=", q)
