#-*- coding:utf-8 -*-
#@Date   : 2018/9/2
#@Author : huali
#@File   : 27.implementStrstr.py

haystack ="aaa"
needle ="aaaa"

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is "":
            return 0
        counti =-1
        for i in haystack:
            counti += 1
            if i is needle[0]:
                q = counti
                countj =0
                for j in needle:
                    try:
                        if haystack[q] is j:
                            q += 1
                            countj +=1

                            if countj ==len(needle):
                                return counti
                        else:
                            break
                    except:
                        return -1

        return -1


a = Solution()
q = a.strStr(haystack,needle)
print(q)













