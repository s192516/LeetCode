#-*- coding:utf-8 -*-
#@Date   : 2018/7/16
#@Author : huali
#@File   : 3th快速排序.py#


#
# class ListNode():
#     def __init__(self,val):
#         self.val = val
#         self.next = None
#
# l1 = None
# temp = ListNode(6)
# temp.next = l1
# l1 = temp
# temp = ListNode(5)
# temp.next = l1
# l1 = temp
# temp = ListNode(4)
# temp.next = l1
# l1 = temp
# temp = ListNode(3)
# temp.next = l1
# l1 = temp
# temp = ListNode(2)
# temp.next = l1
# l1 = temp
# temp = ListNode(1)
# temp.next = l1
# l1 = temp
#
#
#
# temp = l1








# l2 = None
# temp = ListNode(5)
# temp.next = l2
# l2 = temp
# temp = ListNode(4)
# temp.next = l2
# l2 = temp
# temp = ListNode(3)
# temp.next = l2
# l2 = temp
# temp = ListNode(2)
# temp.next = l2
# l2 = temp
# temp = ListNode(1)
# temp.next = l2
# l2 = temp
# temp = ListNode(0)
# temp.next = l2
# l2 = temp


# temp1 = ListNode(None)
# temp1.next = None
# ll1 = temp1
# temp = ListNode(5)
# temp.next = ll1
# ll2 = temp
# temp = ListNode(4)
# temp.next = ll2
# ll3 = temp
# temp = ListNode(3)
# temp.next = ll3
# ll4 = temp
# temp = ListNode(2)
# temp.next = ll4
# ll5 = temp
#
# temp = ListNode(1)
# temp.next = ll5
# ll6 = temp
#
# temp = ListNode(0)
# temp.next = ll6
# ll7 = temp
#
#
#
#
# temp = ll7
# while temp != None:
#     print(temp.val,"->",end="")
#     temp =temp.next

# old_probe = l1
# new_probe = None
# count = 0
# while count <2:
#     temp = old_probe.next
#     old_probe.next = new_probe
#     new_probe = old_probe
#     old_probe = temp
#     count += 1

# old_probe = l1
# new_probe = None
# count = 0
# length = 5
# k = 2
# while count < length - k:
#     temp = ListNode(old_probe.val)
#     temp.next = new_probe
#     new_probe = temp
    # new_probe.next = old_probe.next
    # old_probe = old_probe.next
    # count += 1


# new_l1 = new_probe
# while new_l1 != None:
#     print(new_l1.val,"->",end="")
#     new_l1 = new_l1.next

#
#
# class ListNode():
#     def __init__(self,x,left = None,right = None):
#         self.val = x
#         self.left = left
#         self.right = right
#
#
# temp = ListNode(5)
# l1 = ListNode(3,temp)
# temp = ListNode(2)
# l1 = ListNode(1,l1,temp)
# probe = l1
# class Solution():
#     def __init__(self):
#         self.rtype = ListNode(0)
#
#     def print1(self,lq):
#         if not lq :
#             return None
#
#         print(lq.val,end="...")
#         self.print1(lq.left)
#         self.print1(lq.right)
#
#     def merge(self,l1):
#         if not l1 :
#             return None
#         temp = ListNode(l1.val)
#         temp.left = l1.left
#         temp.right = l1.right
#         rtype = temp
#         self.merge(l1.left)
#         self.merge(l1.right)
#         # self.print1(rtype)
#         return rtype
# a = Solution()
# q = a.merge(probe)
# a.print1(q)

    # return "s"

# print1(l2)











#
# list1 = [[(i , j ) for i in range(5)]for j in range(3)]
# print(list1)

# list1 = [1,1,5,1,2,3,4]
# list2 = [2]
# list1 ,list2 = list2,list1

# while 1 in list1:
# list1.sort()
# set(list1)
# print(list(set(list1)))
#
# list1 = [1,2]
# str1 = str(list1)
# print(str1,type(str1))
#
# [item[3:] for item in A]
# A = [[1, 1, 1, 0, 0, 0], [1, 0, 1, 0, 1, 0], [0, 0, 0, 1, 1, 1]]
# s1 = A[:1][:]
# s2 = [item[3:] for item in A]
# print("s1 = ",s1)
# print("s2 = ",s2)


# left = 1
# right = 6
#
# target = 6
# if target in (left,right):
#     print(True)
# else:

# words = ["w","wo","wor","worl", "world"]
#
# words.sort(key = lambda i : len(i),reverse = True)
# # word1 = sorted(word1,key = lambda i :(len(i)))
# print("pycharm输出为=",words)
# s_str = "123"
# words.decode('unicode-escape')
# print(words)



# import sys
# print('目前系统的编码为：',sys.getdefaultencoding())
# name='小明'
# print(type(name))#首先我们来打印下转码前的name类型，因为它是str，所以可以通过encode来进行编码
# name1=name.encode('Unicode')
# print("这里",name1)


# name2=name1.decode('utf-8')
# print(type(name2))
# print("这里",name2)
# 这里要跟大家说下，decode()括号中为什么写utf-8，而不写gbk，可以这样理解，因为要解码，你总得告诉它我是什么编码的吧，比如我原先是utf-8格式的编码，现在要解码，但是如果冒充utf-8，说自己是gbk，那就会出现乱码，见下：
# <class 'str'>
# <class 'str'>
# 灏忔槑

# def mycmp1(x,y):
#     if len(x) !=  len(y):
#         return len(x) - len(y)
#     elif len(x) == len(y):
#         return x - y
# words = ["world","worlc","english","history"]
# word1 = sorted(words,key = lambda i : len(i),reverse = True)
# word2 = sorted(words,key = lambda i : len(i),reverse = False)
#
#
# word3 = ["aaab","aaac","bbbb","bbba","bbbc","abcd"]
# word4 = ["aaac","aaaa","bbba","bbbb","bbbc","edfg"]
#
# word3 = sorted(word3,key = lambda i : len(i),reverse = True)
# word4 = sorted(word4,key = lambda i : len(i),reverse = False)
# word3 = sorted(word3,key = mycmp1(word3,word3))
#
# print(word1)
# print(word2)
# print(word3)
# print(word4)

# def mycmp1(x,y):
#     if len(x) !=  len(y):
#         return len(x) - len(y)
#     elif len(x) == len(y):
#         return x - y
# word = ["aaab","aaac","bbbb","bbba","bbbc","abcd"]
# word1 = sorted(word,key= lambda i : (len(i),len(i) and i,i))
# word2 = sorted(word,key= lambda i : len(i))
# print(word1)
# print(word2)


# s='9a13C85c7B24A6b' #正确的顺序应该为：abcABC135792468
# lis1=sorted(s,key=lambda x:(x.isdigit(),x.isdigit() and int(x)%2==0,x.isalpha() and x.isupper(),x.isalpha() and x.lower()))
# lis2=sorted(s,key=lambda x:(x.isdigit(),x.isdigit() ))
# lis3=sorted(s,key=lambda x:(x.isdigit() ))
#
# lis4=sorted(s,key=lambda x:(x.isdigit() and int(x)%2==0,x.isalpha() ))
# lis5=sorted(s,key=lambda x:(x.isdigit(),x.isdigit() and int(x)%2==0,x.isalpha() ))
# lis2_1=sorted(s,key=lambda x:(ord(x ) and  ord(x) ))
#
#
#
# print("list1 = ",''.join(lis1))
# print("list2 = ",''.join(lis2))
# print("list3 = ",''.join(lis3))
# print("list4 = ",''.join(lis4))
# print("list5 = ",''.join(lis5))
# print("list2_1 = ",''.join(lis2_1))


# 1.x.isdigit()的作用是把数字放在前边,字母放在后边.
# 2.x.isdigit() and int(x) % 2 == 0的作用是保证奇数在前，偶数在后。
# 3.x.isupper()的作用是在前面基础上,保证字母小写在前大写在后.
# 4.最后的x表示在前面基础上,对所有类别数字或字母排序。



# 3.8: use time.perf_counter or time.process_time
# import time
# list1 = [1,2,3,4,5]
# t1 = time.perf_counter()
# for i in range(999999):
#     sum1 = 0
#     sum1 = sum(list1)
# t2 = time.perf_counter()
#
# t3 = time.perf_counter()
# for i in range(999999):
#     sum1 = 0
#     for i in list1:
#         sum1 += i
# t4 = time.perf_counter()

