#-*- coding:utf-8 -*-
#@Date   : 2018/9/13
#@Author : suyifan
#@File   : 746. Min Cost Climbing Stairs.py


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# cost = [0,0,0,1]


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost)
        list1 = [-1] * length
        print(len(list1),"---",list1)
        self.solve(cost,list1,length-1)
        return min(list1[-1],list1[-2])


    def solve(self,cost,list1,idx):
        if idx < 0:
            return 0

        if list1[idx] != -1:
            return list1[idx]

        list1[idx] =  min(self.solve(cost,list1,idx-2),self.solve(cost,list1,idx-1))+cost[idx]
        print(list1)

        return list1[idx]



a = Solution()
q = a.minCostClimbingStairs(cost)
print("q=",q)