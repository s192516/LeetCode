#-*- coding:utf-8 -*-
#@Date   : 2018/9/8
#@Author : suyifan
#@File   : 17. Letter Combinations of a Phone Number.py

digits = "23"
digits = "23"
digits = "234"
# digits = ""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        digit2chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        start = 0
        path = ""
        rtype = []
        self.solve(start,rtype,path,digits,digit2chars)

        return rtype

    def solve(self,start,rtype,path,digits,digit2chars):
        if len(path) == len(digits):
            rtype.append(path)
            return

        for i in digit2chars[digits[start]]:
            path += i
            self.solve(start + 1,rtype,path,digits,digit2chars)
            path = path[: -1]






a = Solution()
q = a.letterCombinations(digits)
print("q= ",q)




