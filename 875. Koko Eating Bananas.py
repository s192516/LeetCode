#-*- coding:utf-8 -*-
#@Date   : 2018/10/24
#@Author : suyifan
#@File   : 875. Koko Eating Bananas.py

piles = [3,6,7,999]
H = 6

# piles = [312884470]
# H = 968709470
# H = 312884470


# piles = [3,6,7,11]
# H = 8

# piles = [30, 11, 23, 4, 20]
# H = 6
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """


        n = len(piles)
        if n >= H:
            return max(piles)

        left = 1
        right = max(piles)
        while left < right:
            sum1 = 0
            mid = (left + right) // 2
            for num in piles:
                n = num / mid
                print(num,mid,n)
                if n <= 1:
                    sum1 += 1
                else:
                    if int(n) == n:
                        sum1 += int(n)
                    else:
                        sum1 += int(n) + 1
                if sum1 > H:
                    # ans = mid + 1
                    left = mid + 1
                    break
            if sum1 <= H:
                ans = mid
                right = mid
            # print(left,right)
        return left

a = Solution()
q = a.minEatingSpeed(piles,H)
print("q =",q)