#-*- coding:utf-8 -*-
#@Date   : 2019/5/21
#@Author : huali
#@File   : 1042. Flower Planting With No Adjacent.py



N = 3
paths = [[1,2],[2,3],[3,1]]
N = 4
paths = [[1,2],[3,4]]
class Solution:
    def gardenNoAdj(self, N: int, paths: "List[List[int]]") -> "List[int]":

        ans = [0] * N

        for i, t in enumerate(paths):
            count = 1
            n = i
            while n < N and ans[n] == 0:
                if count % 4 == 0:
                    ans[n] = 4
                else:
                    ans[n] = count % 4
                count += 1
                n = paths[n][1]-1
        return ans


a = Solution()
q = a.gardenNoAdj(N,paths)
print("q =",q)