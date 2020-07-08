#-*- coding:utf-8 -*-
#@Date   : 2018/12/4
#@Author : suyifan
#@File   : 279. Perfect Squares.py


n = 15
n  = 16


#解法1
# class Solution:
#
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#
#         stack = [[n, 0]]
#
#         visited = [False] * (n+1)
#         # visited[-1] = True
#
#         while stack:
#             num, step = stack.pop(0)
#
#             i = 1
#             left_num = num - i ** 2
#
#             while left_num >= 0:
#
#                 if left_num == 0:
#                     return step + 1
#
#                 if not visited[left_num]:
#                     stack.append([left_num, step + 1])
#                     visited[left_num] = True
#                 left_num = num - i ** 2
#
#                 i += 1
#                 # left_num = num - i ** 2
#
# a = Solution()
# q = a.numSquares(n)
# print("q =",q)



#解法2
n = 20
n = 15
n = 16
class Solution:

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(n+1):
            dp[i] = i
            j = 1
            while j ** 2 <= i:
                dp[i] = min(dp[i],dp[i-j**2]+1)
                j += 1
        # print(dp)
        return dp[n]


a = Solution()
q = a.numSquares(n)
print("q =",q)