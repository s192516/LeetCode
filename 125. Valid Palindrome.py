#-*- coding:utf-8 -*-
#@Date   : 2018/9/9
#@Author : suyifan
#@File   : 125. Valid Palindrome.py

s = "cattac"
s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "
s = ":::"
s = "0a"

#### 字母和数字!!!!不要只考虑字母
#### 没有字母和数字的字符串和空字符串都算True
#### 所以,不要想太多

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == []:
            return True

        i = 0
        j = len(s)-1
        s = s.lower()
        # print(s)
        while i < j:
            while ((ord(s[i]) <97 or ord(s[i])>122) and ( ord(s[i]) >57 or ord(s[i]) < 48))and i < j:
                i += 1
            # if  ord(s[i]) <97 or ord(s[i])>122:
            #     return False
            # while (ord(s[j]) <96 or ord(s[j])>122) and i < j:
            while ((ord(s[j]) < 97 or ord(s[j]) > 122) and (ord(s[j]) > 57 or ord(s[j]) < 48)) and i < j:

                j -= 1
            # if ord(s[j]) <96 or ord(s[j])>122:
            #     return False
            # if i > j or i>len(s)-1 or j < 0:
            #     return False

            if s[i] == s[j] :
                i += 1
                j -= 1
            else:
                return False

        return True


a = Solution()
q = a.isPalindrome(s)
print("q=",q)