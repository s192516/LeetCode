#-*- coding:utf-8 -*-
#@Date   : 2018/11/8
#@Author : suyifan
#@File   : 273. Integer to English Words.py

num = 123456

class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        dict1 = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",0:"Zero"}

        dict2 = {1:"Thousand",2:"Million",3:"Billion"}
        dict3 = {1:""}
        count = 0
        str1 = ""
        while num :
            yushu = num % 1000
            if count :
                str1 += dict2[count]

            count += 1

            while yushu:
                n = yushu % 10
                str1 += dict1[n]
