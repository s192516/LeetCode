#-*- coding:utf-8 -*-
#@Date   : 2018/12/19
#@Author : suyifan
#@File   : 918. Maximum Sum Circular Subarray.py

A = [-17066,9854,21565,21364,-20470,17727,-16429,-19627,20999,22524,16752,-23476,4484,12866,8979,322]
# A = [-10,1,11,-15,1,1,-20,1,2,-2,3,4]
A = [-17066,9854,21565,21364,-20470,17727,-36056,20999,22524,16752,-23476,26651] # 错误答案77434 正确答案
A = [-17066,52783,-20470,17727,-36056,60275,-23476,26651]

A = [-17,52,-20,17,-36,60,-23,26] # 正确答案 98
A = [-3,10,-4,3,-7,12,-4,5] # 正确答案 20



# 方法正确但是时间复杂度太高
# class Solution:
#     def maxSubarraySumCircular(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#
#         n = len(A)
#         A *= 2
#         nn = len(A)
#
#         k = -1
#         ans = -999999
#         for i in range(nn):
#             if A[i] <= 0:
#                 if A[i] <= ans:
#                     continue
#                 else:
#                     ans = A[i]
#                     continue
#             else:
#                 if i <= k:
#                     continue
#             sum1 = 0
#
#             have = False
#             for j in range(i, min(i + n, nn)):
#                 if A[j] < 0 and not have:
#                     k = j
#                     have = True
#                 if sum1 + A[j] > ans:
#                     ans = sum1 + A[j]
#
#                 if sum1 + A[j] > 0:
#                     sum1 += A[j]
#                 elif sum1 > 0:
#                     k = j
#                     break
#         # print(ans)
#         return ans

# a = Solution()
# q = a.maxSubarraySumCircular(A)
# print("q =",q)



A = [5,-3,5]
A = [-3,10,-4,3,-7,12,-4,5] # 正确答案 20

class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        A *= 2
        nn = len(A)

        k = -1
        ans = -999999

        left = 0
        right = 0
        sum1 = 0
        while left <= right and right < nn:

            if right - left == n:
                sum1 -= A[left]
                left += 1
            while A[left] <= 0 and left < right:
                if sum1 > 0:
                    sum1 -= A[left]
                left += 1
            if A[right] + sum1 > ans:

                ans = sum1 + A[right]
                if A[right] + sum1 > 0:
                    sum1 += A[right]
            elif A[right] + sum1 > 0:
                sum1 += A[right]
            else:
                sum1 = 0
                ans = max(A[right], ans)
                left = right
                # right += 1

            right += 1
        while left < right:
            sum1 -= A[left]
            if sum1 > ans:
                ans = sum1
            left += 1
        return ans







a = Solution()
q = a.maxSubarraySumCircular(A)
print("q =",q)