#-*- coding:utf-8 -*-
#@Date   : 2018/7/16
#@Author : huali
#@File   : 7ReverseInteger.py

import sys
print(sys.maxsize)
x = 1534236469
rev = 0

y= abs(x)
while y != 0:
    pop = y %10
    y //= 10
    rev= rev*10+pop

if x<0:
    rev *=-1

if rev>sys.maxsize or rev< (-sys.maxsize - 1):
    # return 0
    print(rev)

else:
    # return rev
    print(rev)
