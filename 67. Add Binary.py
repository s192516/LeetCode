#-*- coding:utf-8 -*-
#@Date   : 2018/9/4
#@Author : huali
#@File   : 67. Add Binary.py

a ="10"
b = "101111"

# print(len(b))
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        q =len(a)
        w =len(b)
        n = min(q,w)
        m = max(q,w)
        m -= n
        str1 = ""
        add_num =0
        while n > 0:
            int_a = int(a[-1])
            int_b = int(b[-1])
            if int_a + int_b + add_num ==2  :
                str1 +="0"
                add_num = 1
            elif int_a + int_b + add_num ==3:
                str1 +="1"
                add_num = 1
            else:
                str1 += str(int_a + int_b+add_num)
                add_num = 0
            n -= 1
            a = a[:-1]
            b = b[:-1]
        if q > w :
            str_left = a[:m]
        elif q < w:
            str_left = b[:m]

        while m >0:
            int_c = int(str_left[-1])
            if int_c +add_num ==2:
                str1 += "0"
                add_num = 1
            else:
                str1 += str(int_c+add_num)
                add_num = 0
            m -= 1
            str_left = str_left[:-1]


        if add_num == 1:
            str1 += "1"
        # print("str1 =",str1)
        rtype = ""
        for i in range(len(str1)):
            rtype += str1[len(str1)-1-i]

        return rtype



qqq = Solution()
q = qqq.addBinary(a,b)
print("q=",q)