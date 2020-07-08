#-*- coding:utf-8 -*-
#@Date   : 2018/11/23
#@Author : suyifan
#@File   : 76. Minimum Window Substring.py

s = "ADOBECODEBANC"
t = "ABC"

s = "a"
t = "a"

s = "a"
t = "aa"

s = "ab"
t = "a"
s = "cabwefgewcwaefgcf"
t = "cae"

s = "cabeecf"
t = "cae"
# class Solution:
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         def have():
#             for k,v in t_dict.items():
#                 if s_dict.get(k,0) < v:
#                     return False
#             return True
#         s_dict = {}
#         t_dict = {}
#         ans = 9999999
#         rtype = ""
#         for i in t:
#             t_dict[i] = t_dict.get(i,0) + 1
#         t_len = len(t)
#         s_len = len(s)
#         left = 0
#         right = 0
#         end = len(s)
#         while left + t_len <= end and right<s_len:
#             while not have() and right < s_len:
#                 s_dict[s[right]] = s_dict.get(s[right],0) + 1
#                 right += 1
#             # if have():
#             #     n = right -left
#             #     if n < ans :
#             #         ans = n
#             #         rtype = s[left:right]
#
#             while have():
#                 n = right -left
#                 if n < ans :
#                     ans = n
#                     rtype = s[left:right]
#                 s_dict[s[left]] = s_dict.get(s[left], 0) - 1
#                 left += 1
#
#
#             # while not t_dict.get(s[left],0) :
#             #     left += 1
#             # s_dict[s[left]] = s_dict.get(s[left],0) - 1
#
#
#         return rtype
#
# print(s,"\n"+t)
# a = Solution()
# q = a.minWindow(s,t)
# print("q =",q)



#
# s = "ADOBECODEBANC"
# t = "ABC"


# class Solution:
# #     def minWindow(self, s, t):
# #         """
# #         :type s: str
# #         :type t: str
# #         :rtype: str
# #         """
# #         cnt = [0]*128
# #         for i in t:
# #             cnt[ord(i)] += 1
# #         print(cnt)
# #         total = len(t)
# #
# #         left = 0
# #         right = 0
# #         j = 0
# #         min_length = 999999999
# #         for i,c in enumerate(s):
# #             idx_c = ord(c)
# #             if cnt[idx_c]  > 0: #大于还是不等于?
# #                 total -= 1
# #             cnt[idx_c] -= 1
# #             while total == 0:
# #                 if i - j + 1< min_length:
# #                     min_length = i-j+1
# #                     left = j
# #                 num = ord(s[j])
# #                 cnt[num] += 1
# #                 if cnt[num] > 0:
# #                     total += 1
# #                 j += 1
# #                 # right = i
# #                 # num = cnt[ord(s[left])]
# #                 # if num == 0:
# #                 #     if right-i+1 < min_length:
# #                 #         min_length = right - i + 1
# #                 #     total += 1
# #                 # cnt[num] += 1
# #                 # if cnt[num] > 0:
# #                 #     total += 1
# #                 # left += 1
# #         if min_length == 999999999:
# #             print("qqq")
# #             return ""
# #         else:
# #             print(left,min_length)
# #             return s[left:left+min_length]
# # print(s,"\n"+t)
# # a = Solution()
# # q = a.minWindow(s,t)
# # print("q =",q)

#---------------正确的-----------
# class Solution:
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         cnt = [0]*128
#         for i in t:
#             cnt[ord(i)] += 1
#         print(cnt)
#         total = len(t)
#
#         left = 0
#         min_length = 999999999
#
#         for i,c in enumerate(s):
#             idx_1 = ord(c)
#             if cnt[idx_1] > 0:
#                 total -= 1
#             cnt[idx_1] -= 1
#
#             while total == 0:
#                 right = i
#                 if right-left+1 < min_length:
#                     min_length = right-left+1
#                 idx_2 = ord(s[left])
#                 cnt[idx_2] += 1
#                 if cnt[idx_2] > 0:
#                     total += 1
#                     begin = left
#                 left += 1
#
#         if min_length == 999999999:
#             return ""
#         else:
#             # print(left,right,min_length)
#             return s[begin:begin+min_length]
#
# print(s,"\n"+t)
# a = Solution()
# q = a.minWindow(s,t)
# print("q =",q)
#




s = "ADOBECODEBANC"
t = "ABC"

#---------------------练习---------------------
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        array = [0] * 128
        for i in t:
            array[ord(i)] += 1
        total = len(t)

        left = 0
        right = 0
        s_len = len(s)
        min_len = 1e20
        while right < s_len:
            if array[ord(s[right])] > 0:
                total -= 1
            array[ord(s[right])] -= 1
            right += 1

            while total == 0:
                idx_left = ord(s[left])
                array[idx_left] += 1
                if array[idx_left] > 0 :
                    total += 1
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    begin = left
                left += 1

        if min_len != 1e20:

            return s[begin:begin+min_len]
        else:
            return -1

# print(s,"\n"+t)
a = Solution()
q = a.minWindow(s,t)
print("q =",q)