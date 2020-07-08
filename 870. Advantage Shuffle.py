#-*- coding:utf-8 -*-
#@Date   : 2018/10/21
#@Author : suyifan
#@File   : 870. Advantage Shuffle.py



A = [2,7,11,15]
B = [1,10,4,11]
A = [1,3,5,7,5]
B = [2,4,6,8,10]

A = [5,4,3,2,1]
B = [5,4,3,2,1]
A = [5621,1743,5532,3549,9581]
B = [913,9787,4121,5039,1481]

A = [2,0,4,1,2]
B = [1,3,0,0,2]


class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        import collections

        a = sorted(A)
        b = sorted(B)

        b_dict = collections.defaultdict(list)
        for i, num in enumerate(B):
            b_dict[num].append(i)

        n = len(A)
        left = 0
        ans = [None] * n
        remaining = []
        for i in range(n):
            while left < n and a[left] <= b[i]:
                remaining.append(a[left])
                left += 1
            if left < n:
                ans[b_dict[b[i]].pop(0)] = a[left]
                left += 1
            else:
                break
        for i in range(n):
            if not ans[i]:
                ans[i] = remaining.pop()
        return ans

print(A)
print(B)
a = Solution()
q = a.advantageCount(A,B)
print("q =",q)
