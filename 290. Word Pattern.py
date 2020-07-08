#-*- coding:utf-8 -*-
#@Date   : 2018/9/9
#@Author : suyifan
#@File   : 290. Word Pattern.py


pattern = "abbc"
str = "dog cat cat pig"

pattern = "abba"
str = "dog cat cat dog"

# pattern = "abba"
# str = "dog cat cat fish"
#
# pattern = "aaaa"
# str = "dog cat cat dog"
#
# pattern = "abba"
# str = "dog dog dog dog"

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        dict1 = {}
        str1 = str.split()
        try:
            for i in range(len(pattern)):
                if pattern[i] in dict1:
                    if dict1[pattern[i]] == str1[i]:
                        pass
                    else:
                        return False
                else :
                    dict1[pattern[i]] = str1[i]
        except:
            return False

        dict1 = {}
        str1 = str.split()
        try:
            for i in range(len(str1)):
                if str1[i] in dict1:
                    if dict1[str1[i]] == pattern[i]:
                        pass
                    else:
                        return False
                else:
                    dict1[str1[i]] = pattern[i]
        except:
            return False

        return True

a = Solution()
q = a.wordPattern(pattern,str)
print("q=",q)