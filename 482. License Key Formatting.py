#-*- coding:utf-8 -*-
#@Date   : 2018/10/13
#@Author : suyifan
#@File   : 482. License Key Formatting.py



S = "5F3Z-2e-9-w123456"
K = 4
S = "5F3Z-2e-9-w"
K = 10
S = "5F3Z-2e-9-w"
K = 4

S = "2-4A0r7-4k"
K = 3

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        count = 0
        for i in S:
            if i != "-":
                count += 1

        yushu = -count % K
        len1 = count // K
        print("yushu=",yushu,count)
        rtype = ""
        for i in S:

            if i != "-":
                if yushu % K == 0 and yushu != 0 and len1 > 0:
                    rtype += "-"
                if 96 < ord(i) < 123:
                    print(chr(ord(i)-32))
                    rtype += chr(ord(i) - 32)
                else:
                    rtype += i
                yushu += 1

        return rtype
print(S,K)
a = Solution()
q = a.licenseKeyFormatting(S,K)
print("q =",q)