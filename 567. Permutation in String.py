#-*- coding:utf-8 -*-
#@Date   : 2018/11/14
#@Author : suyifan
#@File   : 567. Permutation in String.py

s1 = "ab"
s2 = "eiooba"

s1 = "a"
s2 = "c"


#### 这是正确的版本
# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         n1 = len(s1)
#         n2 = len(s2)
#         if n1 > n2:
#             return False
#
#         list_s1 = [0] * 26
#         list_s2 = [0] * 26
#         for i in s1:
#             list_s1[ord(i) - ord("a")] += 1
#
#         # print(list_s1)
#         for i in s2[:n1]:
#             list_s1[ord(i) - ord("a")] -= 1
#
#         if self.check(list_s1):
#             return True
#         # print(list_s1)
#
#         left = 0
#         right = n1
#         while right < n2 :
#             list_s1[ord(s2[left]) - ord("a")] += 1
#             list_s1[ord(s2[right]) - ord("a")] -= 1
#             if self.check(list_s1):
#                 return True
#             left += 1
#             right += 1
#         return False
#
#     def check(self, list_s1):
#         n = 0
#         for i in list_s1:
#             if i == 0:
#                 n += 1
#         if n == 26:
#             return True
#         else:
#             return False


# a = Solution()
# q = a.checkInclusion(s1,s2)
# print("q =",q)

s1 = "ab"
s2 = "eiooba"
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def solve():
            for i in list_1:
                if i != 0:
                    return False
            return True

        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        list_1 = [0] * 26

        for i in s1:
            list_1[ord(i) - ord("a")] += 1

        for i in range(n1):
            list_1[ord(s2[i]) - ord("a")] -= 1
        if solve():
            return True

        for i in range(n1, n2):

            list_1[ord(s2[i]) - ord("a")] -= 1
            list_1[ord(s2[i - n1]) - ord("a")] += 1
            if solve():
                return True

        return False


a = Solution()
q = a.checkInclusion(s1,s2)
print("q =",q)
