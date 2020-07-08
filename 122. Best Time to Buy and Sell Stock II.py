#-*- coding:utf-8 -*-
#@Date   : 2018/9/21
#@Author : suyifan
#@File   : 122. Best Time to Buy and Sell Stock II.py



prices = [7,1,5,3,6,4]
prices = [3,2]
prices = [1,2,3,4,5]
prices = [2,3]
prices = [7,6,4,3,1]
prices = [2,4,1]
prices = [4,1,2]
prices = [4,2,1,2]
prices = [4,1,2,3]

######## 神tmd逻辑,没百度,每一个字都是我自己敲得
######## 然后我自己都没看懂为什么
######## 反正答案就是对的
######## 本来是写到一半的半成品,想先跑一下看看哪里有错误再改
######## 结果竟然发现答案是对的
######## 就把elif的部分都删了
######## 又把两个if合并成了一个if-else
######## 然后就通过了,我也不明白是怎么回事
######## 成绩还挺好,

print(prices)
class Solution:
    def maxProfit(self, prices):

        l1 = len(prices)
        if l1 < 2:
            return 0

        min_prices = max_prices = prices[0]
        if l1 == 2 :
            return max(prices[1]-prices[0],0)

        profit = 0
        for i in range(1, l1):
            if prices[i] > prices[i-1]:
                max_prices = prices[i]
            else:
                profit += max_prices - min_prices
                max_prices = min_prices = prices[i]

        profit += max_prices - min_prices

        return profit

        # profit = 0
        # idx = 0
        # for i in range(1,l1):
        #     if prices[i] > max_prices:
        #         max_prices = prices[i]
        #         idx = i
        #     elif prices[i]
        #     elif prices[i] < min_prices:
        #         min_prices = prices[i]
        #         if i > idx:
        #             max_prices = min_prices
        #             idx = i
        #     else:
        #         profit += max_prices - min_prices
        #         max_prices = min_prices = prices[i]
        #         idx = i
        #
        # profit += max_prices - min_prices
        #
        # return profit




a = Solution()
q = a.maxProfit(prices)
print("q=",q)