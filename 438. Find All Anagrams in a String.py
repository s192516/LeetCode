#-*- coding:utf-8 -*-
#@Date   : 2018/10/7
#@Author : suyifan
#@File   : 438. Find All Anagrams in a String.py

s = "cbaebabacd"
p = "abc"

# s = "baa"
# p = "aa"

s = "abcdfeabc"
p = "acb"

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return []
        rtype = []
        dict_p = {}
        # dict_s = {}
        for i in p:
            if i in dict_p:
                dict_p[i] += 1
            else:
                dict_p[i] = 1
        i = 0
        while i < len_s - len_p + 1:
        # for i in range(len_s - len_p + 1):
            if not (s[i] in dict_p):
                i += 1
                continue
            dict_s = {}

            for j in range(i, i + len_p):
                if not s[j] in dict_p:
                    i = j
                    break

                if s[j] in dict_s:
                    dict_s[s[j]] += 1
                else:
                    dict_s[s[j]] = 1
            count = 0
            for k, v in dict_s.items():
                if k in dict_p and v == dict_p[k]:
                    count += v
                # else:
                #     break
            if count == len_p:
                rtype.append(i)
                while i + len_p < len_s and s[i] == s[i + len_p]:
                    i += 1
                    rtype.append(i )
            i += 1
        return rtype



a = Solution()
q = a.findAnagrams(s,p)
print("q =",q)