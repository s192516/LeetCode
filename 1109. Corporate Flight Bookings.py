#-*- coding:utf-8 -*-
#@Date   : 2019/7/9
#@Author : huali
#@File   : 1109. Corporate Flight Bookings.py



class Solution:
    # 这个方法可以但是超时
    # 需要使用扫描线法
    def corpFlightBookings(self, bookings: "List[List[int]]", n: int) -> "List[int]":
        ans = [0] * n
        for book in bookings:
            for i in range(book[0],book[1]+1):
                ans[i-1] += book[2]
        return ans

    '''
    只要敲几行代码就可以实现自己心里所想的事情,
    真的是一种很奇妙的感觉
    '''

