#-*- coding:utf-8 -*-
#@Date   : 2018/9/6
#@Author : huali
#@File   : 709. To Lower Case.py


str = "Hello world!"

class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        # A = 65,Z = 90
        str1 = ""
        self.str = str


        for i in self.str :
            if ord(i) >=65 and ord(i) <= 90:
                str1 += chr(ord(i)+32)
            else :
                str1 += i
        return str1




a = Solution()
q = a.toLowerCase(str)
print("q=",q)