# t5 = time.perf_counter()
# for i in range(99999):
#     sum1 = 0
#     for i in range(5):
#         sum1 += list1[i]
# t6 = time.perf_counter()

# t55 = time.perf_counter()
# for i in range(99999):
#     sum1 = 0
#     length = len(list1)
#     for i in range(length):
#         sum1 += list1[i]
# t66 = time.perf_counter()


# t7 = time.perf_counter()
# for i in range(999999):
#     sum1 = 0
#     for i in range(len(list1)):
#         sum1 += list1[i]
# t8 = time.perf_counter()
#

# t9 = time.perf_counter()
# i = 0
# while i < 99999:
#     sum1 = 0
#     sum1 = sum(list1)
#     i += 1
# t10 = time.perf_counter()
# print(t2 - t1 )
# print(t4 - t3 )
# print("t55",t6 - t5 )
# print("t65",t66 - t55 )
# print(t8 - t7 )
# print(t8 - t1 )
# print(t10 - t9)
# print((t2 - t1) + (t4 - t3) + (t6 - t5) + (t8 - t7))


# list1 = [1,2,3,4,5]
# t1 = time.perf_counter()
# for i in range(99999):
#     sum1 = 0
#     for i in list1:
#         sum1 -= i
# t2 = time.perf_counter()
#
# t3 = time.perf_counter()
# for i in range(99999):
#     sum1 = 0
#     length = len(list1)
#     for i in range(5):
#         sum1 -= list1[i]
# t4 = time.perf_counter()
#
# t5 = time.perf_counter()
# for i in range(99999):
#     sum1 = 0
#     i = 0
    # length = len(list1)
    # while i < 5:
        # sum1 -= list1[i]
        # sum1 -= i
        # i += 1
# t6 = time.perf_counter()

# print(t2 - t1)
# print(t4 - t3)
# print(t6 - t5)


# for i in range(97,123):
#     print(chr(i))
# import string
# i = 'asdf, sdf.'
# trantab = str.maketrans({key: None for key in string.punctuation})
# i = i.translate(trantab)
# str.punctuation(s)
# print(i)



# lower_case_documents = ['Hello, how are you!','Win money, win from home.','Call me now.','Hello, Call hello you tomorrow?','asdf, sdf.']
# sans_punctuation_documents = []
# import string
# #
# for i in lower_case_documents:
# #     #TODO
#     trantab = str.maketrans({key: None for key in string.punctuation})
#     j = i.translate(trantab)
#     sans_punctuation_documents.append(j)
#
# print(sans_punctuation_documents)


#
# L = [1,3,5,7,8,6,4,2]
#
# import random
#
# def fast_sorted(L):
#     if len(L) < 2: return L
#     pivot_element = random.choice(L)
#     small = [i for i in L if i < pivot_element]
#     medium = [i for i in L if i == pivot_element]
#     large = [i for i in L if i > pivot_element]
#     return fast_sorted(small) + medium + fast_sorted(large)

# print(fast_sorted(L))


#
# odd = (num for num in range(10) if num % 2 == 1)
# for num in odd:
#     print(num)


# for num in (num for num in range(10) if num % 2 == 1):
#     print(num)

# lsit1 = {1:5}
# for k,v in list1:
#     print(k,v)


# class Solution:
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
        # ans = collections.defaultdict(list)
        # ans = collections.defaultdict(list)
        # rtype = [[strs[0]]]
        # dict1 = {}
        # for word in strs:
        #     list1 = [0] * 26
        #     for i in word:
        #         list1[ord(i) - ord("a")] += 1
        #     tup1 =tuple(list1)
            # if tup1 in ans:
            #     ans[tup1].append(word)
            # else:
            #     ans[tup1] = word
            # ans[tuple(list1)].append(word)
        # return ans.values()

        # ans = collections.defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     ans[tuple(count)].append(s)
        # return ans.values()


# s='9a13C85c7B24A6b' #正确的顺序应该为：abcABC135792468
# lis1=sorted(s,key=lambda x:(x.isdigit(),x.isdigit() and int(x)%2==0,x.isalpha() and x.isupper(),x.isalpha() and x.lower()))

#
# list1 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
# for i in list1[0]:
#     print(i)
#
# for i in list1[0]:
#     print(0 ^ i)


# list1 = [[1,2],[4,6],[3,5],[2,8]]
#
# print(sorted(list1,key =lambda i :list1))

#
# nums = [2,2,3]
#
# class Solution():
#     def solve(self,nums):
#         list1 = [[]]
#         for i in nums:
#             list2 = list1[:]
#             for temp in list2:
#                 q = temp[:]
#                 q.append(i)
#                 if q not in list1:
#                     list1.append(q)
#
#         return list1
#
#
#
#
#
#
# a = Solution()
# q = a.solve(nums)
# print("q =",q)

# dict1 = {{"1"}:1,{"2"}:2}
# print(dict1)



# print(int(1.0) == 1)



# while  input("qqq"):
    # print("len =",len(a))
    # print(a)
    # str1= input("www").split()
    # print(str1)
    # a = int(a)
    # b = int(b)
    # print(a+b,type(a))


# while True:
#     list1 = input("qqq").split("\n")
#     if len(list1) == 0:
#         break
#     a = int(list1[0])
#     b = int(list1[1])
#     print(a + b)

#
#
# import sys
# list1 = []
# list2 = []
# for line in sys.stdin:
#     a,b = line.split()
#     a = int(a)
#     b = int(b)
#     list1.append(a)
#     list2.append(b)
#
# n = len(list1)
# for n in range(n):
#     print(list1[n] + list2[n])

# text = "123afasd  !@%#$dsfga34234"
# def clean_email_text(text):
#     pure_text = ""
#     for letter in text:
#         if letter.isalpha() or letter == " ":
#             pure_text += letter
#
#     return pure_text
#
# pure_text = clean_email_text(text)
# print(pure_text)


# word1 = sorted(word,key= lambda i : (len(i),len(i) and i,i))


#方法1,直接把接收的秘钥转成数字比较大小

#
#
# n = int(input("接收秘钥个数"))
# list1 = [] #装秘钥用
# dict1 = {} #把秘钥和他所对应的数字建立映射  12 -> 00012
# while n > 0:
#     temp = input()
#     num = int(temp)
#     list1.append(temp)
#     if num not in dict1:
#         dict1[num] = [temp]
#     else: # 当遇到12,012,0012这样数字相等的就给他都添加进去
#         dict1[num].append(temp)
#     n -= 1
#
# list1.sort(key =  lambda num : len(num)) # 将秘钥按照长度排序
# if n == 1: # 若只有一个秘钥,直接返回结果
#     print(list1[0])
#
# else:
#     #若最短的秘钥只有一个
#     if len(list1[0]) != len(list1[1]):
#         list2 = dict1[list1[0]]   # list2 等于该
#         list2.sort(key =  lambda num : len(num))
#         print("answer =",list2[0])
#


# print(dict1)
# print("list1 =",list1)

#
# n = int(input("接受秘钥个数"))
# list1 = [] #装秘钥
# while n > 0:
#     list1.append(input())
#     n -= 1
#
# if n == 1:
#     print(list1[0])
#
# list1.sort(key=  lambda str1 :len(str1))
#
# if list1[0] != list1[1]:
#     print(list1[0])
#
# for num in list1:




# def classfication(sex,height,fit):
# #     count = 0
# #     count = count * 2 + fun_sex(sex)
# #     count = count * 2 + fun_height(height)
# #     count = count * 2 + fun_fit(fit)
# #     print("第{0}类".format(count))
# #
# # def fun_sex(sex):
# #     if sex == "male":
# #         return 1
# #     else:
# #         return 0
# #
# # def fun_height(height):
# #     if height == "tall":
# #         return 1
# #     else:
# #         return 0
# #
# # def fun_fit(fit):
# #     if fit == "fat":
# #         return 1
# #     else:
# #         return 0
# #
# # classfication("male","tall","fat")

# print(5)
# for i in range(5,5):
#     print(i)

# list1 = ["a","s","d"]
# str1 = str(list1)
# print(str1,type(str1))
#
# str2 = "".join(list1)
# print(str2)

# str1 = "the sky is blue"
# list_str = str1.split()
# for word in list_str[::-1]:
#     print(word,end=" ")
# print(" ".join(list_str[::-1]))
# print()
# print(rtype)

# str1 = "123.123"
#
# list1 = [123,123]


# str1 = "123.123.132"

# list1  = str1.split(".")


