#-*- coding:utf-8 -*-
#@Date   : 2018/10/14
#@Author : suyifan
#@File   : 697. Degree of an Array.py


nums = [1,2,2,4,6]
nums = [1,2,2,3,1]
nums = [1]
nums = [1,2]
nums = [1,2,2,3,1]
nums = [1,2,2,3,1,4,2]
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        dict2 = {}
        dict3 = {}
        # min1 = len(nums)
        list1 = []
        repeat = False
        max_count = 0
        if len(nums) == 1:
            return 1
        for i, num in enumerate(nums):
        # for  i in nums:
        #     print("i =",i,"num =",num)
            if num in dict1:
                # print(type(dict[num]))
                repeat = True
                dict1[num] += 1
                dict3[num] = i - dict2[num] + 1
            else:
                dict1[num] = 1
            # if num not in dict2:
                dict2[num] = i
            # if num in dict3:
        if not repeat:
            return 1

        for k,v in dict1.items():
            if v > max_count:
                max_count = v
                list1 = [k]
            elif v == max_count:
                list1.append(k)

        # print(dict1)
        # print(dict2)
        # print(dict3)
        # print(list1)

        length = 50000
        for i in list1:
            if dict3[i] < length:
                length = dict3[i]
        return length


print(nums)
a = Solution()
q = a.findShortestSubArray(nums)
print("q =",q)