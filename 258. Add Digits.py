#-*- coding:utf-8 -*-
#@Date   : 2018/9/12
#@Author : suyifan
#@File   : 258. Add Digits.py


#从第一位开始加,当大于10之后就把这个两位数的个位和十位相加求一个一位数
#一直加到最后
#注意考虑 n <10的情况

#当n = 0时候直接返回0
# 当n != 0时候,各位之和相加永远都不可能相加等于0
#也就是说最后结果只能是1-9中的一个数字,而且1-9循环
#那么只要看他除以9 的余数就可以
# 但是余数为零的时候不可以返回0,而是要返回9
#为了保证这种情况就用减一加一法
#return (num-1) % 9 +1就可


# num = 999
#
# class Solution(object):
#     def addDigits(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         num = str(num)
#         length = len(num)
#         rtype = 0
#         str(type)
#         for i in range(length):
#             if rtype < 10:
#                 rtype += int(num[i])
#             else:
#                 rtype = int(str(rtype)[0]) + int(str(rtype)[1]) + int(num[i])
#
#         if rtype >= 10:
#             rtype = int(str(rtype)[0]) + int(str(rtype)[1])
#         return rtype
#
#
# a = Solution()
# q = a.addDigits(num)
# print("q=",q)


num = 1

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        rtype = num
        while num >= 10:
            rtype = 0
            num = str(num)
            length = len(num)
            for i in range(length):
                rtype += int(num[i])
            num = rtype
        return rtype


a = Solution()
q = a.addDigits(num)
print("q=",q)
