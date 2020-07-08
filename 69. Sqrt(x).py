#-*- coding:utf-8 -*-
#@Date   : 2018/9/25
#@Author : suyifan
#@File   : 69. Sqrt(x).py

# x = 1
#
# class Solution:
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         left = 0
#         right = x + 1
#         ans = 0
#         while  left < right :
#             mid = (left + right) // 2
#             if self.guess(mid,x):
#                 left = mid + 1
#                 ans = mid
#             else:
#                 right = mid
#
#         return ans
#
#     def guess(self,mid,x):
#         if mid ** 2 <= x:
#             return True
#         else:
#             return False
#
#
#
# a = Solution()
# q = a.mySqrt(x)
# print("q=",q)


n =16


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
       """
        yushu = 0
        shang = ""
        temp = 0
        n = str (x)

        if  len(n) %2 ==0:
            begin =0
        else :
            beichushu = int(n[0])
            begin =1
            if beichushu == 0:
                return 0
            elif beichushu  < 4:
                shang +="1"
                yushu = beichushu - 1
                temp = 1
            elif beichushu < 9:
                shang += "2"
                yushu = beichushu -4
                temp = 2
            else:
                shang += "3"
                yushu = beichushu -9
                temp = 3

        for q in range(begin,len(n),2):
            beichushu = yushu * 100 + int(n[q:q + 2])
            for i in range(11):
                chushu = i+20*temp
                if i*chushu > beichushu:
                    shang += str(i - 1)
                    temp = temp * 10 + (i-1)
                    yushu = beichushu - (i-1)* (chushu - 1)
                    break
        shang = int(shang)
        return shang






a = Solution()
q = a.mySqrt(n)
print("q=",q)