#
#
# list1 = [780,935,2439,444,513,1603,504,2162,432,110,1856,575,172,367,288,316]
#
#
# [444,513,1603,504,110,1856,575,172,367,288,316]
#
# [935,2439,432,780,2162,1603,575,513,367,316,1856,504,444,288,172,110]
#
# list1.sort(reverse= True)
# print(list1)

# import random
# list1 = []
# for i in range(999999):
#     list1.append(random.randint(1,999999))
# print(list1)
# print(sorted(list1))
#
# import math
# n = int(math.sqrt(101))
# print(n)


# dict1 = {}
#
# dict1[5] = dict1.get(5,0) +2
# print(dict1[5])
#
# list1 = [1,3,5,6,4,2]
#
# s = "sdf"
# s.split()


# a = "1+-3i"
# list1 = a.split("+")
# print(list1)

# print(list1[1])
# print(list1[1][0])
# print(list1[1][0] == "-")
# if list1[1][0] == "-":
#     num1 = -int(list1[1][1:-1])
# print(num1)



# kid = True or False
# print(kid)

# c = 1
# a,b = c* 2 ,c

# list1 = [99,2,3,4,5,6,7]
# list2 = [7,6,5,99,3,2,1]
#
# num1 = list1[0]
# num2 = list2.index(num1)
# print(num2)

#
# import re
# p = re.compile(r'\d+')
# print(p.split("one11two22three23123for45df"))
#
# print(p.findall("231ont12l3j12j3i123i12n42"))


# n = 5
#
# for i in range(n):
#     n -= 1
#     print(i)

# s = "-11"
# s = int(s)
# print(type(s),s+1)

# print(6//-132)
# print(52//-3)
# print(-52//3)

# print(5 // -2,5 % -2)
#
# print(int(5/-2))
#
# import random
#
# a = round(5.55)
# print("a=",a)

# def fun1(x,y):
#     return x+y > y+x

# list1 = [1,223,5623,8671,3,4,345,56234,71235,7435]
# list1 = [3,30,34,5,9]
# list2 = [str(i) for i in list1]

# list2.sort(key = fun1)

# list2.sort(reverse = True)
# print(list2)
# for i in  range(1,len(list2)):
    # print(list2[i-1]+list2[i] > list2[i]+list2[i-1],type(list2[i-1]+list2[i]))
    # if list2[i-1] + list2[i] < list2[i] + list2[i-1]:
    #     print(list2[i])
    #     list2[i],list2[i-1] = list2[i-1],list2[i]

# print(list2)


# largest_num = ''.join(sorted(map(str, list1), key=fun1))
# print(list1)
# print(list2)
# str1 = "".join(list2)
# print(str1)



# q = 5 & 6 & 7
#
# q = 5
# for i in range(6,8):
#     q &= i

# q = 28 & 29 & 30 & 31
# q = 5 & 6 & 7
#

# print(q)

# a = "qweewq"
# a = "qwerty"
# for i in a[::-1]:
#     print(i)

# for i in a[::-2]:
#     print(i)


# dict1 = {1:1,2:1,3:3}

# print(dict1.get(5,1))


# def product( v):
#     n = 1
#     while v > 1:
#         n *= v
#         v -= 1
#     return n
        # print(v)
    # print(n)
# product(5)

# target = 5

# dp = [0 for i in range(target + 1)]
# dp = *6
# dp[0] = 1
# print(dp)


# dp = [0 for i in range(target+1)]
# dp[0] = 1
# print(dp)

# s = "11,213h"
#
# ss = "234"
# list1 = [5,1]
# sign = list1[ss=="+"]
# print(sign)

# list1 = [5,6,7]
#
# for k,v in enumerate(list1):
#     print(k,v)


# list1 = [1,2,6]
# rtype = 0
# for num in list1:
#     rtype = rtype * 10 + num
# print(rtype)

# list1 = ["1",'2']
# str1 = int(str(list1))
# print(type(str1),str1)


# num = "".join(list1)
# print(num,type(num))


# print(1337/7,191*7)

# print(1 and 8 )

# print(int(-5 / 2))

# print(int(-1 >> 1),-3 >> 1)

# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 5
#
# for item in matrix:
#     if target in item:
#         print("yes")
#     else:
#         print("no")

# secret = "1234543"
# dict3 = {}
# dict4 = {}
# for i in secret:
#     dict3[i] = dict3.get(i,0) + 1
#
# print(dict3)



# import  time
# n = 9999
# t1 = time.perf_counter()
# for i in range(n):
#     # print(i)
#     list1 = [[Nonefor i in range(100)] for i in range(100)]
#     # print(i)
# t2 = time.perf_counter()
# print(t2 - t1,"sec")
#
# t3 = time.perf_counter()
# i = 0
# for i in range(n):
#     list1 = [[] * 100 for i in range(1)]
# t4 = time.perf_counter()
# print(t4 - t3,"sec")


# dp = [0] * 10
# dp[0] = 1
# print(dp)

# str1 = "qwe"
# str1.isdigit()
# if str1.isalpha():
#     print("qwe")

#
# list1 = ["q","w","aa","da","dd"]
# list1 = ["m","mo","m w","w"]
#
# list1.sort()
# print(list1)
#
#
# dp = []
# index = 1
# nums = []
# n =1
# class qwe():
#     def slove(self):
#         pass
#
#
#         dp[index] = max( nums[index-1]+
#                          self.solve(nums,dp,index*4,n) +
#                          self.solve(nums,dp,index*4+1,n) +
#                          self.solve(nums,dp,index*4+2,n) +
#                          self.solve(nums,dp,index*4+3,n) ,
#                          dp[index*2] + dp[index*2+1] )


# s1 = 2
# s2 = s1 + None
# print(s2)

#
# list1 = [1,2]
# list2 = [0,[1,[0]]]
#
# nestedList = [0,[1,[2]]]
# class NestedIterator(object):

    # def __init__(self, nestedList):
    #     """
    #     Initialize your data structure here.
    #     :type nestedList: List[NestedInteger]
    #     """
    #     self.stack = []
    #     for item in nestedList:
        # while nestedList:
        #     item = nestedList.pop(0)
        #     if  type(item) == list:
        #         nestedList += item
        #         print(nestedList,"yes")
            # else:
            #     print(self.stack)
                # self.stack.append(item)
        #
        # print(self.stack)
    #
    #
    # def next(self):
    #     pass
# a = NestedIterator(nestedList)
#


# lista = ["a"]
# listb = ["b"]
# listc = ["c"]
#
# lista,listb,listc = listb,listc,lista
#
# print(lista,listb,listc)


# lista = ["qqq"]
# listb = ["aaa"]
# listc = ["zzz"]
#
# ta = lista
# tb = listb
# tc = listc
# lista = tb
# listb = tc
# listc = ta
# print(ta,tb,tc)
# print(lista,listb,listc)

#
# def perfect_square():
#     #寻找第一个满足要求的数
#     x = 1
#     while True:
#         if square(x):
#             if square(x+168):
#                 print("the answers is",x)
#                 break
#         x += 1
#
# def perfect_square1(n):
#     #寻找小于n的整数中所有满足要求的数
#     x = 1
#     print("小于",n,"的数中所有答案为",end=" ")
#     while n > 0:
#         if square(x) and square(x+168):
#             print(x,end=" ")
#         n -= 1
#         x += 1
#
#
# def square(x):
#     import  math
#     n = math.sqrt(x+100)
#     if n == int(n):
#         return True
#     else:
#         return False
#
# if __name__ == "__main__":
#     perfect_square()
#     perfect_square1(1000)



# def solve(nums,left):
#     n = len(nums)
#     if left == n -1:
#         print(nums)
#         return
#     for i in range(left,n):
#         nums[i],nums[left] = nums[left],nums[i]
#         solve(nums,left+1)
#         nums[i],nums[left] = nums[left],nums[i]
#
# if __name__ == "__main__":
#     nums = [1,2,3]
#     left = 0
#     solve(nums,left)

#
# list1 = ["q","w","e"]
# print(list1.index("e"))

# str1 = "qwe"
# str2 = "asdqwe"
# print(complex(str1,str2))

# def choose_id(head,n):
#     probe = head
#     num_of_china = 0
#     while probe:
#         num_of_china += 1
#         probe = probe.next


# m1 = [ [1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
#
# def reshape(m1):
#     height= len(m1)
#     width = len(m1[0])
#     m2 = [[None for i in range (height)] for j in range(width)]
#     print(m2)
#     for i in range(height):
#         for j in range(width):
#             print(i,j)
#             m2[width-j-1][i] = m1[i][j]
#     return m2
#
# m2 = reshape(m1)
# print(m2)

