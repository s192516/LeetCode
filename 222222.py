#-*- coding:utf-8 -*-
#@Date   : 2018/12/22
#@Author : suyifan
#@File   : 222222.py

# def g(n,k,x):
#     # list1 =
#     list1 = f(n,k)
#     # print(list1)
#     ans = gailv(list1,x)
#     # ans = list1.count(x) / len(list1)
#     return ans

# def f(n,k,list1 = None):
#     if not list1:
#         # list1 = [[None] for i in range(n)]
#         list1 = []
#         for i in range(n):
#             list1.append([i])
#     else:
#         length = len(list1)
#         for i in range(length):
#             list_q = list1.pop(0)
#             # n = len(list_q)
#             for j in list_q:
#                 if j == 0:
#                     continue
#                 else:
#                     list_x = []
#                     for x in range(j):
#                         list_x.append(x)
#                     list1.append(list_x)
#     if k == 0:
#         return list1
#     # print(list1)
#     return f(n,k-1,list1)

# def gailv(list1,x):
#     num = 0
#
#     for i in list1:
#         # if i and i[-1] != 0:
#         #     n += 1
#         count = 0
#         for j in i:
#             if j == x:
#                 count += 1
#         num += count / len(i)
#     num /= len(list1)
#     return num


# list1 = [[5,1,1],[4,1,0],[4,0,0],[8,3,2],[6,3,2],[6,3,0],[5,3,2],[5,3,0],[5,0,0]]
# for i in list1:
    # print(i)
    # print(i,g(*i))


# ------------动归方法------------

# list1 = [[5,1,1],[4,1,0],[4,0,0],[8,3,2],[6,3,2],[6,3,0],[5,3,2],[5,3,0],[5,0,0]]
# list1 = [[3,2,0],[6,1,0],[5,2,0],[6,2,0],[10,2,0],[10,4,0],[10,6,0],[6,2,0]]
# # list1 = [[500,100,20]]
# def test_p(n, k, x):
#     # 初始化数组全部为 None   dp1:分子(f(n,k) == X)的概率，dp2：分母 不抛异常的概率
#     dp1 = [[None for j in range(k + 1)] for i in range(n + 1)]
#     dp2 = [[None for j in range(k + 1)] for i in range(n + 1)]
#
#     for i in range(k + 1):
#         dp1[0][i] = 0
#         dp2[0][i] = 0
#
#     for i in range(n + 1):
#         dp1[i][0] = 0 if x >= i else 1 / i
#         dp2[i][0] = 0 if i == 0 else 1
#
#     for i in range(1, n + 1):
#         for j in range(1, k + 1):
#             dp1[i][j] = sum([dp1[m][j - 1] / i for m in range(i)])
#             dp2[i][j] = sum([dp2[m][j - 1] / i for m in range(i)])
#
#     for i in dp1:
#         print(i)
#     print()
#     for j in dp2:
#         print(j)
#     # print(dp1)
#     # print(dp2)
#     return dp1[n][k] / dp2[n][k]
#
#
# for i in list1:
#     # print(i)
#     print(i,test_p(*i))
#     print("-----------------")





########--------------------迭代方法-----------
# def test_p1(n, k, x):
#     if n == 0:
#         return 0
#     if k == 0:
#         return 0 if x >= n else 1 / n
#
#     return 0 if x >= n else sum([test_p1(i, k - 1, x) / n for i in range(1, n)])
#
#
# def test_p2(n, k, x):
#     if n == 0:
#         return 0
#     if k == 0:
#         return 1
#
#     return sum([test_p2(i, k - 1, x) / n for i in range(1, n)])
#
#
# def test_p(n, k, x):
#     return test_p1(n, k, x) / test_p2(n, k, x)