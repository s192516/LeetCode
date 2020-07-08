#-*- coding:utf-8 -*-
#@Date   : 2018/10/7
#@Author : suyifan
#@File   : 917. Reverse Only Letters.py

S = "a-bC-dEf-ghIj"
S = "Test1ng-Leet=code-Q!"
S = "7_28]"
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        left = 0
        right = len(S) - 1
        rtype = ""
        temp = ""
        while left < right:
            while left < right and (ord(S[left]) < 65 or (ord(S[left]) > 90 and ord(S[left]) < 97)):
                rtype += S[left]
                left += 1
            while left < right and (ord(S[right]) < 65 or (ord(S[right]) > 90 and ord(S[right]) < 97)):

                temp = S[right] + temp
                right -= 1


            if left != right:
                rtype += S[right]
                temp = S[left] + temp
                left += 1
                right -= 1
            # else:
            #     rtype += S[left] + temp

        if left == right:
            rtype += S[left] + temp
        else:
            rtype += temp
        return rtype
print(S)
a = Solution()
q = a.reverseOnlyLetters(S)
print("q = ",q)

print(ord("A"),ord("Z"),ord("a"),ord("z"))