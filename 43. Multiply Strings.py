#-*- coding:utf-8 -*-
#@Date   : 2018/9/13
#@Author : suyifan
#@File   : 43. Multiply Strings.py

num1 = "1234"
num2 = "12"

num1 = "123"
num2 = "456"

num1 = "2"
num2 = "0"


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        length1 = len(num1)
        length2 = len(num2)
        jinwei = 0
        list1 = [[0 for x in range(length2)] for x in range(length1)]
        for i in range(length1):
            for j in range(length2):
                list1[i][j] = int(num1[i]) * int(num2[j])

        rtype = ""
        for qq in range(length1 + length2 - 1 ,1,-1):
            idx1 = max(0 ,qq - length2 )
            idx2 = qq -1 - idx1
            sum = jinwei
            jinwei = 0
            while idx1 < length1  and idx2 >= 0  :
                sum += list1[idx1][idx2]
                idx1 += 1
                idx2 -= 1

            rtype = str(sum)[-1] + rtype
            jinwei = sum // 10

        rtype = str(list1[0][0] + jinwei) + rtype

        return rtype

a = Solution()
q = a.multiply(num1,num2)
print("q=",q)


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        length1 = len(num1)
        length2 = len(num2)
        jinwei = 0
        list1 = [[0 for x in range(length2)] for x in range(length1)]
        for i in range(length1):
            for j in range(length2):
                list1[i][j] = int(num1[i]) * int(num2[j])

        rtype = ""
        for qq in range(length1 + length2 - 1 ,1,-1):
            idx1 = max(0 ,qq - length2 )
            idx2 = qq -1 - idx1
            sum = jinwei
            jinwei = 0
            while idx1 < length1  and idx2 >= 0  :
                sum += list1[idx1][idx2]
                idx1 += 1
                idx2 -= 1

            rtype = str(sum)[-1] + rtype
            jinwei = sum // 10

        rtype = str(list1[0][0] + jinwei) + rtype

        return rtype

a = Solution()
q = a.multiply(num1,num2)
print("q=",q)