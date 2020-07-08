#-*- coding:utf-8 -*-
#@Date   : 2018/10/14
#@Author : suyifan
#@File   : 696. Count Binary Substrings.py



s = "101010010011110001111"
# s = "110011"

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        len1 = len(s)
        rtype = 0
        i = 0
        front = 0
        behind = 0
        while i < len1:
            if s[i] == s[0]:
                front += 1
            else:
                break
            i += 1
        print("#28 front =",front)

        while i < len1:
            temp = s[i]
            while i < len1:
                if s[i] == temp:
                    behind += 1
                else:
                    rtype += min(front, behind)
                    front = behind
                    behind = 0
                    break
                i += 1
        rtype += min(front,behind)


        return rtype
print(s)
a = Solution()
q = a.countBinarySubstrings(s)
print("q = ",q)