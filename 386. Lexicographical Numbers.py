#-*- coding:utf-8 -*-
#@Date   : 2019/1/18
#@Author : suyifan
#@File   : 386. Lexicographical Numbers.py

n = 10
n = 100
n = 192
n = 333
class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        ans = [1] * n

        for i in range(1, n):
            before = ans[i - 1]
            if before * 10 <= n:
                ans[i] = before * 10
            elif before % 10 != 9:
                if before + 1 <= n:
                    ans[i] = before + 1
                else:
                    while before >= 10:
                        before //= 10
                    before += 1
                    ans[i] = before
            else:
                before += 1
                while before % 10 == 0:
                    before //= 10
                ans[i] = before
        return ans