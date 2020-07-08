#-*- coding:utf-8 -*-
#@Date   : 2018/9/5
#@Author : huali
#@File   : 8.StringToInteger.py


str1 = "  -4 and 987"
str1 = "43"
str1 = "   -42"
str1 = "4193 with words"
str1 = "words and 987"
str1 = "-91283472332"
str1 = "  0000000000012345678"
str1 = "2147483646"
# str1 = "   -42sdfz"
# str1 = "  "
# str1 = "  +1"


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip(" ")
        str2 = str.split(" ")[0]
        int2 = 0
        try :
            if str2[0] =="-":
                rtype = -1
                str2 = str2[1:]
            elif str2[0] == "+" :
                str2 = str2[1:]
                rtype = 1
            else :
                rtype = 1
        except:
            return 0
        for i in range(len(str2)):
            try:
                int2 = int2 * 10 +rtype * int(str2[i])
            except:
                break

        rtype = int2
        print(int2)
        if int2 >2147483646:
            rtype = 2147483647
        elif int2 < -2147483648:
            rtype = -2147483648



        return rtype

a = Solution()
q = a.myAtoi(str1)
print("q=",q)