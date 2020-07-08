#-*- coding:utf-8 -*-
#@Date   : 2019/5/17
#@Author : huali
#@File   : 413. Arithmetic Slices.py

A = [1,2,3,4,6]
# A = [1,2,3,4]
class Solution:
    def numberOfArithmeticSlices(self, A: "List[int]") -> int:
        n = len(A)
        ans = 0
        idx = 0
        while idx < n - 1:
            cha = A[idx + 1] - A[idx]
            num = -1
            for i in range(idx + 1, n):
                if A[i] - A[i - 1] == cha:
                    num += 1
                    idx = i
                else:
                    break
            ans += (num + 1) * num // 2
        return ans



a = Solution().numberOfArithmeticSlices(A)

print("a = ",a)