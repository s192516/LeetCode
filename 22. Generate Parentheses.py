#-*- coding:utf-8 -*-
#@Date   : 2018/10/9
#@Author : suyifan
#@File   : 22. Generate Parentheses.py


n = 3


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtype = []
        str1 = ""
        self.solve(n, rtype, str1)
        return rtype

    def solve(self, n, rtype, str1):
        if len(str1) == 2 * n:
            temp = self.valid(rtype, str1)
            # print(temp)
            if temp == 0:
                # print("yes")
                rtype.append(str1)
                # print(rtype, str1)

        else:
            str1 += "("
            if self.valid(rtype, str1) >= 0:
                self.solve(n, rtype, str1)
                str1 = str1[:-1]
                str1 += ")"
                if self.valid(rtype, str1) >= 0:
                    self.solve(n, rtype, str1)

    def valid(self, rtype, str1):
        count = 0
        for i in str1:
            if i == "(":
                count += 1
            else:

                count -= 1
        return count

a = Solution()
q = a.generateParenthesis(n)
print("q =",q)