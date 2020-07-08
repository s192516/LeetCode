#-*- coding:utf-8 -*-
#@Date   : 2019/1/13
#@Author : suyifan
#@File   : 973. K Closest Points to Origin.py

points = [[3,3],[5,-1],[-2,4]]
K = 2


class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        list1 = []
        for i in points:
            n = i[0]**2 + i[1]**2
            # dict1[n] = i
            list1.append([n,i])
        # print(list1)

        # ans = [ for i in ]
        ans = sorted(list1,key=lambda i:i[0])
        # for i in range
        #
        # ans = [v for k,v]
        # print(ans)

        ans = ans[:K]
        ans = [ i[1] for i in ans]
        return ans
a = Solution()
q = a.kClosest(points,K)
print("q =",q)