#-*- coding:utf-8 -*-
#@Date   : 2018/10/22
#@Author : suyifan
#@File   : 923. 3Sum With Multiplicity.py

A = [1,1,2,2,3,3,4,4,5,5]
target = 8
class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        rtype = 0
        dict1 = {}
        for i in A:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        s = list(set(A))
        s.sort()

        # print(s,target)
        # nums_hash = {}
        # result = list()
        # for num in s:
        #     nums_hash[num] = nums_hash.get(num, 0) + 1
        # if 0 in nums_hash and nums_hash[0] >= 3:
        #     result.append([0, 0, 0])
        #
        # neg = list(filter(lambda x: x < target, nums_hash))
        # pos = list(filter(lambda x: x >= target, nums_hash))
        #
        # for i in neg:
        #     for j in pos:
        #         dif = 0 - i - j
        #         if dif in nums_hash:
        #             if dif in (i, j) and nums_hash[dif] >= 2:
        #                 result.append([i, j, dif])
        #             if dif < i or dif > j:
        #                 result.append([i, j, dif])
        # return result


        left = 0
        right = len(s) - 1

        print(dict1)
        print(s)
        while left < right:
            extra = target - s[left] - s[right]
            qq = s[left]
            qw = s[right]
            # print(extra,"extra",dict1[extra],dict1[left],dict1[right])
            if extra in dict1 and s[left] < extra < s[right]:
                rtype += dict1[extra] * dict1[s[left]] * dict1[s[right]]
                rtype = rtype % 1000000007
                left += 1
                right -= 1
            elif extra in dict1 and extra == s[left] and dict1[s[left]] > 1:
                rtype += dict1[extra] * dict1[s[left]] * dict1[s[right]]
                rtype = rtype % 1000000007
                left += 1
                right -= 1
            elif extra in dict1 and extra == s[right] and dict1[s[right]] > 1:
                rtype += dict1[s[right]] * (dict1[s[right]] - 1) // 2 * dict1[s[left]]
                rtype = rtype % 1000000007
                left += 1
                right -= 1
            elif extra > s[right]:
                left += 1
            else:
                right -= 1
        return rtype

a = Solution()
q = a.threeSumMulti(A,target)
print("q =",q)