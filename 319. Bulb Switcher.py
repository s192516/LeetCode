#-*- coding:utf-8 -*-
#@Date   : 2018/9/13
#@Author : suyifan
#@File   : 319. Bulb Switcher.py

n = 3
n = 6
n = 999999

####如果n 能整除i,也就是说如果i是n的约数,那么第i轮就会被按一下,
####必定有如果n能整除i, n / i = k,则第k轮也会被按一下,一开一关相当于没按
####对于任意一个n 都有 i1,i2...    ...k2,k1为它的约数,
####只有对于平方数 n = i * i, 使它被按奇数次
####日你妈 就一个开根号取整还能比别人慢
import math
class Solution:
    def bulbSwitch(self, n):
        return "%d" % (math.sqrt(n))
        # return  int(math.sqrt(n))

a = Solution()
q = a.bulbSwitch(n)
print("q=",q)