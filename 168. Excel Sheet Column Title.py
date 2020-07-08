#-*- coding:utf-8 -*-
#@Date   : 2018/9/12
#@Author : suyifan
#@File   : 168. Excel Sheet Column Title.py

#10进制转化26进制,
#这个26进制没有0,却有26也就是说z
#当n为26倍数时会导致商+1,所以要先减一再除26
#记得把减去的1,在下一轮加回来
n = 27
n = 1
n = 28
n = 701
n = 26
n = 676
n = 650
n = 52
n = 17576
n = 26 * 26
n = 99999

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        str1 = ""
        str2 = ""
        count = True
        # n += 1
        while n >26:
            if count == True:
                q = n  % 26
                count = False
                if q == 0:
                    q = 26
            else :

                q = n % 26
                if q == -1:
                    q = 26

            # print(chr(q + 64),q,n)
            str1 += chr(q + 64)
            str2 = str1 + str2
            str1 = ""
            n = (n - 1) //26
            # if n <= 26:
            #     n = q

            # count += 1
        # if count == True:
        str1 += chr(n + 64 )
        str2 = str1 + str2
        # else :
        #     str1 += chr(n - 1 + 64)
        #     str2 = str1 + str2
        return str2
a = Solution()
q = a.convertToTitle(n)
print("q=",q)