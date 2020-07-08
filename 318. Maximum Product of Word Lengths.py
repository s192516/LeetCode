#-*- coding:utf-8 -*-
#@Date   : 2019/1/10
#@Author : suyifan
#@File   : 318. Maximum Product of Word Lengths.py


words = ["abcw","baz","foo","bar","xtfn","abcdef"]
words = ["foo","bar","xtfn","abcdef"]

class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dp = []

        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i+1):
                n = len(words[i])
                count = 0
                for c in words[i]:
                    if c not in words[j]:
                        count+=1
                if count == n:
                    ans = max(len(words[i])*len(words[j]),ans)

        return ans

a = Solution()
q = a.maxProduct(words)
print("q =",q)