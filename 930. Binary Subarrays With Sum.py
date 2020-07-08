#-*- coding:utf-8 -*-
#@Date   : 2018/10/29
#@Author : suyifan
#@File   : 930. Binary Subarrays With Sum.py

# A = [1,1,1,0,0,1,1,1,0,1,0,1,1,1,1,0]
# S = 3

# A = [1,1,1,0,0,1]
# S = 3

# A = [1,1,1,0,0,1]
# S = 0

# A = [0,0,1,0,0]
# S = 1
# S = 0
#
# A = [0,1,1,1,1]
# S = 3
# class Solution:
#     def numSubarraysWithSum(self, A, S):
#         """
#         :type A: List[int]
#         :type S: int
#         :rtype: int
#         """
#         sum_all = sum(A)
#         if sum_all < S:
#             return 0
#         left = 0
#         n = len(A)
#         # 数组为[],S = -1报错
#         if n == 0:
#             return 0
#
#         left = 0
#         right = 0
#         count = 0
#         finish = False
#         #S == 0 单独算
#
        # if S == 0:
        #     idx = 0
        #     while idx < n:
        #         # if A[idx] == 0:
        #         while idx < n and A[idx] == 1:
        #             idx += 1
        #             if idx == n:
        #                 finish = True
        #         zero = 0
        #         for i in range(idx,n):
        #
        #             if i == n - 1:
        #                 finish = True
        #             if A[i] == 0:
        #                 zero += 1
        #             else:
        #                 idx = i
        #                 break
        #         count += (zero+1) * zero // 2
        #         if finish:
        #             return count
#
#         # S -= A[0]
#         while left <= right or right < n:
#             if (right == n and S > 0) or left == n :
#                 return count
#             if S > 0:
#                 plus_right = 1
#                 plus_left = 0
#                 S -= A[right]
#                 right += 1
#             elif S < 0:
#                 plus_left = 1
#                 plus_right = 0
#                 S += A[left]
#                 left += 1
#             else:
#                 count += 1
#                 if right < n:
#                     if A[right] == 0:
#                         S -= A[right]
#                         right += 1
#                     else:
#                         S += A[left]
#                         left += 1
#                 else:
#                     # if plus_left:
#                     S += A[left]
#                     left += 1
#                     # else:
#                     #     S -= A[right]
#                     #     right += 1
#             # if S == 0 and left != right:
#             #     count += 1
#         return count
#
# a = Solution()
# q = a.numSubarraysWithSum(A,S)
# print("q =",q)

A = [1,1,1,0,0,1,1,1,0,1,0,1,1,1,1,0] # rtype = 20
S = 3

A = [1,1,1,0,0,1]
S = 3
#
A = [1,1,1,0,0,1]
S = 0
#
A = [0,0,1,0,0] # rtype = 9
S = 1
S = 0
# #
# A = [0,1,1,1,1]
# S = 3

A = [1,0,1,0,1] # rtype = 4
S = 2
class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        rtype = 0
        n = len(A)
        if n == 0:
            return 0
        sum_all = sum(A)
        if sum_all < S:
            return 0
        finish = False
        count = 0
        if S == 0:
            idx = 0
            while idx < n:
                # if A[idx] == 0:
                while idx < n and A[idx] == 1:
                    idx += 1
                    if idx == n:
                        finish = True
                zero = 0
                for i in range(idx,n):

                    if i == n - 1:
                        finish = True
                    if A[i] == 0:
                        zero += 1
                    else:
                        idx = i
                        break
                count += (zero+1) * zero // 2
                if finish:
                    return count



        left = 0
        while left < n:
            sum1 = 0
            for j in range(left, n):
                if sum1 == S:
                    count_right = 0
                    idx_right = j
                    while idx_right < n and A[idx_right] == 0:
                        count_right += 1
                        idx_right += 1
                    idx = left
                    count_left = 0
                    while idx < j and A[idx] == 0:
                        count_left += 1
                        idx += 1
                    rtype += (count_left + 1) * (count_right + 1)
                    left = idx + 1
                    break
                if sum1 < S:
                    sum1 += A[j]
                else:
                    left += 1
                    break
                if j == n - 1:
                    if sum1 == S:
                        idx = left
                        count_left = 0
                        while idx < j and A[idx] == 0:
                            count_left += 1
                            idx += 1

                        rtype += count_left + 1
                    return rtype
        return rtype


a = Solution()
q = a.numSubarraysWithSum(A,S)
print("q =",q)