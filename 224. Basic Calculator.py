#-*- coding:utf-8 -*-
#@Date   : 2018/11/8
#@Author : suyifan
#@File   : 224. Basic Calculator.py

s = " 2-1 + 2 "
# s = "(1+(4+5+2)-3)+(6+8)"
s = "2-(5-6)"
s = "234"
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        nums_stack = []
        symbols_stack = []

        res,num,sign,satck = 0,0,1,[]

        for i in s:
            if i == " ":
                continue
            elif i == "+":
                res += sign * num
                sign = 1
                num = 0
            elif i == "-":
                res += sign * num
                sign = -1
                num = 0
            elif i == "(":
                # res += sign * num
                nums_stack.append(res)
                symbols_stack.append(sign)
                res = 0
                sign = 1
            elif i == ")":
                res += sign * num
                num = res
                res = nums_stack.pop()
                sign = symbols_stack.pop()
                # res += sign * num
                # num = 0
            else:
                num = num * 10 +int(i)
        res += sign * num
        return res
a = Solution()
q = a.calculate(s)
print("q =",q)