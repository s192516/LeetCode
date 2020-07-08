#-*- coding:utf-8 -*-
#@Date   : 2018/11/27
#@Author : suyifan
#@File   : 60. Permutation Sequence.py


n = 3
k = 3

n = 4
k = 9
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        list_num = [(i+1) for i in range(n)]
        list1 = [1] * n
        for i in range(1,n):
            list1[i] = list1[i-1] * (i+1)
        k -= 1
        ans = []
        for i in range(n-1,-1,-1):
            shang = k // list1[i-1]
            k = k % list1[i-1]
            ans.append(str(list_num.pop(shang)))
        print(ans)
        str1 = "".join(ans)
        return str1

a = Solution()
q = a.getPermutation(n,k)
print("q =",q)