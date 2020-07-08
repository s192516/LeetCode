#-*- coding:utf-8 -*-
#@Date   : 2018/9/2
#@Author : huali
#@File   : 38.CountAndSay.py
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221



# class Solution:
#     def countAndSay(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """
#         rtype = ""
#         count = 1
#         n = str(n)
#
#         if len(n) ==1:
#             rtype = "1"+n
#
#         for i in range(len(n)-1):
#             if n[i+1] is n[i]:
#                 count += 1
#                 # print(i)
#
#             else:
#                 rtype +=str(count)
#                 rtype +=n[i]
#
#                 count = 1
#                 # print("n1=",n[i],"n=",n)
#                 # print(rtype)
#
#             if i == len(n)-2:
#                 rtype += str(count)
#                 rtype += n[i+1]
#                 # print(rtype)
#         return rtype

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221

n = 5

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        rtype = "1"
        str1 ="1"
        qq = 1
        count =1

        if n > 0:
            # rtype = "1" + str1
            rtype ="1"
            str1 =rtype
            qq +=1

        if n > 1:
            rtype = "11"
            str1 =rtype
            qq += 1


        while qq <= n :
            rtype = ""
            for i in range(len(str1)-1):
                if str1[i+1] is str1[i]:
                    count += 1
                    # print(i)

                else:
                    rtype +=str(count)
                    rtype +=str1[i]

                    count = 1
                    # print("n1=",n[i],"n=",n)
                    # print(rtype)

                if i == len(str1)-2:
                    rtype += str(count)
                    rtype += str1[i+1]
                    # print(rtype)
            count =1
            qq +=1
            str1 =rtype
            # print(rtype)



        return rtype




a = Solution()
q =a.countAndSay(n)
print(q)