# list1 = ["q",".","q","q"]
# str1 = str(list1)
# str2 = "".join(list1)
# print(str2)
# print(str1)


# matrix = [ [1,2,3,4],
#            [5,6,7,8],
#            [9,10,11,12],
#            [13,14,15,16]]
#
# def  fun1(martix):
#     n = len(martix)
#
#     for i in range(n):
#         for j in range(n):
#             print(martix[i][j])
#
# fun1(matrix)

#
# set1 = set()
#
# set1.add(1)
# set1.add(1)
# set1.add(2)
# set1.remove(1)
# print(set1)

# n = 4
# list1 = [1 for _ in range(4)]
# list1 = [(i+1) * list1[i-1] for i in range(n)]
# print(list1)

# n = 4
# list1 = [1] * n
# for i in range(1,n):
#     list1[i] = list1[i-1] * (i+1)
# print(list1)




# list1 = ["q",".","q","q"]
# str1 = str(list1)
# str2 = "".join(list1)
# print(str2)
# print(str1)


# ans = [1,2,3,4]
# ans = ["a","s","df"]
# str1 = "".join(ans)
# print(str1)


# list1 = [[1,2],[5,7],[3,6]]
# list1.sort(key=lambda list1 : list1[0])
# print(list1)

# list1 = ["a","b","c"]
# list2 = ["d","e","f","g"]
# list3 = ["h","i"]
#
# def solve(list1,list2,list3):
#     ans = []
#     for i in list1:
#         for j in list2:
#             for k in list3:
#                 ans.append([i,j,k])
#
#     return "共{}种,是".format(len(ans)),ans
#
# print(solve(list1,list2,list3))
#
#
# list1 = ["a","b","c"]
# list2 = ["a",]


# import pygame
#
# pygame.mixer.init()
# track=pygame.mixer.music.load("/Users/suyifan/Desktop/新建文件夹/others/WE214.wav") #可以播放.mp3 .wav等多种格式的音频文件
# pygame.mixer.music.play()

# import os

# os.system("/Users/suyifan/Desktop/新建文件夹/others/WE214.wav")

# import pygame
#
# pygame.init()
# track = pygame.mixer.music.load(r"/Users/suyifan/Desktop/新建文件夹/others/WE214.wav")
# pygame.mixer.music.play()
# time.sleep(100)
# pygame.mixer.music.stop()

# path = r"/Users/suyifan/Music/网易云音乐/陶然,帅琪,曾嵘 - 雷雨公路.mp3"
# import mp3play
# def playmusic(path):
#     clip = mp3play.load(path)
#     clip.play()
#     time.sleep(10)
#     clip.stop()
#     playmusic('test.mp3')

# playmusic(path)
# class Solution(object):
#     def minAreaRect(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: int
#         """
#         points = map(tuple, points)
#         points.sort()
#         pset = set(points)
#         N = len(points)
#         res = float('inf')
#         for i in range(N - 1):
#             p1 = points[i]
#             for j in range(i + 1, N):
#                 p4 = points[j]
#                 if p4[0] == p1[0] or p4[1] == p1[1]:
#                     continue
#                 p2 = (p1[0], p4[1])
#                 p3 = (p4[0], p1[1])
#                 if p2 in pset and p3 in pset:
#                     res = min(res, abs(p3[0] - p1[0]) * abs(p2[1] - p1[1]))
#         return res if res != float("inf") else 0
#
#
# points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
# set1 = list(map(tuple,points))
# print(set1)
# points = map(tuple, points)
# points.sort()
# pset = set(points)
# print(pset)


# print(-5 % 4)


# matrix =  [[1, 2], [3], [4, 5, 6]]
# martix = []
# matrix = [ [1,2,3],[4,5,6],[7,8,9]]
# class Solution():
#
#     def solve(self,martix):
#         ans = []
#         temp = []
#         ans = self.fun1(martix,ans,temp)
#         return ans
#
#     def fun1(self,martix,ans,temp):
#         if not martix:
#             ans.append(temp[:])
#             return
#
#         for num in martix[0]:
#             temp.append(num)
#             self.fun1(martix[1:],ans,temp)
#             temp.pop()
#         return ans
# a = Solution()
# q = a.solve(matrix)
# print("q =",q)



# import heapq as hq
#
#
# nums = [1,3,-1,-3,5,3,6,7,1,1,1,1,1,1]
# k = 3
# n = len(nums)
# heap = nums[:k]
# for i in range(k,n):
#     hq.heappush(heap,nums[i])
#     print(hq.nlargest(1,heap),end=" ")
    # print(heap)
    # heap.pop(-1)
    # hq.heappop(heap)
    # print(heap)


# s = "aa"
# p = "a*"
#
# class Solution:
#     def isMatch(self, s, p):
#         if not (s and p):
#             return True
#
#         if not (s or p):
#             return False
#         len_s = len(s)
#         len_p = len(p)
#         dp = [[False]*(len_p+1) for _ in range(len_s+1)]
#         dp[0][0] = True
#
#         for i,char in enumerate(p):
#             if char == "*" and dp[0][i-1]:
#                 dp[0][i+1] == True
#
#         for i in range(len_s):
#             for j in range(len_p):
#                 if s[i] == p[j] or p[j] == ".":
#                     dp[i+1][j+1] = dp[i][j]
#                 if p[j] == "*":
#                     if s[i] != p[j-1] or p[j-1] != ".":
#                         dp[i+1][j+1] = dp[i+1][j-1]
#                     else:
#                         dp[i+1][j+1] = dp[i][j] or dp[i][j+1] or  dp[i+1][j-1]
#         return dp[-1][-1]
#
#
#
#
# a = Solution()
# q = a.isMatch(s, p)
# print("q =", q)



# n = 5
#
# if 0 < n < 6:
#     print("yes")


# nums = [5,4,3,2,1]
# num = 2
# i = 1
# nums[num-1],nums[i] = num,nums[num-1]
# nums[2],nums[1] = nums[1],nums[2]
# nums[2],nums[1] = nums[1],[2]

# print(nums)

# for i in range(chr(1
#                    ),chr(9)):
#     print(chr(i))

# for i in range(10):
#     print( -i ^ 4)


# list1 = [1,2,3,4,5,6]
# list2 = list1[:]
# list2 = list1
# list1[0] = 99
# print(list1)
# print(list2)

# str={"customerType":"DCF","tk":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9","customer":"fbd"}
# print(type(str))


# list1 = [ [1,2,3],[4],[5,6,7]]
#
#
# def fun1(list1):
#     list_len = []
#     for i in list1:
#         list_len.append(len(i))
#
#     for i in list_len:
#         for j in range(i):

# class Solution:
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         q = list()
#         q.append([n, 0])
#         visited = [False for _ in range(n+1)]
#         visited[n] = True
#
#         while any(q):
#             num, step = q.pop(0)
#
#             i = 1
#             tNum = num - i**2
#             while tNum >= 0:
#                 if tNum == 0:
#                     return step + 1
#
#                 if not visited[tNum]:
#                     q.append((tNum, step + 1))
#                     visited[tNum] = True
#
#                 i += 1
#                 tNum = num - i**2

# print(10 ** 9 + 7)

# import tensorflow as tf
# w = tf.Variable(0,dtype = tf.float32)
# tf.multiply(w-5,w-5)


# import pandas as pd

# a1 = pd.DataFrame( {"aa":[1,2,3],"bb":[4,5,6],"cc":"7,8,9"},index = ["qq","ww","ee"])
# a1.set_index("aa")
# print(a1)
# a1.set_index()

# import jieba
#
# stopwords = []
#
# def split_word(path, words):
#     with open("{}.txt".format(path), "r", encoding="gb18030") as f:
#         #         f = f.encoding("")
#         i = 0
#         for line in f.readlines():
#             #             line = line.encode("utf-8")
#             try:
#                 segs = jieba.lcut(line.strip())
#                 segs = [x for word in segs if len(word) > 1 and word not in stopwords]
#                 words += segs
#
#             except:
#                 i += 1
#                 print("为什么读这些行时候有错误:", line)
#                 continue
#
#
# split_word(f_path, words)
# print("一共有{}行数据发生异常".format(i))
# words

# arr = [ [1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#
# print( [ [row[i] for row in arr] for i in range(len(arr[0]))])
#
# for i in range(len(arr[0])):
#     for row in arr:
#         print(row)
    # print()

# s = "1223"
# s = s.strip()


