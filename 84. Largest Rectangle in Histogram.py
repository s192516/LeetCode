#-*- coding:utf-8 -*-
#@Date   : 2018/12/11
#@Author : suyifan
#@File   : 84. Largest Rectangle in Histogram.py


heights = [2,1,5,6,2,3]
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        stack = []
        heights.append(0)
        res = 0
        for i, num in enumerate(heights):
            while stack and num < heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    idx = stack[-1]
                else:
                    idx = -1
                res = max(res, (i-idx-1) * height)

            stack.append(i)

        return res

a = Solution()
q = a.largestRectangleArea(heights)
print("q =",q)