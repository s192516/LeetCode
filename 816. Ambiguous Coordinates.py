#-*- coding:utf-8 -*-
#@Date   : 2019/1/3
#@Author : suyifan
#@File   : 816. Ambiguous Coordinates.py

S = "(000111)" # ans = ["(0, 0.0111)","(0.001, 1.1)","(0.001, 11)","(0.0011, 1)"]
S = "(100)"
class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S[1:-1]
        stack = []
        n = len(S)
        for i in range(n-1):
            stack.append([S[:i+1],S[i+1:]])
        print(stack)

        ans = []
        while stack:
            a1,a2 = stack.pop(0)
            n1 = len(a1)
            n2 = len(a2)
            for i in range(n1):
                aa1 = self.if_valid(a1, i)  # 小数点前面有i位,i从零开始计数
                if aa1:
                    for j in range(n2):
                        aa2 = self.if_valid(a2,j)
                        if aa2:
                            str_ans = "("+aa1+", "+aa2+")"
                            ans.append(str_ans)
                        else:
                            continue
                else:
                    continue
        return ans

    def if_valid(self,str1, idx):
        if len(str1) == 1:
            return str1
        # if (idx!=len(str1)-1) and str1[-1] =="0":
        #     return False
        # if (str1[0] == "0" and idx != 0):
        #     print("yes")
        # if (idx  != len(str1) and str1[-1] == "0"):
        #     print("yew")

        if (str1[0] == "0" and idx != 0) or (idx + 1 != len(str1) and str1[-1] == "0") or int(str1) == 0 or (
                idx != 0 and int(str1[:idx + 1]) == 0):
            return False
        elif idx + 1 != len(str1):
            return str1[:idx + 1] + "." + str1[idx + 1:]
        else:
            return str1

a = Solution()
q = a.ambiguousCoordinates(S)
print("q =",q)