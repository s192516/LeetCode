#-*- coding:utf-8 -*-
#@Date   : 2019/1/14
#@Author : suyifan
#@File   : 695. Max Area of Island.py

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid = [[0,1],[1,1]]

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        set2 = ((1,0),(0,1),(-1,0),(0,-1))
        set1 = set()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    set1.add((i,j))
                    temp = 1
                    while set1:
                        a,b = set1.pop()
                        # while set1:
                        for a1,b1 in set2:
                            if 0<=a+a1<m and 0<=b+b1<n and grid[a+a1][b+b1] == 1:
                                set1.add((a+a1,b+b1))
                                grid[a+a1][b+b1] = 0
                                temp += 1
                    ans = max(temp,ans)


        return ans




a = Solution()
q = a.maxAreaOfIsland(grid)
print("q =",q)