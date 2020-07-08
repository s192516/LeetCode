#-*- coding:utf-8 -*-
#@Date   : 2019/1/3
#@Author : suyifan
#@File   : 149. Max Points on a Line.py


point = [[1,1],[2,2],[3,3]]


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        import collections

        dict_x = collections.defaultdict(set)
        dict_y = collections.defaultdict(set)
        dict_y_x = collections.defaultdict(set)
        dict_y__x = collections.defaultdict(set)
        for arr in points:
            x = arr[0]
            y = arr[1]
            dict_x[x].add(y)
            dict_y[y].add(x)
            dict_y_x[y - x].add(x)
            dict_y__x[y + x].add(x)
        ans = 0
        for arr in dict_x.values():
            ans = max(ans,len(arr))

        for arr in dict_y.values():
            ans = max(ans,len(arr))

        for arr in dict_y_x.values():
            ans = max(ans,len(arr))

        for arr in dict_y__x.values():
            ans = max(ans,len(arr))

        # for arr in dict_x.values():
        #     ans = max(ans,len(arr))

        return ans

a = Solution()
q = a.maxPoints(point)
print("q =",q)
