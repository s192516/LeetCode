#-*- coding:utf-8 -*-
#@Date   : 2018/10/15
#@Author : suyifan
#@File   : 811. Subdomain Visit Count.py

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict1 = {}

        for i in cpdomains:
            list1 = i.split()
            count = int(list1[0])
            str1 = list1[1]

            while str1 :
                if str1 not in dict1:
                    dict1[str1] = count
                else:
                    dict1[str1] += count
                while str1 and str1[0] != ".":
                    str1 = str1[1:]
                    print(str1)
                str1 = str1[1:]

        list2 = []
        for k,v in dict1.items():
            str1 = str(v) + " " + str(k)
            list2.append(str1)
        return list2

a = Solution()
q = a.subdomainVisits(cpdomains)
print("q =",q)