#-*- coding:utf-8 -*-
#@Date   : 2018/9/15
#@Author : suyifan
#@File   : 680. Valid Palindrome II.py


s = "abcdccba"
s = "abcdcca"
# s = "aba"
s = ""
s = "a"
s = "ebcbbececabbacecbbcbe"
s = "bcbbc"
s = "bc"
s = "pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"
s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
s = "cupupucu"
s = "ccu"
print(list(s))
print(list(s[-1::-1]))
     # "ebcbbececabbacecbbcbe"
#### 操你妈啊,这次空字符串又不需要考虑了
#### 考虑bc这种情况和bcbbc这种情况

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """


        i = 0
        j = len(s)-1
        delate = False
        while i < j:
            if s[i] == s[j] :
                i += 1
                j -= 1
            elif (not delate):
                if s[i] == s[j-1] and s[i+1] == s[j] and j - i >= 4:
                    if s[i+2] == s[j - 1]:
                        i += 1
                        delate = True
                    elif s[i+1] == s[j - 2]:
                        j -= 1
                        delate = True
                    else:
                        return False
                elif s[i] == s[j-1]:
                    j = j-1
                    delate = True
                elif  s[i+1] == s[j]:
                    i = i +1
                    delate = True
                else:
                    return False
            else:
                return False
        return True




a = Solution()
q = a.validPalindrome(s)
print("q=",q)