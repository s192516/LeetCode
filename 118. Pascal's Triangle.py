#-*- coding:utf-8 -*-
#@Date   : 2018/9/8
#@Author : suyifan
#@File   : 118. Pascal's Triangle.py

num = 5

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        self.generateHelper(numRows)

    def generateHelper(self,numRows):
        if numRows > 1:
            self.genertaeHelper(numRows-1)
            self.printNum(numRows)

    def printNum(self,numRows):
        for i in range(numRows):
            print()



a = Solution()
q = a.generate(num)
print("q= ",q)
