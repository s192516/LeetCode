#-*- coding:utf-8 -*-
#@Date   : 2018/7/16
#@Author : huali
#@File   : 14LongestCommonPrefix.py

#最长公共前缀
list = ['abc','aaa','aqw']
l1=[]
# list.reverse()
# print(list)

for l in list:
    # list.append(l[::-1])
    # print(1)
    # print(list)
    l1.append(l[::-1])

for num in range(len(l1)):
    print(1)