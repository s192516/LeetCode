#-*- coding:utf-8 -*-
#@Date   : 2019/1/9
#@Author : suyifan
#@File   : 131. Palindrome Partitioning.py

s = "aab"
s = "aabbc"
class Solution:

    def __init__(self):
        self.ans = []

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.n = len(s)
        self.s = s
        self.slove(s,0,[])
        return self.ans

    def slove(self,s,idx,temp):
        if idx == self.n:
            self.ans.append(temp[:])
            return

        # n = len(s)
        start = idx
        for i in range(idx,self.n):
            end = i

            str1 = s[start:end+1]
            if str1 == str1[::-1]:
                temp.append(s[start:end+1])
                # start = end+1
                self.slove(s,i+1,temp)
            else:
                continue
            temp.pop()

        # return self.ans




    def huiwen(self,s):
        if s == s[::-1]:
            return True
        else:
            return False



a = Solution()
q = a.partition(s)
print("q =",q)