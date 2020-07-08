#-*- coding:utf-8 -*-
#@Date   : 2018/9/5
#@Author : huali
#@File   : 29. Divide Two Integers.py

dividend = 4
divisor = 1

# dividend = 10
# divisor = 3
#
dividend = 7
divisor = -2
#
dividend = -1
divisor = 1



dividend = -4
divisor = -1

dividend = -2147483648
divisor = 1

dividend = -1021989372
divisor = -82778243
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        """
        想了半天,这不就相当于让我重新发明一遍除法么
        """
        # rtype = 0
        # count = 1
        # divisor1 = 0 - divisor
        # if divisor < 0:
        #     divisor = 0 - divisor
        #     count =  0 - count
        # if dividend < 0:
        #     dividend = 0 - dividend
        #     count = 0 - count
        #
        #
        # while dividend >= divisor:
        #     dividend -= divisor
        #     rtype +=1
        #
        # if count < 0:
        #     rtype = 0 - rtype

        # if rtype > 2147483648:
        #     rtype = 2147483648
        count = 1
        if divisor < 0:
            divisor = 0 - divisor
            count = 0 - count
        if dividend < 0:
            dividend = 0 - dividend
            count = 0 - count

        weishu = len(str(divisor))
        zongchang = len(str(dividend))
        rtype = 0
        str_divident = str(dividend)
        # int_beichushu = int(str_divident[0:weishu])
        int_beichushu = 0


        for i in range(zongchang):

            q = 1
            temp = int_beichushu

            while q < 10:
                int_beichushu += temp
                q += 1

            int_beichushu += int(str_divident[i])

            q = 1
            temp = rtype
            while q < 10:
                rtype += temp
                q += 1

            while int_beichushu >= divisor:
                int_beichushu -= divisor
                rtype += 1



        if count < 0:
            rtype = 0 - rtype

        if rtype > 2147483647:
            rtype = 2147483647


        return  rtype

a = Solution()
q = a.divide(dividend,divisor)
print("q= ",q)