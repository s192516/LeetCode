#-*- coding:utf-8 -*-
#@Date   : 2018/9/6
#@Author : huali
#@File   : 59.Spiral Matrix II.py


n = 4

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rtype = [[None for i in range(n)] for i in range(n)]
        count =1

        i = j = 0
        while count <= n * n:


            while j < n and rtype[i][j] == None:
                rtype[i][j] = count
                count += 1
                j += 1
            j -= 1
            i += 1
            while i < n and rtype[i][j] == None:
                rtype[i][j] = count
                count += 1
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and rtype[i][j] == None:
                rtype[i][j] = count
                count += 1
                j -= 1
            j += 1
            i -= 1
            while i > 0 and rtype[i][j] == None:
                rtype[i][j] = count
                count += 1
                i -= 1
            i += 1
            j += 1



        return rtype


a = Solution()
q = a.generateMatrix(n)
print("q= ",q)