# a = [1,2,2,3,4]
# a.remove(2)
# print(a)
# import math
# print(math.sqrt(2))


# import numpy as np
#
# a = np.array([1,0])
# b = np.array([[0.9,0.1],[0.5,0.5]])


# for i in range(5):
#     print(a.dot(b))

# for i in range(5):
#     print(i)


# str1 = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
# a = [539834657,21,539834678,539834699,1079669377,1619504076,2699173453,4318677529,7017850982,11336528511]
# temp =""
# for i in range(len(a)-2):
#     if a[i] + a[i+1] != a[i+2]:
#         print(a[i])
#     else:
#        temp += str(a[i])
# temp += str(a[-2]) + str(a[-1])
#
# if temp == str1:
#     print("yes")


# class Solution():
#     def __init__(self):
#         self.a = self.run()
#
#     def run(self):
#         print("qqq")

# import tensorflow as tf
#
# a = tf.constant([1.,2.],name="a")
# b = tf.constant([3.,4.],name="b")
#
# num = tf.add(a , b,name = "add")
# print(num)



# stack = [1,2,3]
# print(stack)


# class Solution:
#     def isScramble(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#
#         if (not s1) or (not s2):
#             return False
#
#         if s1 == s2 :
#             return True
#         dp =[0]*26
#
#         for i in range(len(s1)):
#             dp[ord(s1[i])-ord("a")] += 1
#             dp[ord(s2[i])-ord("a")] -= 1
#
#         for num in dp:
#             if num != 0:
#                 return False
#
#         for i in range(len(s1)):
#             if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
#                 return True
#             if self.isScramble(s1[:i],s2[len(s1)-i:]) and self.isScramble(s1[i:],s2[:len(s1)-i]):
#                 return True
#         return False


# str1 = ""
#
# print(str1[0])



######################## tensorFlow 实战第三章
# batch_size = 8
#
# w1 = tf.Variable(tf.random_normal([2, 3], stdsev=1, seed=1))
# w2 = tf.Variable(tf.random_normal([3, 1], stdsev=1, seed=1))
#
# x = tf.placeholder(tf.float32, shape=(None, 2), name="x_input")
# y_ = tf.placeholder(tf.float32, shape=(None, 1), name="y_input")
#
# a = tf.matmul(x, w1)
# y = tf.matmul(a, w2)
#
# y = tf.sigmoid(y)
#
# cross_entropy = -tf.reduce_mean(y * tf.log(tf.clip_by_value(y, 1e-10, 1.0))
#                                 + (1 - y) * tf.log(tf.clip_by_value(1 - y, 1e-10, 1.0)))
# # learning_rate = 0.001
# train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)
#
# rdm = RandomState(1)
# dataset_size = 128
# X = rdm.rand(dataset_size, 2)
#
# Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]
#
# with tf.Session() as sess:
#     init_op = tf.global_variables_initializer()
#     sess.run(init_op)
#
#     sess.run(w1)
#     sess.run(w2)
#
#     STEPS = 5000
#
#     for i in range(STEPS):
#         start = (i * batch_size) % dataset_size
#         end = min(start + batch_size, dataset_size)
#
#         sess.run(train_step, feed_dict,{x: X[start:end], y_: Y[start:end]})
#
#         if i % 1000 == 0:
#             total_cross_entropy = sess.run(cross_entropy, feed_dict={x: X, y_: Y})
#             print("after %d training step(s),cross entropy on all data is %g" % (i, total_cross_entropy))
#
#     print(sess.run(w1))
#     print(sess.run(w2))


####################################tensorflow实战 第四章
# import tensorflow as tf
# from numpy.random import RandomState
#
# batch_size = 8
#
# x = tf.placeholder(tf.float32,shape = (None,2),name = "x_input")
# y_ = tf.placeholder(tf.float32,shape = (None,1),name = "y_input")
#
#
# w1 = tf.Variable(tf.random_normal([2,1],stddev=1.0,seed=1))
# y = tf.matmul(x,w1)
#
# loss_less = 1
# loss_more = 10
#
# loss = tf.reduce_sum(tf.where(tf.greater(y,y_),(y-y_)*loss_more,(y_-y)*loss_less))
# # loss = tf.reduce_mean(tf.square(y_-y)) + tf.contrib.layers.l2_regularize(lambda )(w)
#
# loss = tf.reduce_mean(tf.square(y_-y)) + tf.contrib.
#
#
#
#
# train_step = tf.train.AdamOptimizer(0.001).minimize(loss)
#
# rdm = RandomState(1)
# dataset_size = 128
# X = rdm.rand(dataset_size,2)
#
# Y =[ [x1+x2+rdm.rand()/10-0.05 ] for (x1,x2) in X]
#
# with tf.Session() as sess:
#     init_op = tf.global_variables_initializer()
#     sess.run(init_op)
#     STEPS = 5000
#
#     for i in range(STEPS):
#         start = (i*batch_size)  % dataset_size
#         end = min(start + batch_size,dataset_size)
#         sess.run(train_step,feed_dict={ x:X[start:end],y_:Y[start:end]})
#
#         if (1+i) % 1000 == 0:
#             print(sess.run(w1))

# import numpy as np
# a = np.array([[1,2,3,4],[5,6,7,8]])
# b = a.argmax(axis=1)
# print(b,)

# nums = [7,1,13,6,19,18,12,3,15,4,20,11,2,15,14]
# print(sum(nums))
# print(sorted(nums))

# nums = []
#
# print(len(nums))

# n = "123321"
# nn = len(n)
# for i in range(nn):
#     if n[i] != n[nn-i-1]:
#         print("no")
#

# print("yes")


# s = "qwer"
# s_dict = {}
#
# for c in s:
#     s_dict[c] = s_dict.get(c,0) + 1
# print(s_dict)


# list1 = [-17066,9854,21565,21364,-20470,17727,-16429,-19627,20999,22524,16752,-23476,4484,12866,8979,322]
# print(sum(list1)+17066)


# class Solution:
#     def maxChunksToSorted(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: int
#         """
#         nums = sorted(arr)
#
#         num_dict = {}
#         for i, num in enumerate(nums):
#             num_dict[num] = i
#
#         cur = 0
#         ans = 1
#         for i in range(len(arr)):
#             cur = max(num[i], i)
#             if num_dict[arr[i]] > cur:
#                 ans += 1
#         return ans



# arr = [1,2,3]
# v = sorted([(n << 32) | i for i, n in enumerate(arr)])
# print(v)

# import collections
# nums = sorted(arr)
#
# num_dict = collections.defaultdict(list)
# for i, num in enumerate(nums):
#     if num not in num_dict:
    # num_dict[num].append(i)
#
# print(type(num_dict[1]))


# a = [[1,2,3],[5,4,0]]
# a = ["q","w","e"]
# str1 = "".join([i for i in a])
# set1 = set(a)
# print(str1)
# list1 = []
# list1.append(a)
# print([[1,2,3],[5,4,]] in list1 )

# dict1 = {1:[1,2,3]}
# print(a.index(0))


# board = [[1,2,3],[5,4,0]]
# s = "".join(str(c) for row in board for c in row)
# q = [(s, s.index("0"))]
# print(type(q),q)


# s = "A1"
# s = s.lower()
# print(chr(ord("a")-32))


# import re
#
# str1 = "qwe(rty)yui(asd)"
#
# a = re.findall("\((.*?)\)",str1)
# print(a,str1)

# path_dict[1].append([123])
# print(path_dict)


# str1 = "   qwe rty  "
# str1.strip("q")
# print(str1)


# str1 = "qwe"
# str2 = "asd"

# print(str1 + "/" + str2)




# ans = "1(2(4)())  (3())"
# my  = "1(2(4 ()))3())"
# my1 = "1(2(4()()()(3()()"
# my2 = "1(2(4(()() (3(())"
#

# "1(2(4( )))   ()()  (3())  ()"

# import random
# import time
#
# list1 = []
# for i in range(100):
#     t1 = time.perf_counter()
#     for i in range(100):
#         for i in range(100):
#             random.randint(1,100)
#     t2 = time.perf_counter()
#
#
#     t3 = time.perf_counter()
#     for i in range(100):
#         for i in range(100):
#             random.randint(1,99999)
#     t4 = time.perf_counter()
#     list1.append((t2-t1)-(t4-t3))
#
# print(sum(list1))

# import random

# print(random.randint(0,0))


# people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# list1 = sorted(people)#,key= lambda :  i[1]  )
# print(list1)


