#-*- coding:utf-8 -*-
#@Date   : 2018/9/5
#@Author : huali
#@File   : 12.IntegerToRoman.py

num = 3498
num = 60



class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # dict1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        rtype = ""
        while num >= 1000:
            rtype += "M"
            num -= 1000
        if num >= 900:
            rtype += "CM"
            num -= 900
        if num >= 500:
            rtype += "D"
            num -= 500
        if num >= 400:
            rtype += "CD"
            num -= 400

        while num >= 100:
            rtype += "C"
            num -= 100
        if num >= 90:
            rtype += "XC"
            num -= 90
        if num >= 50:
            rtype += "L"
            num -= 50
        if num >= 40:
            rtype += "XL"
            num -= 40

        while num >= 10:
            rtype += "X"
            num -= 10
        if num == 9:
            rtype += "IX"
            num -= 9
        if num >= 5:
            rtype += "V"
            num -= 5
        if num == 4:
            rtype += "IV"
            num -= 4
        while num > 0:
            rtype += "I"
            num -= 1
        return rtype


        # print(num,rtype)
        # if num == 500:
        #
        # if num >400:
        #     rtype

a = Solution()
q = a.intToRoman(num)
print("q= ",q)




