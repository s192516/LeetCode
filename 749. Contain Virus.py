#-*- coding:utf-8 -*-
#@Date   : 2019/1/18
#@Author : suyifan
#@File   : 749. Contain Virus.py

grid =[[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]

grid = [[1,1,1],
 [1,0,1],
 [1,1,1]]

class Solution:
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        set1 = ((1,0),(-1,0),(0,1),(0,-1))
        height = len(grid)
        width = len(grid[0])
        dict1 = dict() #
        set2 = set() # 记录所有的病毒区域
        set3 = set()
        # count_ganran = 0
        # while True:
        for i in range(height):
            for j in range(width):
                if (i,j) not in set2:
                    if grid[i][j] == 1:
                        count_ganran = 0
                        set2.add((i,j))
                        set3.add((i,j))
                        zhalan = 0
                        while set3:
                            q,w = set3.pop()
                            for qq,ww in set1:
                                if 0<= q+qq<height and 0 <= w+ww < width :
                                    if grid[q+qq][w+ww] == 1:
                                        if (q+qq,w+ww) not in set2:
                                            set2.add((q+qq,w+ww))
                                            set3.add((q+qq,w+ww))
                                    elif grid[q+qq][w+ww] == 0:
                                        count_ganran += 1

                        dict1[(i,j)] = count_ganran
        print(dict1)



a = Solution()
q = a.containVirus(grid)
print("q =",q)