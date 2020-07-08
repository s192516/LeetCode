#-*- coding:utf-8 -*-
#@Date   : 2018/12/26
#@Author : suyifan
#@File   : 436. Find Right Interval.py


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

intervals = [ [3,4], [2,3], [1,2] ]
# intervals = [ [1,4], [2,3], [3,4] ]
# --------------------------这道题实际上是一个intervals类,里面不是列表,而是start,和end两个属性,
#注意把intervals[0][0] 换成intervals[0].start
class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """

        import collections
        count = collections.Counter()
        for i, num in enumerate(intervals):
            count[str(num)] = i
        list1 = sorted(intervals, key=lambda x: x[0])
        # list1 = sorted(list1,key=lambda x:x[0])
        n = len(list1)
        ans = [-1] * n
        for i, l in enumerate(intervals):
            target = l[1]
            if list1[-1][0] < target:
                continue
            left = 0
            right = n

            while left < right:
                mid = (left + right) // 2
                if list1[mid][0] >= target:
                    right = mid - 1
                    ans[i] = count[str(list1[mid])]
                else:
                    left = mid + 1
            # list1[i] = ans
        return ans

a = Solution()
q = a.findRightInterval(intervals)
print("q =",q)