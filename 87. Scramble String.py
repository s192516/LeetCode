#-*- coding:utf-8 -*-
#@Date   : 2018/12/12
#@Author : suyifan
#@File   : 87. Scramble String.py


s1 = "great"
s2 = "eatgr"


class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if (not s1 ) or (not s2):
            return False
        if s1 == s2:
            return True

        letter = [0]*26

        for i in range(len(s1)):
            letter[ord(s1[i])-ord("a")] += 1
            letter[ord(s2[i])-ord("a")] -= 1

        for i in letter:
            if i != 0:
                return False

        for i in range(len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:] , s2[i:]):
                return True

            if self.isScramble(s1[:i],s2[len(s1)-i:]) and self.isScramble(s1[i:] ,s2[:len(s1)-i] ):
                return True

        return False


a = Solution()
q = a.isScramble(s1,s2)
print("q =",q)