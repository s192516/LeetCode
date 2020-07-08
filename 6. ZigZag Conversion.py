#-*- coding:utf-8 -*-
#@Date   : 2018/9/23
#@Author : suyifan
#@File   : 6. ZigZag Conversion.py

s = "PAYPALISHIRING"
numRows = 3

# s = "PAYPALISHIRING"
# numRows = 4

s = "PAYPALISHIRING"
numRows = 1

s = "ABC"
numRows = 3

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rtype = ""
        if numRows == 1:
            return s
        for i in range(numRows):
            j = i
            while j < len(s):
                rtype +=  s[j]
                j += (2 * numRows - 2 * (i + 1) )
                if i != 0 and i != numRows -1:
                    if j >= len(s):
                        break
                    else:
                        rtype += s[j]
                        j += 2 * i
                if  i == numRows - 1:
                    j += 2 * numRows - 2

                # print(rtype,j)
        return rtype

print(s)
a = Solution()
q = a.convert(s,numRows)
print("q= ",q)