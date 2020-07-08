#-*- coding:utf-8 -*-
#@Date   : 2019/1/18
#@Author : suyifan
#@File   : 547. Friend Circles.py

M = [[1,1,0],
 [1,1,1],
 [0,1,1]]
M = [[1,1,0],
 [1,1,0],
 [0,0,1]]
M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]] # ans = 1
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """


        n = len(M)
        set1 = set()
        ans = 0
        set2 = set()
        for i in range(n):
            for j in range(i,n):




                if M[i][j] == 1:
                    M[i][j] = 0
                    if j not in set2:
                        set1.add((i,j))
                        set2.add(j)
                    ans += 1

                while set1:
                    q,w= set1.pop()
                    for e in range(n):
                        if M[w][e] == 1:
                            if e not in set2:
                                set2.add(e)
                                set1.add((w,e))
                            M[w][e] = 0
        return ans

a = Solution()
q = a.findCircleNum(M)
print("q =",q)
