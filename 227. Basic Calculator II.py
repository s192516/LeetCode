#-*- coding:utf-8 -*-
#@Date   : 2018/10/29
#@Author : suyifan
#@File   : 227. Basic Calculator II.py

s = "33 + 2/3"
s = "33+2*2"
s = "3"
s = "0"
s = "1*1"
s = " 3/2 "
s = "1+2*3+4*5+6*7+8*9+10"
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = []
        nums = []
        num_str = ""
        for i in s:
            if i == " ":
                continue
            if 48 <= ord(i) <= 57:
                num_str += i
            else:
                # print(i == "/")
                # if symbols:
                #     print("ss")
                # if symbols and (symbol[-1] == "*" or symbol[-1] == "/"):# 字符串永远合法
                if symbols and symbols[-1] == "*":
                    nums[-1] = nums[-1] * int(num_str)
                    symbols = symbols[:-1]

                elif symbols and symbols[-1] == "/":
                    nums[-1] = nums[-1] // int(num_str)
                    symbols = symbols[:-1]
                else:
                    nums.append(int(num_str))
                num_str = ""
                symbols.append(i)

        nums.append(int(num_str))
        if symbols and symbols[-1] == "*":
            # nums[-2] = nums[-2] * int(num_str)
            nums[-2] = nums[-2] * nums[-1]
            nums = nums[:-1]
            symbols = symbols[:-1]
            # symbols = symbols[:-1]
        elif symbols and symbols[-1] == "/":
            # nums[-1] = nums[-1] // int(num_str)
            nums[-2] = nums[-2] // nums[-1]
            nums = nums[:-1]
            symbols = symbols[:-1]

            # symbols = symbols[:-1]

        rtype = nums[0]
        if symbols:
            for i in range(1, len(nums)):
                if symbols[i - 1] == "+":
                    rtype += nums[i ]
                else:
                    rtype -= nums[i ]
        return rtype

a = Solution()
q = a.calculate(s)
print("q =",q)