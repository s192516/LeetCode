#-*- coding:utf-8 -*-
#@Date   : 2018/9/28
#@Author : suyifan
#@File   : 500. Keyboard Row.py

words = ["hello","dad","asdf","qaz","Hello"]

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rtype = []
        dict1 = {"q": 1, "w": 1, "e": 1, "r": 1, "t": 1, "y": 1, "u": 1, "i": 1, "o": 1, "p": 1, "a": 2, "s": 2, "d": 2,
                 "f": 2, "g": 2, "h": 2, "j": 2, "k": 2, "l": 2, "z": 3, "x": 3, "c": 3, "v": 3, "b": 3, "n": 3, "m": 3,"Q": 1, "W": 1, "E": 1, "R": 1, "T": 1, "Y": 1, "U": 1, "I": 1, "O": 1, "P": 1, "A": 2, "S": 2, "D": 2,
                 "F": 2, "G": 2, "H": 2, "J": 2, "K": 2, "L": 2, "Z": 3, "X": 3, "C": 3, "V": 3, "B": 3, "N": 3, "M": 3}
        for i in words:
            j = i[0]
            count = dict1[j]
            if (self.solve(i, count, dict1)):
                rtype.append(i)
        return rtype

    def solve(self, i, count, dict1):
        for j in i:
            if dict1[j] != count:
                return False
            # else:
        return True

a = Solution()
q = a.findWords(words)
print("q = ",q)