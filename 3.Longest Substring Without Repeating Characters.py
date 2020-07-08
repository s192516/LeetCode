#-*- coding:utf-8 -*-
#@Date   : 2018/9/5
#@Author : huali
#@File   : 3.Longest Substring Without Repeating Characters.py
#
# s = "au"
# s ="jbpnbwwd"


# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         max_length = 0
#         # length = 0
#         for i in range(len(s)):
#             length = 1
#             str_temp = s[i]
#             for j in range(i+1,len(s)):
#                 if not (s[j] in str_temp):
#                     str_temp +=s[j]
#                     length += 1
#                 else :
#                     if length > max_length:
#                         max_length = length
#                         length = 1
#                     break
#
#             if length > max_length:
#                 max_length = length
#                 length = 1
#
#         return max_length



# s = "au"
# s ="jbpnbwwd"
# s ="advds"
# s ="abcabcbb"
# s = "bbb"
# s = "aab"
# s = "bba"
# s = "pwwkew"
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         max_length = 0
#         temp_str = ""
#         len_str = len(s)
#         # for  i in  range(len(s)):
#         # abcb
#         i,j = 0,0 #i 快指针,j慢指针
#         while i < len_str and j < len_str:
#            if s[i] in temp_str:
#                length = i - j
#                if length > max_length:
#                    max_length = length
#
#                j += 1
#                temp_str = temp_str[1:]
#
#                continue
#            else:
#                temp_str += s[i]
#                i += 1
#
#         if len(temp_str) > max_length:
#             max_length = len(temp_str)
#
#         return max_length
# a = Solution()
# q = a.lengthOfLongestSubstring(s)
# print("q=",q)


s = "au"
s ="jbpnbwwd"
# s ="advds"
# s ="abcabcbb"
# s = "bbb"
# s = "aab"
# s = "bba"
# s = "pwwkew"
# s = "ohomm"
# s = "abba"
# s = "tmmzuxt"
#

# sss = "qqq"
# dict1 = {}
# dict1[sss[1]] = 1
# print(dict1[sss[1]]-1)
# print(len(dict1.keys()))

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         dict1 = {}
#         max_length = 0
#         temp,index = 0,0
#         length = 0
#         i = 0
#         while i < len(s):
#             if s[i] in dict1:
#                 length = i - index
#                 index += 1
#                 dict1[s[i]] = i
#                 # i -= 1
#                 # continue
#             else :
#                 dict1[s[i]] = i
#             temp = index
#             if length > max_length:
#                 max_length = length
#             i += 1
#
#         print(len(s)-index,"---")
#         if len(s)-index > max_length:
#             max_length = len(s) - index
#
#         return max_length

# a = Solution()
# q = a.lengthOfLongestSubstring(s)
# print("q=",q)


# s = "abba"
s = "abbcabdabcdab"
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {}
        idx = 0
        ans = 0
        for i,c in enumerate(s):
            if c in dict1:
                idx = max(dict1[c]+1,idx)
            ans = max(ans,i-idx+1)
            dict1[c] = i
        return ans


        dict1 = {}
        j = 0
        ans = 0
        for i in range(len(s)):
            if s[i] in dict1:
                j = max(dict1[s[i]] + 1,j)
            ans = max(ans, i - j + 1)
            dict1[s[i]] = i
        return ans


a = Solution()
q = a.lengthOfLongestSubstring(s)
print("q=",q)
