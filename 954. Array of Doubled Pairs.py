#-*- coding:utf-8 -*-
#@Date   : 2018/12/9
#@Author : suyifan
#@File   : 954. Array of Doubled Pairs.py

A = [1,2,3,2,4,6]

# A = [4,-2,2,-4]

# A = [3,1,3,6]

# A = [-2,-2,1,-2,-1,2 ]  # false

# A = [1,2,4,16,8,4] # false

# A = [4,2,4,4,2,-4,0,-2,0,4] # false

A = [-8,-4,-2,-1,0,0,1,2,4,8] # true
class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort()
        nums = A
        nums_hash = {}
        for num in nums:
            nums_hash[num] = nums_hash.get(num, 0) + 1
        neg = list(filter(lambda x: x < 0, A))
        pos = list(filter(lambda x: x >= 0, A))

        n1 = len(neg)
        n2 = len(pos)
        if n1 % 2 != 0 or n2 % 2 != 0:
            return False
        neg.reverse()

        count = 0
        i = 0
        while count < n1 // 2 and i < n1:
            if nums_hash[neg[i]] == 0:
                i += 1
                continue
            nums_hash[neg[i]] -= 1

            num = neg[i] * 2
            if num not in nums_hash:
                return False
            elif nums_hash[num] <= 0:
                return False
            else:
                nums_hash[num] -= 1
                i += 1
                count += 1

        count = 0
        i = 0
        while count < n2 // 2 and i < n2:
            if nums_hash[pos[i] ] == 0:

                i += 1
                continue
            nums_hash[pos[i]] -= 1

            num = pos[i] * 2
            if num not in nums_hash:
                return False
            elif nums_hash[num] <= 0:
                return False
            else:
                # if num == 0:
                #     nums_hash[num] -= 1
                nums_hash[num] -= 1
                i += 1
                count += 1



        return True



a = Solution()
q = a.canReorderDoubled(A)
print("q =",q)
