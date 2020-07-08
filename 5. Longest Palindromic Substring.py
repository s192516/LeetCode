#-*- coding:utf-8 -*-
#@Date   : 2018/9/22
#@Author : suyifan
#@File   : 5. Longest Palindromic Substring.py



s = "abbcbbb"
s = "cbbd"
# s = "a"
# s = ""
# s = "bb"
s = "ccc"

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        rtype = ""

        count = 0
        for i in range(length):
            idx1 = i - 1
            idx2 = i + 1
            temp = s[i]
            temp_count = 1
            if temp_count > count:
                count = temp_count
                rtype = temp
            while idx1 >= 0 and idx2 <= length - 1:
                if s[idx1] == s[idx2]:
                    temp = s[idx1] + temp + s[idx2]
                    temp_count += 2
                    if temp_count > count:
                        rtype = temp
                        count = temp_count
                else:
                    break
                idx1 -= 1
                idx2 += 1

        for i in range(length - 1):
            if s[i] == s[i + 1]:
                temp_count = 2
                temp = s[i] + s[i]
                if temp_count > count:
                    rtype = temp
            else:
                continue
            idx1 = i - 1
            idx2 = i + 2
            while idx1 >= 0 and idx2 <= length - 1:
                if s[idx1] == s[idx2]:
                    temp_count += 2
                    temp = s[idx1] + temp + s[idx1]
                    if temp_count > count:
                        count = temp_count
                        rtype = temp
                else:
                    break
                idx1 -= 1
                idx2 += 1

        return rtype

a = Solution()
q = a.longestPalindrome(s)
print("q=",q)