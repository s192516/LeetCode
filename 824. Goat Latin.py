#-*- coding:utf-8 -*-
#@Date   : 2018/10/14
#@Author : suyifan
#@File   : 824. Goat Latin.py



S = "I speak Goat Latin"
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        set1 = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        # set1 = set("aeiouAEIOU")
        k = 1
        begin = True
        rtype = ""
        for i in S:
            if begin:
                if i in set1:
                    tail = "ma" + "a" * k
                    rtype += i
                else:
                    tail = i + "ma" + "a" * k
                begin = False
            else:
                if i == " ":
                    begin = True
                    rtype += tail + " "
                    k += 1
                    tail = ""
                else:
                    begin == False
                    rtype += i
        rtype += tail
        return rtype
print(S)
a = Solution()
q = a.toGoatLatin(S)
print("q =",q)