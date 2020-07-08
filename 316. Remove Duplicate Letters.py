#-*- coding:utf-8 -*-
#@Date   : 2019/1/2
#@Author : suyifan
#@File   : 316. Remove Duplicate Letters.py


s = "cabcdcac"
s = "cabcdcbc"
s = "cbacdcbc"

# s = "abacb" # ans = abc

class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [0] * 26
        for i in s:
            dp[ord(i)-ord("a")] += 1


        stack = []
        set1 = set()
        for i in s:
            if i not in set1:
                while set1 and stack[-1] > i and dp[ord(stack[-1])-ord("a")] :#and
                    set1.remove(stack.pop())
                stack.append(i)
                set1.add(i)
            dp[ord(i)-ord("a")] -= 1


        return "".join(stack)


a = Solution()
q = a.removeDuplicateLetters(s)
print("q =",q)