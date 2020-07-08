#-*- coding:utf-8 -*-
#@Date   : 2018/9/20
#@Author : suyifan
#@File   : 171. Excel Sheet Column Number.py


s = "AAA"
s = "A"
s = "AB"
# s = "ZY"
# print(ord("A"),ord("Z"))

# class Solution:
#     def titleToNumber(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         dict1 ={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
#         count = 0
#         rtype = 0
#         # while s != "":
#         #     rtype += (ord(s[-1]) - 64) * (26 ** count)
#         #     count += 1
#         #     s = s[:-1]
#
#         s = s[::-1]
#         for i in s:
#             rtype += dict1[i] * (26 ** count)
#             # rtype += (ord(i) - 64) * (26 ** count)
#             count += 1
#             # s = s[:-1]
#
#
#         return rtype
#
#
# a = Solution()
# q = a.titleToNumber(s)
# print("q=",q)

s = "AA"
s = "ZY"
class Solution:
    def titleToNumber(self, s):

        count = len(s) - 1
        rtype = 0
        for i in s:
            rtype = (ord(i) - 64) + (rtype * 26)
            count -= 1

        return rtype


a = Solution()
q = a.titleToNumber(s)
print("q=",q)
