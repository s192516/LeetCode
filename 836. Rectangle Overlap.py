#-*- coding:utf-8 -*-
#@Date   : 2018/10/8
#@Author : suyifan
#@File   : 836. Rectangle Overlap.py

[0,0,1,1]
[1,0,2,1]


class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if rec2[3] >= rec1[3]:
            max1 = rec2
            min1 = rec1
        else:
            max1 = rec1
            min1 = rec2

        if max1[0] >= min1[2]:
            return False
        else:
            if max1[1] >= min1[3]:
                return False
            else:
                return True

        if rec2[4] >= rec1[4]:
            max1 = rect2
            min1 = rect1
        else:
            max1 = rect1
            min1 = rect2

        if max1[1] >= min1[3]:
            return False
        else:
            if max1[0] >= min1[2]:
                return False
            else:
                return True


