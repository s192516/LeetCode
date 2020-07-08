#-*- coding:utf-8 -*-
#@Date   : 2018/12/23
#@Author : suyifan
#@File   : 966. Vowel Spellchecker.py

wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
class Solution:
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        import collections

        set_true = set(wordlist)

        dict_same_c = collections.defaultdict(list)
        for i in wordlist:
            dict_same_c[i.lower()].append(i)

        dict_d = collections.defaultdict(list)
        for i in wordlist:
            temp = ""
            for c in i.lower():
                if c not in ("a","e","i","o","u"):
                    temp += c
                else:
                    temp += "."
            dict_d[temp].append(i)

        ans = [None] * len(queries)
        for i,word in enumerate(queries):
            if word in  set_true:
                ans[i] = word
            elif word.lower() in dict_same_c:
                ans[i] = dict_same_c[word.lower()][0]
            elif self.change(word) in dict_d:
                ans[i] = dict_d[self.change(word)][0]
            else:
                ans[i] = ""
        return ans

    def change(self,word):
        temp = ""
        for c in word.lower():
            if c not in ("a","e","i","o","u"):
                temp += c
            else:
                temp += "."
        return temp

a = Solution()
q = a.spellchecker(wordlist,queries)
print("q =",q)