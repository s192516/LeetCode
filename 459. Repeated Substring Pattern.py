#-*- coding:utf-8 -*-
#@Date   : 2018/10/7
#@Author : suyifan
#@File   : 459. Repeated Substring Pattern.py


s = "abcabc"

class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        # count = 0
        # i = 1
        for i in range(1,length//2 + 1):
            count = 0
            if length % i == 0:
                while count + i <= length and s[ count:count + i] == s[:i]:
                    count += i
                if count == length:
                    return True
            # elif length / i < 2:
            #     return False
        return False

a = Solution()
q = a.repeatedSubstringPattern(s)
print("q =",q)