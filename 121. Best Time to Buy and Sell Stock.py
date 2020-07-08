#-*- coding:utf-8 -*-
#@Date   : 2018/9/13
#@Author : suyifan
#@File   : 121. Best Time to Buy and Sell Stock.py

#### 考虑数组为空或者长度为1情况
prices = []
prices = [1]
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
prices = [1,2,4]
prices = [2,1,2,1,0,1,2]
prices = [3,3,5,0,0,3,1,4]
prices = [3,3,5,2,2,3,0]
######max 7 1 5 5 6 6
######min 7 1 1 1 1 1
print(prices)


#### for 循环一路找过去寻找最大的差值
#### 长度小于2直接返回0
#### 最开始要设置一大堆东西
#### 当最小值刷新后,重置最大值


# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices) <= 1:
#             return 0
#
#         min_price = prices[0]
#         max_price = 0
#         max_profit = prices[1] - prices[0]
#         idx_min = 0
#         idx_max = 1
#         for i in range(1,len(prices)):
#             if prices[i] < min_price :
#                 min_price = prices[i]
#                 idx_min = i
#             if prices[i] >= max_price:
#                 max_price = prices[i]
#                 idx_max = i
#             if idx_min > idx_max and idx_min + 1 < len(prices):
#                 idx_max = idx_min + 1
#                 max_price = prices[idx_max]
#
#             if max_profit < max_price - min_price and idx_max > idx_min:
#
#                 max_profit = max_price - min_price
#
#         if max_profit > 0 :
#             return max_profit
#         else:
#             return 0
#
#
#
#
# a = Solution()
# q = a.maxProfit(prices)
# print("q=",q)

prices = []
prices = [1]
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
prices = [1,2,4]
prices = [2,1,2,1,0,1,2]
prices = [3,3,5,0,0,3,1,4]
prices = [3,3,5,2,2,3,0]

print(prices)


#### 一个for循环过去,如果当前值减去当前最小值的差大于之前的差则更新
#### 如果是负数返回0

class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        min_prices = min(prices[0],prices[1])
        max_prices = prices[1]
        max_profit = max_prices - min_prices

        for i in range(2,len(prices)):
            min_prices = min(prices[i],min_prices)
            if prices[i] - min_prices > max_profit:
                max_profit = prices[i] - min_prices

        if max_profit > 0:
            return max_profit
        else:
            return 0




a = Solution()
q = a.maxProfit(prices)
print("q=",q)