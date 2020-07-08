#-*- coding:utf-8 -*-
#@Date   : 2018/7/16
#@Author : huali
#@File   : 9.PalindromeNumber.py

#回文数
# x =123321
# y= x
# rev = 0
# if x <0 :
#     # return False
#     print(False)
# else:
#     while y != 0:
#         pop = y % 10
#         y //= 10
#         rev = rev * 10 + pop
#     if rev == x:
#         # return True
#         print(True)
#     else:
#         # return(False)
#         print(False)


#方法二
x =123321
y = str(x)
result = y[::-1]
result =int(result)
# print(result)

if x == result:
    print(True)
else:
    print(False)
