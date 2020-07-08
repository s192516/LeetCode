#-*- coding:utf-8 -*-
#@Date   : 2018/12/16
#@Author : suyifan
#@File   : 970. Powerful Integers.py

x = 2
y = 3
bound = 10

x = 1
y = 1
bound = 0

x = 1
y = 2
bound = 100
x = 1
y = 1
bound = 3
class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        # for i in range(x+y,bound):
        import math
        if bound < 2:
            return []


        min1 = min(x,y)
        max1 = max(x,y)

        ans = []
        if min1 == 1 and max1 == 1:
            if bound >= 2:
                return [2]
            else:
                return []
        n = int(math.log(bound,y))


        if min1 == 1:
            for i in range(n+1):
                num = min1  + max1 ** i
                ans.append(num)

        else:
            for i in range(n+1):
                idx = 0
                num = min1 ** idx + max1 ** i
                while num <= bound:
                    ans.append(num)
                    idx += 1
                    num = min1 ** idx + max1 ** i


        return list(set(ans))



a = Solution()
q = a.powerfulIntegers(x,y,bound)
print("q =",q)