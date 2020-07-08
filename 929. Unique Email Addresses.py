#-*- coding:utf-8 -*-
#@Date   : 2018/10/29
#@Author : suyifan
#@File   : 929. Unique Email Addresses.py

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        set1 = set()
        for email in emails:
            list1 = email.split("@")
            n = len(list1[0])
            for i in range(n):
                if list1[0][i] == "+":
                    list1[0] = list1[0][:i]
                    break
            list2 = list1[0].split(".")
            str1 = ""
            for s in list2:
                str1 += s
            str1 += list1[1]
            # list1[0] = str1

            set1.add(str1)
            # print(set1)
        return len(set1)

a = Solution()
q = a.numUniqueEmails(emails)
print("q =",q)