# words = ["w","wo","wor","worl", "world","worlc"]
# a = sorted(words,key = lambda i : (len(i) ,len(i) and i,i),reverse = True)
# print(a)


# list1 = [None] *10
#
# print(list1)
#
# str1 = "0" * 0 + "1"*1
# print(str1)

# dict1 = {"q":1,"w":2}
# dict1.pop("q")
# print(dict1)


# import collections
#
#
# input = {"A省":["B市",["C县",["D村","E村"]]]}
# #
# #
# output = {"A省":{"B市":{"C县":["D村","E村"]}}}
# #
# dict1 = collections.defaultdict(dict)
# def fun1(input):

    # for k,v_list in input.items():
        # v_list.reverse()
        # while type(v_list) == type(list()) and v_list[-1] == type(list()):
        # if v_list[-1] == type(list()):
        #     fun2(v_list)

# def fun2(input):
#     if input[-1] == type(list()):
#         fun2(v_list)




        # print(v_list)
        # for i in v_list:
        #     result = dict()
        #     result[i] = k
        #     v = result
    # return result

# print(fun1(input))

#
#
# k1, v1 = 'a.b.c', 1
# def nested_dict(k, v):
#     key_list = k.split('.')
#     key_list.reverse()
#     for i in key_list:
#         result = dict()
#         result[i] = v
#         v = result
#
#     return result
#
# print( nested_dict(k1, v1))



# def g(n,k,x):
#     # list1 =
#     list1 = f(n,k)
#     print(list1)
#     ans = gailv(list1,x)
#     # ans = list1.count(x) / len(list1)
#     return ans
#
# def f(n,k,list1 = None):
#     if not list1:
#         # list1 = [[None] for i in range(n)]
#         list1 = []
#         for i in range(n):
#             list1.append([i])
#     else:
#         length = len(list1)
#         for i in range(length):
#             list_q = list1.pop(0)
#             # n = len(list_q)
#             for j in list_q:
#                 if j == 0:
#                     continue
#                 else:
#                     list_x = []
#                     for x in range(j):
#                         list_x.append(x)
#                     list1.append(list_x)
#     if k == 0:
#         return list1
#     print(list1)
#     return f(n,k-1,list1)
#
# def gailv(list1,x):
#     n = 0
#     num = 0
#
#     for i in list1:
#         # if i and i[-1] != 0:
#         #     n += 1
#         count = 0
#         for j in i:
#             if j == x:
#                 count += 1
#         num += count / len(i)
#     num /= len(list1)
#     return num
# print(g(10,5,1))

# 人 = {"新": 67, "青": 8, "玉": 33, "小": 25}
# for 名字, 岁 in 人.items() :
#   print("小",名字,"今年",岁)


# list1 = [1,3,4,5,3,2]
#
# max1 = max(list1)
# idx = list1.index(max1)
# print(idx)
# str1 = "aw"
# if str1:
#   print("ye")

# list1 = [ [3,4], [2,3], [1,2] ]


# sorted_word_to_cnt = sorted(list1,key=lambda a:a[1],reverse=True)
# list1 = sorted(list1,key=lambda x:x[0])
# print(list1)

# print(-48%99)
# for i in range(1,-1,-7):
#     print(i)

# print("qqq")
# import numpy
# print(numpy)
# import tensorflow as tf

# nums = [1,2,3]
# nums.remove(0)
# nums.remove()
# print(nums)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



#-----------------------------------------------------概率-----
# def test_p1(n, k, x):
#     if n == 0:
#         return 0
#     if k == 0:
#         return 0 if x >= n else 1 / n
#
#     return 0 if x >= n else sum([test_p1(i, k - 1, x) / n for i in range(1, n)])
#
#
# def test_p2(n, k, x):
#     if n == 0:
#         return 0
#     if k == 0:
#         return 1
#
#     return sum([test_p2(i, k - 1, x) / n for i in range(1, n)])
#
#
# def test_p(n, k, x):
#     return test_p1(n, k, x) / test_p2(n, k, x)
#
#
# def test_pp(n, k, x):
#     # 初始化数组全部为 None   dp1:分子(f(n,k) == X)的概率，dp2：分母 不抛异常的概率
#     dp1 = [[None for j in range(k + 1)] for i in range(n + 1)]
#     dp2 = [[None for j in range(k + 1)] for i in range(n + 1)]
#
#     for i in range(k + 1):
#         dp1[0][i] = 0
#         dp2[0][i] = 0
#
#     for i in range(n + 1):
#         dp1[i][0] = 0 if x >= i else 1 / i
#         dp2[i][0] = 0 if i == 0 else 1
#
#     for i in range(1, n + 1):
#         for j in range(1, k + 1):
#             dp1[i][j] = sum([dp1[m][j - 1] / i for m in range(i)])
#             dp2[i][j] = sum([dp2[m][j - 1] / i for m in range(i)])
#
#     return dp1[n][k] / dp2[n][k]

#
# class Solution:
#     def knightProbability(self, N, K, r, c):
#         """
#         :type N: int
#         :type K: int
#         :type r: int
#         :type c: int
#         :rtype: float
#         """
#
#         def s1(n, k, r, c):
#             if k == 0:
#                 list1 = [1, 2, -1, -2]
#                 count = 0
#                 for i in list1:
#                     for j in list1:
#                         if abs(i) != abs(j):
#                             if 0 <= r + i < n and 0 <= c + j < n:
#                                 count += 1
#
#                 return count / 8
#
#
#
#             sum([s1(n,k,r,c),s1(n,k,r,c),s1(n,k,r,c),s1(n,k,r,c),s1(n,k,r,c),s1(n,k,r,c),s1(n,k,r,c),s1(n,k,r,c)])
#             # return sum(s1(n, k - 1, r + 1, c + 2), s1(n, k - 1, r + 1, c - 2),
#             #            s1(n, k - 1, r + 2, c + 1), s1(n, k - 1, r + 2, c - 1),
#             #            s1(n, k - 1, r - 1, c + 2), s1(n, k - 1, r - 1, c - 2),
#             #            s1(n, k - 1, r - 2, c + 1), s1(n, k - 1, r - 2, c - 1))
#
#         def s2():
#             return
#
#         return s1(N, K, r, c)
#
# # def test_p2(n, k, x):
# #     if n == 0:
# #         return 0
# #     if k == 0:
# #         return 1
#
# #     return sum([test_p2(i, k - 1, x) / n for i in range(1, n)])
#
# a = sum([1, 2, 3, 4, 5, 6, 7, 8])
# print(a)

#
# c = "c"
# c = "1"
#
# print(c.isdigit())

# aaa = "1.0.1."
#
# list1 = aaa.split(".")
#
# for i in list1:
#     for c in i:
#         print(i.isdigit(),"---")


# p = [1,2,3,4,5,6,7,1,2,3,4,5,6,7]
# limit = 7
# p = [2,4]
# limit = 5
# p = sorted(p,reverse=True)
# print(p)
# for i in p:
#     if limit - i >= 0:
#         p.remove(i)
#
# print( len(p))
# # p.sort(reverse=True)
# temp = []
# q = []
# for i in p:
#     # print(i)
#     if 7 -i in p:
#         p.remove(7-i)
#         print(p)
#     temp.append(i)
#     # temp.append(a)
#     # q.append([i,a])
# print(temp)
# print(q)



# str1 = "0001"
# print(int(str1))


# def if_valid( str1, idx):
#     if len(str1) == 1:
#         return str1
#     # if (idx!=len(str1)-1) and str1[-1] =="0":
#     #     return False
#     # if (str1[0] == "0" and idx != 0):
#     #     print("yes")
#     # if (idx  != len(str1) and str1[-1] == "0"):
#     #     print("yew")
#
#     if (str1[0] == "0" and idx != 0) or (idx+1 != len(str1) and str1[-1] == "0" ) or int(str1) == 0 or (idx != 0 and int(str1[:idx + 1]) == 0):
#         return False
#     elif idx+1 != len(str1):
#         return str1[:idx + 1] + "." + str1[idx + 1:]
#     else:
#         return str1
# str1 = "10"
# for i in range(len(str1)):
#     q = if_valid(str1,i)
#     print(q)
# if_valid(str1,idx)

# str1 = "0"
# print(if_valid(str1,1))



# str1 = "-3"
# str1 = "5"
# print(str1.isdigit())

# import collections
#
# dict1 = collections.defaultdict(int)
#
# dict1[1] += 1
# print(dict1)

# dict1[3].add((1,2))
# dict1[1].add(1)
# print(dict1)
#
# ans = max(dict1.values())
# print(ans)

