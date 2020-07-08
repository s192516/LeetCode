#-*- coding:utf-8 -*-
#@Date   : 2018/10/25
#@Author : suyifan
#@File   : 139. Word Break.py

s = "leetcode"
wordDict = ["leet","code"]
s = "aaaaaaa"
wordDict = ["aaaa","aaa"]

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        left = 0
        right = len(s)

        return self.solve(s, wordDict, left, right)

    def solve(self, s, wordDict, left, right):
        # if left = right:
        # return True

        while left < right:
            idx = left + 1
            while idx <= right:
                temp = s[left:idx]
                if s[left:idx] in wordDict:
                    left = idx
                    break
                idx += 1
            if idx != left:
                return False
        return True


a = Solution()
q = a.wordBreak(s,wordDict)
print("q =",q)