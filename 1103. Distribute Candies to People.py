#-*- coding:utf-8 -*-
#@Date   : 2019/7/10
#@Author : huali
#@File   : 1103. Distribute Candies to People.py

'''
排排坐，分糖果。

我们买了一些糖果 candies，打算把它们分给排好队的 n = num_people 个小朋友。

给第一个小朋友 1 颗糖果，第二个小朋友 2 颗，依此类推，直到给最后一个小朋友 n 颗糖果。

然后，我们再回到队伍的起点，给第一个小朋友 n + 1 颗糖果，第二个小朋友 n + 2 颗，依此类推，直到给最后一个小朋友 2 * n 颗糖果。

重复上述过程（每次都比上一次多给出一颗糖果，当到达队伍终点后再次从队伍起点开始），直到我们分完所有的糖果。注意，就算我们手中的剩下糖果数不够（不比前一次发出的糖果多），这些糖果也会全部发给当前的小朋友。

返回一个长度为 num_people、元素之和为 candies 的数组，以表示糖果的最终分发情况（即 ans[i] 表示第 i 个小朋友分到的糖果数）。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distribute-candies-to-people
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
candies = 7
num_people = 4
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> "List[int]":

        ans = [0] * num_people

        # for i in range(num_peo)

        count = 1
        while candies >= count:
            ans[(count % num_people) - 1] += count
            candies -= count
            count += 1

        ans[(count % num_people) - 1] += candies
        return ans
        # left = 0
        # right = candies
        # ans = [0] * num_people
        # while left < right:
        #     n = (left+right) // 2
        #     if n * (n+1) < candies:
        #         left = n
        #     elif  n * n > candies:
        #         right = n
        #     else:
        #         break
        # yushu = n % num_people
        # count = n // num_people
        # for i in range(num_people):
        #     if i + 1< yushu:
        #         moxiang = i + num_people * (count)
        #         # 等差数列求某项 = 首项 + 公差 * (项数-1) 因为多一项还要+1和-1抵消
        #         sum1 = (i+moxiang) * num_people // 2 # 等差数列求和
        #         # 和= (首项+模项) * 公差 // 2
        #     else:
        #         moxiang = i + num_people * (count-1)
        #         sum1 = (i+moxiang) * num_people // 2
        #     ans[i] = sum1
        # return ans

a = Solution()
q = a.distributeCandies(candies,num_people)
print(f"q={q}")


