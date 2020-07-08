#-*- coding:utf-8 -*-
#@Date   : 2018/11/25
#@Author : suyifan
#@File   : 401. Binary Watch.py

num = 0
num = 1

class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for i in range(12):
            for j in range(60):
                count = 0
                hour = i
                min = j
                while hour != 0:
                    if hour % 2 == 1:
                        count += 1
                    hour //= 2
                while min != 0 :
                    if min % 2 == 1:
                        count += 1
                    min //= 2
                if count == num:
                    # if i < 10 :
                    #     i = "0" + str(i)
                    if j < 10:
                        j = "0"+ str(j)
                    str1 = str(i) + ":" + str(j)
                    ans.append(str1)
        return ans

a = Solution()
q = a.readBinaryWatch(num)
print("q =",q)