#
# set1 = set()
# set1.add((1,2))
# set1.add((1,2))
# if (1,2) in set1:
#     print("e")
# print(set1)

# list1 = []
# list2 = [1,2]
# list1.extend(list2)
# print(list1)


# print(0^1)
# print(1^1)
# print(2<<0)

# ans = [1]
# ans1 = None
# ans += ans1
# print(ans)

# list1 = [1,2,3,4]
# for i in range(10):
#      strq = 'str'+str(i)
#
#      strq = str(i)
#      "str"+str("i") = str(i)
#
# s1 = 1
# s2 = 2
# s3 = 3
# s4 = 4

# list1 = [ [1,2,3],[4],[5,6,7],[8,9]]
# n = len(list1)
# for q in range(len(list1[0])):
#     for w in range(len(list1[1])):
#         for e in range(len(list1[2])):
#             for r in range(len(list1[3])):
#                 print([list1[0][q],list1[1][w],list1[2][e],list1[3][r]])





# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# -----------------------------排列组合----------------------
# import itertools

# list1 = itertools.permutations([1,2,3,4],3)
# list1 = itertools.combinations([1,2,3,4],3)
# list1 = itertools.product([1,2,3,4],repeat=3)
# print(list(list1))

# ------------------------------------------------------------------yield---------------
# passwd = ("".join(x) for x in itertools.product("123",repeat=2))
#
# def password(passwd):
#     while True:
#         yield next(passwd)
#
# for i in password(passwd):
#     print(i,end="   ")

# print(password(21))

# def func():
#     x = 1
#     while True:
#         y = (yield x)
#         x += y
#
# geniter = func()
# print(geniter.__next__() ) # 1
# print(geniter.send(3) )# 4
# print(geniter.send(10) )# 14

# import re

# regex = "1(([3]\d)|(47))\d{8}"
# str1 = "phone:13912345678qqq"
# str1 = "131123456789"
# a = re.match(regex,str1)
# b = re.findall(regex,str1)
# c = re.search(regex,str1)
# print(a)
# print(b)
# print(c.group())


# import numpy as np
#
# pi = np.asarray([0.2,0.4,0.4])
# a1 = np.asarray([[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]])
# b1 = np.asarray([[0.5,0.5],[0.4,0.6],[0.7,0.3]])
# print(pi)
# print(pi.dot(b1))
# print(pi.dot(a1))
# print(pi.dot(a1).dot(b1))


# pi = np.asarray([[0.2,0.4,0.4]])
# pi_T = pi.T
# print(pi)
# print(pi.shape)
#
# print(pi_T,pi_T.shape)



# s = "aabbc"
# print(s[::-1])
#
# temp = [[1,2,3,4,5],[2,4,5],[4,5]]
#
# ans = []
# temp = [1,3,4]
# end = 0
# while temp:
#     start = end
#     end = temp.pop(0)+1
#     ans.append(s[start:end])
# print(ans)
# s = "qweer"
# start = 1
# end = 2
#
# print(s[start:end+1] )
# print(s[start:end+1:])

# set1 = {1,2,3}
#
# set1.pop()

# key = "abc"
# n = 3
# dict2 = {}
# for i in range(n):
#     dict2[key[:i+1]] = dict2.get(key[:i+1],0) + 3


# dict1 = {"a":1,"b":2,"c":4,"d":3}
#
# # dict1 = { sorted() for k,v}
# dict2 = dict(sorted(dict1.items(),key=lambda item:item[1],reverse=True))
# print(dict2)
# ans = "".join(k*v for k,v in dict2.items())
# print(ans)
# for i in range(-1,3):
#     print(i)
#
# dict1 = {}
# dict2 = {}
# dict1[(1,2)] = 1
# dict2[(2,1)] = 2
# dict1.update(dict2)
# print(dict1)


# list1 = [7,1,-5,3,-6,4]
#
# n = len(list1)
# left = 0
# right = 0
#
# ans = 0
# sum1 = 0
# while right < n and left <= right:
#     sum1 += list1[right]
#     if sum1 > 0:
#         right += 1
#         ans = max(ans,sum1)
#     else:
#         sum1 = 0


# print(1)
# print(2)


# s = "3[a2[c]]"
# print(s)
#
# class Solution:
#     def decodeString(self, s,idx=0):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if not idx == len(s):
#             return ""
#         stack_num = [1]
#         stack_str = []
#         ans = ""
#         str1 = ""
#         n = len(s)
#         for i in range(idx,n):
#             if s[i].isdigit():
#                 stack_num.append(int(s[i]))
#                 stack_str.append(str1)
#                 str1 = ""
#                 # stack_num = int(s[i])
#             elif s[i] == "[":
#                 str1 += self.decodeString(s,i+1)
#             elif s[i] == "]":
#                 stack_str.append(str1)
#
#                 while stack_str:
#                     ans = stack_str.pop()*stack_num + ans
#
#                 # ans += str1*stack_num.pop()
#                 return ans
#             else:
#                 str1 += s[i]
#         return ans
# if __name__ == "__main__":
#     a = Solution()
#     q = a.decodeString(s)
#     print("q =",q)



# import random
#
# a = random.randint(0,5)
# a = 3
# b = 2
# list1 = [ [i,j]for i in range(a) for j in range(b)]
# print(list1)

# print(a)



# -----------------------------公约数,leetcode 878. 第 N 个神奇数字----------------------------------

# m = 7
# A = 5
# B = 8
# ans = 0
# min_q = 0
# max_q = B
# for i in range(m):
#
#     if min_q + A < max_q:
#         min_q += A
#         ans = min_q
#     elif min_q + A == max_q:
#         ans = max_q
#         min_q += A
#         max_q += B
#     else:
#         # min_q = B
#         ans = max_q
#         max_q += B
#
#     print(ans)

    # xiao = min_q
    # da = max_q
    # min_q = min(min_q+A,max_q+B)
    # max_q = max(xiao+A,da+B)
    # print(min_q)
    # ans += min_q
    # print(ans)



# -----------------------------正则表达式----------------------------------
# S = "2.0(1)"
# S = "222.123(0123)"


# s = S.split(".","")
# print(s)


# import re

#
# regex = "(\d*\.)|\d*|(\(\d*\))"
# regex = "(\(\d*\)|\d*)"
# ans = re.findall(regex,S)
# for i in ans:
#     print(i)
# print(ans)
# list1 = ans
# print(list1)
# s = "123asd456"
# regex = "\d*|\w*"

# ---------------------------------------分数库--------------------------------

# from fractions import Fraction

# a = Fraction(5,1)
# print(a)


# def num(n):
#     i = n.index(".")
#     num_zheng = Fraction(int(n[:i]),len(n[:i]))
#     n = n[i + 1:]
#     i = n.index("(")
#     num_fen = n[:i]
#     num_xum = n[i + 1:-1]
#     num_zheng += Fraction(int(num_fen), 10 ** len(num_fen))
#     return num_zheng

# print(num("1.23(4)"))



# list1 = [1,2,3,4,5]
#
# for i,num in enumerate(list1):
#     if i == 2:
#         # list1.pop(i)
#         list1.insert(0,1)
#         break
# print(list1)

# ---------------__________________________________-----------zip()函数--------------------
# nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
# nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]

# a = [[1,2,3],[4,5,6]]
# b = [["q","w","e"],["a","s","d"]]
# c = list(zip(a,b))
#
# for i in c:
#     print(i,type(i))
# print(type(c))

# a = [1,2,3]
# b = [4,5,6]
# c = [ q+w for q,w in zip(a,b)]
# print(c)

#
# nums = [1,2,3,4,5]
# ans = [[]]
# for i in nums:
#     for j in range(len(ans)):
#
#         temp = ans[j][:]
#         if (not temp) or i >= temp[-1]:
#             temp.append(i)
#             ans.append(temp[:])
# # ans.pop(0)
# ans = [ i for i in ans if len(i)>=2]
# # for i in ans:
# #     print(len(i))
# print(ans)
# print(len(ans))


# def fun1(list1):
#     n = len(list1)
#     dp = [0] * n
#     ans = []
#     max1 = -1e15
#     for i in range(n):
#         max1 = max(list1[i][0],max1)
#
#     while True:
#         count = 0
#         for i in range(n):
#             m = len(list1[i])
#             if list1[i][dp[i]] < max1 :
#                 if dp[i]+1<m:
#                     dp[i] += 1
#                     break
#                 else:
#                     return ans
#             elif list1[i][dp[i]] == max1:
#                 count += 1
#             else:
#                 max1 = list1[i][dp[i]]
#                 break
#         if count+1 == n:
#             ans.append(max1)
#             for i in range(n):
#                 if i+1 < m:
#                     dp[i] += 1
#                 else:
#                     return ans
#             max1 = list1[0][dp[0]]
#
#
#
#
# print(fun1(list1))



