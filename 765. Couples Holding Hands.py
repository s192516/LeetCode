#-*- coding:utf-8 -*-
#@Date   : 2019/1/14
#@Author : suyifan
#@File   : 765. Couples Holding Hands.py

row = [3,2,0,1]
row = [0,2,1,3]
row = [0,2,1,4,3,5]
class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)
        dp = [None] * n
        dict1 = {}
        for i,num in enumerate(row):
            dict1[num] = i

        ans = 0
        for i in range(0,n,2):
            # if row[i] // 2 != row[i+1] // 2:
            while row[i]//2 != row[i+1] // 2:
                ans += 1
                if row[i] % 2 == 0:
                    num = row[i] + 1
                else:
                    num = row[i] - 1

                idx = dict1[num]
                if idx % 2 == 0:
                    idx += 1
                else:
                    idx -= 1
                row[i],row[idx] = row[idx],row[i]

        return ans
a = Solution()
q = a.minSwapsCouples(row)
print("q =",q)