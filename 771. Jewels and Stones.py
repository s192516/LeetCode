#-*- coding:utf-8 -*-
#@Date   : 2018/9/6
#@Author : huali
#@File   : 771. Jewels and Stones.py



J = "aA"
S = "aAAbbbb"

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in S:
            if i in J:
                count +=1
        return count



a = Solution()
q = a.numJewelsInStones(J,S)
print("q=",q)