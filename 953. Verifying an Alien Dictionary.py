#-*- coding:utf-8 -*-
#@Date   : 2018/12/9
#@Author : suyifan
#@File   : 953. Verifying an Alien Dictionary.py



order = "hlabcdefgijkmnopqrstuvwxyz"

order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["word","world","row"]

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"


words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"


words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"

class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dict1 = dict()
        for i,num in enumerate( order):
            dict1[num] = i +1

        n = len(words)
        yes = False
        for i in range(n-1):
            n2 = len(words[i])
            n3 = len(words[i+1])
            n_min = min(n2,n3)
            for j in range(n_min):
                print(dict1[words[i][j]])
                if dict1[words[i][j]] > dict1[words[i+1][j]]:
                    return False
                elif dict1[words[i][j]] == dict1[words[i+1][j]]:
                    continue
                else:
                    yes = True
                    break
            if n3 < n2 and not yes:
                return False
        return True




a = Solution()
q = a.isAlienSorted(words,order)
print("q =",q)