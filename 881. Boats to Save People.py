#-*- coding:utf-8 -*-
#@Date   : 2019/1/3
#@Author : suyifan
#@File   : 881. Boats to Save People.py

people = [2,4]
limit = 5

people = [1,2]
limit = 3

people = [5,1,4,2]
limit = 6

people = [3,2,2,1]
limit = 3
class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()

        left = 0
        right = len(people) - 1
        ans = 0
        while left <= right:
            ans += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1

        return ans


a = Solution()
q = a.numRescueBoats(people,limit)
print("q =",q)