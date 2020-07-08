#-*- coding:utf-8 -*-
#@Date   : 2018/9/28
#@Author : suyifan
#@File   : 345. Reverse Vowels of a String.py


s = ",."
s = "leetcode"
s = "aheihou"

print(s)
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        left = 0
        right = len(s) - 1
        list1 = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = list(s)
        rtype = ""
        temp = ""
        while left < right:
            if s[left] in list1 and left < right:
                if s[right] in list1 and left < right:
                    rtype += s[right]
                    temp = s[left] + temp
                    left += 1
                    right -= 1
                else:

                    temp = s[right] + temp

                    right -= 1
            else:
                rtype += s[left]

                left += 1


        if left != right:
            rtype = rtype + temp
        else:
            rtype = rtype + s[left] + temp

        return rtype

a = Solution()
q = a.reverseVowels(s)
print("q=",q)