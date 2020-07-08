#-*- coding:utf-8 -*-
#@Date   : 2018/8/31
#@Author : huali
#@File   : 883.ProjectionAreaOf3DShape.py

#########这是拆分出来后的版本
grid =[[2,2,2],[2,1,2],[2,2,2]]

class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a = self.fushi(grid)
        b = self.zuoshi(grid)
        c = self.zhengshi(grid)
        rtype =a+b+c
        print(a,b,c)
        return rtype

    def fushi(self,grid):
        a = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    a += 1
        return a

    def zuoshi(self,grid):
        b =0
        for i in range(len(grid)):
            b += max(grid[i])
        return b

    def zhengshi(self,grid):
        c = 0
        d = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[j][i] >d:
                    d = grid[j][i]
            c +=d
            d=0
        return c

q = Solution()
w =q.projectionArea(grid)
print(w)