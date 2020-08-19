#-*- coding:utf-8 -*-
#@Date   : 2020/7/10
#@Author : huali
#@File   : 08.07. Permutation I LCCI.py

S = "qwe"


class Solution:
    def permutation(self, S) :
        if S == '': return []
        res = []
        path = ''

        def backtrack(S, path, res):
            if S == '':
                res.append(path)
                return

            for i in range(len(S)):
                cur = S[i]
                backtrack(S[:i] + S[i + 1:], path + cur, res)

        backtrack(S, path, res)

        return res



class Solution:
    def permutation(self, S) :
        if S == "":
            return []

        left = 0
        right = len(S) - 1

        return self.slove(S,left,right)
    def slove(self,s,left,right):

        if left == right:
            pass

a = Solution()
q = a.permutation(S)
print("q = ",q)

print(S[:-1])