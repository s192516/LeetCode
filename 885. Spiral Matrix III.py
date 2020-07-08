#-*- coding:utf-8 -*-
#@Date   : 2018/10/24
#@Author : suyifan
#@File   : 885. Spiral Matrix III.py

R = 4
C = 1
r0 = 0
c0 = 0

R = 5
C = 6
r0 = 1
c0 = 4

class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        if R * C == 1:
            return [r0, c0]

        # up = down = left = right = 1
        rtype = [[r0, c0]]
        direction = 1
        count = 1
        n = 0
        while R * C > count:
            # if r0 < R and c0 < C:
            #     rtype.append([r0,c0])
            #     count += 1

            if direction % 2 == 1:
                n += 1
            for i in range(n):
                if direction == 1:
                    c0 += 1
                elif direction == 2:
                    r0 += 1
                elif direction == 3:
                    c0 -= 1
                else:
                    r0 -= 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    rtype.append([r0, c0])
                    count += 1

            direction = (direction + 1) % 4

        return rtype


a = Solution()
q = a.spiralMatrixIII(R,C,r0,c0)
print("q =",q)
print(len(q))