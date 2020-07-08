#-*- coding:utf-8 -*-
#@Date   : 2018/9/6
#@Author : huali
#@File   : 807. Max Increase to Keep City Skyline.py

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]


class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        temp1,temp2 = 0,0
        # max1 = max2 = 0
        list1 = []
        list2 = []
        for i in range(m):
            for j in range(m):
                if grid[i][j] > temp1:
                    temp1 = grid[i][j]
                if grid[j][i] > temp2:
                    temp2 = grid[j][i]
            print(temp1,temp2)
            list1.append(temp1)
            list2.append(temp2)
            temp1 = 0
            temp2 = 0

        sum = 0
        for i in range(m):
            for j in range(m):
               min1 = min(list1[i],list2[j])
               # print(min1)
               sum = sum + (min(list1[i],list2[j]) - grid[i][j])

        return sum

a = Solution()
q = a.maxIncreaseKeepingSkyline(grid)
print("q= ",q)
