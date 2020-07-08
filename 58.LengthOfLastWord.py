#-*- coding:utf-8 -*-
#@Date   : 2018/9/3
#@Author : huali
#@File   : 58.LengthOfLastWord.py

s= "    "
# s=""
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1 = s.split(" ")
        rtype = 0
        if list1 == [""]:
            rtype =  0
        else :
            i = len(list1)-1
            while i>=0:
                if list1[i] != "":
                    return len(list1[i])
                i -=1

        return rtype

a = Solution()
q = a.lengthOfLastWord(s)
print(q)



