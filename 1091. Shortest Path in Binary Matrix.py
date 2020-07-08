#-*- coding:utf-8 -*-
#@Date   : 2019/7/11
#@Author : huali
#@File   : 1091. Shortest Path in Binary Matrix.py

grid = [[0,1],[1,0]]
grid = [[0,0,0],[1,1,0],[1,1,0]]
class Solution:
    def shortestPathBinaryMatrix(self, grid: 'List[List[int]]') -> int:
        import collections
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return False

        length = len(grid)
        width = len(grid[0])
        # dict1 = collections.defaultdict(list)
        # dict1[(0,0)] = [(0,0)]
        # for k,v in dict1.items():
        #     i,j = k[0],k[1]
        #     for ii in range(-1,2):
        #         for jj in range(-1,2):
        #             idx_i,idx_j = i+ii,j+jj
        #             if 0<=idx_i<length and 0<= idx_j<width:
        #                 if grid[idx_i][idx_j] == 0 and (idx_i,idx_j) not in v:
        #                     v1 = v+[(idx_i,idx_j)]
        #                     dict1
        stack = [[(0,0)]]
        while stack:
            path = stack.pop(0)
            i,j = path[-1]
            for ii in range(-1,2):
                for jj in range(-1,2):
                    idx_i ,idx_j = i+ii,j+jj
                    if idx_i == length-1 and idx_j == width-1:
                        # print(path)
                        return len(path)+1
                    if 0<=idx_i<length and 0<=idx_j<width:
                        if grid[idx_i][idx_j] == 0 and (idx_i,idx_j) not in path:
                            stack.append(path+[(idx_i,idx_j)])
        return -1




a = Solution()
q = a.shortestPathBinaryMatrix(grid)
print(f'q = {q}')