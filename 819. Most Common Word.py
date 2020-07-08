#-*- coding:utf-8 -*-
#@Date   : 2018/10/16
#@Author : suyifan
#@File   : 819. Most Common Word.py


paragraph = "abc abc? abcd the jeff!"
banned = ["abc","abcd","jeff"]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import string

        str1 = paragraph.lower()
        list1 = str1.split()
        dict1 = {}
        # print(list1)
        # print(str1)
        import string
        for i in list1:
            # print(i)
            trantab = str.maketrans({key: None for key in string.punctuation})
            i = i.translate(trantab)
            # print(i)
            if i not in banned:
                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1

        max1 = 0
        rtype = ""
        # print(dict1)
        for k, v in dict1.items():
            if v > max1:
                rtype = k
                max1 = v

        return rtype

a = Solution()
q = a.mostCommonWord(paragraph,banned)
print("q =",q)