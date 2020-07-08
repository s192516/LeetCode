#-*- coding:utf-8 -*-
#@Date   : 2018/7/16
#@Author : huali
#@File   : 13RomanToInteger.py

#罗马数字
import sys
dict1 ={"I":1,"V":5,"X" : 10,"L":50,"C":100,"D":500,"M":1000}
# IV
#VI
str1 = input()
list1 =list(str1)
sum = 0
temp = sys.maxsize
# print(temp)
for item in list1:
    if dict1[item] <=temp:
        sum +=dict1[item]
    else :
        sum = sum+dict1[item]-2*temp
    temp = dict1[item]
print(sum)
