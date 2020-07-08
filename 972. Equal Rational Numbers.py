#-*- coding:utf-8 -*-
#@Date   : 2019/1/12
#@Author : suyifan
#@File   : 972. Equal Rational Numbers.py

S = "2.0(1)"
T = "2.01(1)"
S = "2"
T = "2.0"
S = "0.(52)"
T ="0.5(25)"

from fractions import Fraction
class Solution:

    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if ("(" not in S) and ("(" not in T) :
            return float(S) == float(T)

        if ("(" in S) and ("(" not in T):
            return False

        if ("(" not in S) and ("(" in T):
            return False

        s = self.num(S)
        t = self.num(T)
        print(s,t)
        return s == t

    def num(self, n):

        i = n.index(".")
        num_zheng = Fraction(int(n[:i]), len(n[:i]))
        n = n[i + 1:]
        i = n.index("(")
        num_fen = n[:i]
        # i = num_fen.index("(")
        num_xun = n[i + 1:-1]
        if num_fen:
            num_zheng += Fraction(int(num_fen), 10 ** len(num_fen))
        print(10 ** i * (10 ** len(num_xun))-1)
        num_zheng += Fraction(int(num_xun), 10 ** i * ((10 ** len(num_xun))-1))
        return num_zheng

a = Solution()
q = a.isRationalEqual(S,T)
print("q =",q)