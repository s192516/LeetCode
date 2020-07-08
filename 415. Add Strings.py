#-*- coding:utf-8 -*-
#@Date   : 2018/10/12
#@Author : suyifan
#@File   : 415. Add Strings.py


num1 = "0"
num2 = "0"

num1 = "10"
num2 = "9"

num1 = "99999"
num2 = "1"

# num1 = "15579999999"
# num2 = "1"

num1 = "8999"
num2 = "1"

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        jinwei = 0
        rtype = ""
        len1 = len(num1)
        len2 = len(num2)
        if len1 > len2:
            long1 = num1[:len1 - len2 ]
            len_short = len2
        else:
            long1 = num2[:len2 - len1 ]
            len_short = len1


        while len_short > 0:
            count = int(num1[-1]) + int(num2[-1]) + jinwei
            if count > 9:
                jinwei = 1
            else:
                jinwei = 0
            count = str(count % 10)
            rtype = count + rtype
            num1 = num1[:-1]
            num2 = num2[:-1]
            len_short -= 1

        print("long1=",long1,"rtype=",rtype)
        if jinwei != 0:
            while jinwei and long1:
                if long1[-1] == "9":
                    rtype = "0" + rtype
                    long1 = long1[:-1]
                else:
                    rtype = long1[:-1] + str(int(long1[-1]) + 1) + rtype
                    return rtype
            if jinwei:
                return "1" + rtype
            else:
                return rtype
        else:
            return long1 + rtype

        # rtype = "1" + rtype

print("num1=",num1,num2)
a = Solution()
q = a.addStrings(num1,num2)
print("q =",q)