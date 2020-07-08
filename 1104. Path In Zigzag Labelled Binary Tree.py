#-*- coding:utf-8 -*-
#@Date   : 2019/7/10
#@Author : huali
#@File   : 1104. Path In Zigzag Labelled Binary Tree.py


label = 14
label = 26
class Solution:
    def pathInZigZagTree(self, label: int) -> "List[int]":
        ans = [label]
        while label != 1:
            n1 = 0
            num = label
            count = 0
            while num != 1:
                if num % 2 == 0:
                    n1 += 2 ** count
                count += 1
                num //= 2
            n1 += 2 ** count
            n1 //= 2
            label = n1
            ans.insert(0,n1)
        return ans

a = Solution()
q = a.pathInZigZagTree(label)
print(f"q = {q}")