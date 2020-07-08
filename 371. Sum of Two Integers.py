#-*- coding:utf-8 -*-
#@Date   : 2018/11/8
#@Author : suyifan
#@File   : 371. Sum of Two Integers.py


a = 20
b = 13

# a = 1
# b = 1
#
# a = 8
# b = 16

a = 0
b = 13

a = -8
b = -16

a = -8
b = 16
###自己写的错误答案
# class Solution:
#     def getSum(self, a, b):
#         """
#         :type a: int
#         :type b: int
#         :rtype: int
#         """
#         temp = 0
#         rtype = 0
#         count = 1
#         while a or b:
#             a1 = a % 2
#             b1 = b % 2
#
#             num = (a1 ^ b1 ^ temp)
#             # print("temp =",temp)
#             rtype = rtype  ^ (num and count)
#
#             # print((a1 & b1) , (a1 & temp) , (b1 and temp) , (a1 & b1 & temp))
#             if (a1 & b1) or (a1 & temp) or (b1 and temp) or (a1 & b1 & temp):
#                 temp = 1
#             else:
#                 temp = 0
#
#             if a == -1:
#                 a = 0
#             if b == -1:
#                 b = 0
#
#             a = a >> 1
#             b = b >> 1
#
#             # print("rtype = ",rtype)
#             count = count << 1
#
#
#         if temp:
#             rtype = rtype ^ count
#         return rtype
#
# s = Solution()
# q = s.getSum(a,b)
# print("q =",q)


a = -8
b = 16
class Solution:
    def getSum(self, a, b):
        # if(b == 0 ) :
        #     return a
        #
        # return self.getSum(a^b, (a&b)<<1);
        while (a):

            x = a ^ b
            a = (a & b) << 1
            b = x

        return b


s = Solution()
q = s.getSum(a,b)
print("q =",q)