# import numpy as np
#
# list1 = np.array([1,2,3])
# list2 = np.array([4,5,6])
#
# list3 = list1+list2
# print(list3,list3.shape)
#
#
# list4 = [a+b for (a,b) in zip(list1,list2)]
# print(list4,type(list4))

#
# list1 = [1,2,3]
#
# def mysum(*args):
#     return sum(args)
#
# print(mysum(*list1))


# class Solution:
#     """
#     @param str: An array of char
#     @param offset: An integer
#     @return: nothing
#     """
#
#     def rotateString(self, str, offset):
#
#         # write your code here
#
#         left = 0
#         n = offset - 1
#
#         while left < n:
#             str[left], str[n] = str[n], str[left]
#             left += 1
#             n -= 1
#
#         n = offset
#         right = len(str) -1
#         while n < right:
#             str[right], str[n] = str[n], str[right]
#             right -= 1
#             n += 1
#
#         right = len(str) - 1
#         left = 0
#
#         while left < right:
#             str[left], str[right] = str[right], str[left]
#             left += 1
#             right -= 1
#         return str
# str = [1,2,3,4,5,6,7]
# offset = 3
# a = Solution()
# q = a.rotateString(str,offset)
# print("q = ",q)

# i = 5
# 10e5

# n = 1
# class Solution:
#     """
#     @param n: The number of digits
#     @return: All narcissistic numbers with n digits
#     """
#
#     def getNarcissisticNumbers(self, n):
#         # write your code here
#
#         res = []
#
#         for num in range(10 ** (n - 1) - 1, 10 ** n):
#             ans = 0
#             while num:
#                 temp = num % 10
#                 ans += temp ** n
#                 num //= 10
#             if ans == num:
#                 res.append(num)
#         return res
# a = Solution()
# q = a.getNarcissisticNumbers(n)
# print("q=",q)
# s = "  Life  doesn't  always    give     us  the       joys we want."

# s = "the sky is blue"
# class Solution:
#     """
#     @param: s: A string
#     @return: A string
#     """
#
#     def reverseWords(self, s):
#         # write your code here
#         import re
#
#         regex = "[^\\s]*"
#         q = re.findall(regex,s)
#         print(q)
#         list1 = s.split(" ")
#         print(list1)
#
# a = Solution()
# q = a.reverseWords(s)
# print("q =",q)


# def sleeptime(hour,min,sec):
#     return hour*3600 + min*60 + sec
# second = sleeptime(0,0,1)
# while 1==1:
#
    # time.sleep(second)
    # print ('do action')
#---------------------------------------python 播放音乐,每隔1秒钟自动执行任务-----------------------
# from threading import Timer
# import time
# import pygame
#
# def printHello():
#     print("Hello World")
#     t = Timer(2, printHello)
#     t.start()
#
#
#                      把你的时间循环锁在系统时钟上就行了。轻松点。

# import time
# starttime=time.time()while True:
#   print "tick"
#   time.sleep(60.0 - ((time.time() - starttime) % 60.0))
#

# if __name__ == "__main__":
#     printHello()
#     while True:
#         print("yes")
#     time.sleep(10)
#     path = "C:/Users/huali/Desktop/新建文件夹/others/other/WE214.wav"
#     path = "C:/Users/huali/Desktop/新建文件夹/others/other/1187077700_342839.mp3"
#     pygame.init()
#     print("开始")
#     pygame.mixer.init()
#     track = pygame.mixer.music.load(path)
#     pygame.mixer.music.load(path)
#     pygame.mixer.music.play()
#     time.sleep(10)
#     pygame.mixer.music.stop()



# lst = [1,2,3]
#
#
# for item in lst:
#     if item.isInteger():
#         lst.append(item.getInteger())
#         print("yes")

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# class NestedIterator(object):
#
#     def __init__(self, nestedList):
#         """
#         Initialize your data structure here.
#         :type nestedList: List[NestedInteger]
#         """
#         self.stack = []
#         self.slove(nestedList)
#
#     def next(self):
#         """
#         :rtype: int
#         """
#         return self.stack.pop(0)
#
#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         if self.stack:
#             return True
#         return False
#
#     def slove(self, nestedList):
#         for item in nestedList:
#             if item.isInteger():
#                 self.stack.append(item)
#             else:
#                 self.slove(item)
#
# # Your NestedIterator object will be instantiated and called as such:
# # i, v = NestedIterator(nestedList), []
# # while i.hasNext(): v.append(i.next())

# for i in range(31,-1,-1):
#     print(i)
# list1 = [0,0,1,1,1,2,2]

# a = any(2^1 ^ p in list1 for p in list1)
#
# print(1+a)

# list1 = [1,2,3,4]
# a = list1.index(6)
# print(a)

# list1 = [1,2,3]

# for i,num in enumerate(list1,start=1):
#     for i1,num1 in enumerate(list1,start=2):
#         print(i,i1,num,num1)
# help(enumerate)

# ans = [1,2]
# ans = ans*2 + ans*2
# print(ans)

# ans.remove(1)
# print(ans)

# dict1 = {"q":[1,2,3]}
#
# for i in dict1['q']:
#     print(i)

# set1 = set()
# set1.add([1,2,3])
# print(set1)



# import tensorflow as tf
# import keras

# print(1)

#---------------------------------------python 播放音乐,每隔1秒钟自动执行任务-----------------------
# from threading import Timer
# import time
# import pygame
# a = 1
# def printHello(a):
#     a += 1
#     print("Hello World")
#     t = Timer(2, printHello,[a])
#     t.start()
#     print("123")
#     print(a)
#     # while True:
#     #     a = 1
# printHello(a)

#                      把你的时间循环锁在系统时钟上就行了。轻松点。

# import time
# starttime=time.time()
#
# while True:
#   print "tick"
#   time.sleep(60.0 - ((time.time() - starttime) % 60.0))
#

#
# if __name__ == "__main__":
#     printHello()
#     while True:
#         print("yes")
#     time.sleep(10)
#     path = "C:/Users/huali/Desktop/新建文件夹/others/other/WE214.wav"
#     path = "C:/Users/huali/Desktop/新建文件夹/others/other/1187077700_342839.mp3"
#     pygame.init()
#     print("开始")
#     pygame.mixer.init()
#     track = pygame.mixer.music.load(path)
#     pygame.mixer.music.load(path)
#     pygame.mixer.music.play()
#     time.sleep(10)
#     pygame.mixer.music.stop()


# str1 = "0,0"
#
# k,v = str1.split(",")
# k = int(k)
# v = int(v)
# print(k,v)
#
# dict1 = {}
# dict1[(1,2)] = 1
# print(dict1)

# v = {(1,2)}
# v1 = v.add((3,4))
# print(v)
# print(v1)

# list1 = [(0,1)]
# list3 = []
# list2 = list1 + [(1,2)]
# list3.append(list1+[(1,2)])
# print(list2)
# print(list3)


# list1 = [1,3,5,3]
# print(sorted(list1))

# list1 = [1,2,3,4,5]
# num_wanted = 3
# n = min(num_wanted,len(list1)) 
# ans = sum(sorted(list1)[:n])
# print(ans)


# import numpy as np
# import pdb
#
# # pdb.set_trace()
# a1 = np.array([[1],[2],[3],[4],[5]])
# c = 2
# # print(a1 * c)
# a1 = np.array([[1,2,3,4,5]])
#
# a2 = np.array([[1,2,3,4,5]])


# print(a1.shape,a2.shape)

# a1 = np.array([ [1,2],[3,4] ])
# a2 = np.array([ [1,2,],[3,4]])
# print(np.matmul(a1,a2))
# print(a1.dot(a2))

# print("q".isdigit())

################编辑距离##################

str1 = "abc"
str2 = "abd"

def distance(str1:str,str2: str) -> int:
    n1 = len(str1)
    n2 = len(str2)

    dp = [[0] * (n1+1)  for i in range(n2+1)]

    for i in range(n2+1):
        dp[i][0] = i
    for j in range(n1+1):
        dp[0][j] = j

    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    return dp[-1][-1]

n = distance(str1,str2)
print(str1,str2,n)










