#-*- coding:utf-8 -*-
#@Date   : 2020/7/10
#@Author : huali
#@File   : 309. Best Time to Buy and Sell Stock with Cooldown.py


prices = [1,2,3,0,2]

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp = [0 for i in range(n)]

        