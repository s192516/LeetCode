#-*- coding:utf-8 -*-
#@Date   : 2018/10/11
#@Author : suyifan
#@File   : 56. Merge Intervals.py


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        return "L"
        n = len(intervals)
        if n == 0:
            return []
        rtype = []
        for i in range(n):
            for j in range(n):
                if intervals[j]:
                    if intervals[i].left <= intervals[j][0]:
                        if intervals[i][1] >= intervals[j][0]:
                            intervals[i][1] = intervals[j][1]
                            intervals[j] = None

                        # if intervals[i][1] < intervals[j][0]:
                        #     continue
                        # else:
                        #     intervals[i][1] = intervals[j][1]
                        #     intervals[j] = None
                    else:
                        if intervals[i][0] <= intervals[j][1]:
                            intervals[i][0] = intervals[j][1]
                            intervals[j] = None
            rtype.append(intervals[i])
        return rtype

