#-*- coding:utf-8 -*-
#@Date   : 2018/9/23
#@Author : suyifan
#@File   : 844. Backspace String Compare.py

#
# S = "abc###c"
# T = "ad##c"

# class Solution:
#     def backspaceCompare(self, S, T):
#         """
#         :type S: str
#         :type T: str
#         :rtype: bool
#         """
#
#         # if len(S) != len(T):
#         #     return False
#         len_s = len(S)
#         len_t = len(T)
#         str1 = str2 = ""
#         for i in range(len_s):
#             if S[i] != "#":
#                 str1 += S[i]
#             else:
#                 str1 = str1[:-1]
#
#         for i in range(len_t):
#             if T[i] != "#":
#                 str2 += T[i]
#             else:
#
#                 str2 = str2[:-1]
#
#         if str1 == str2:
#             return True
#         else:
#             return False

# a = Solution()
# q = a.backspaceCompare(S,T)
# print("q=",q)



S = "abc###c"
T = "ad##c"

S = "ac######c"
T = "ad##c"

S= "a#c"
T = "b"

# S = "xywrrmp"
# T = "xywrrm#p"
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        len_s = len(S)
        len_t = len(T)
        count_dif1 = count_dif2 = ""
        min1 = min(len_s, len_t)
        for i in range(min1):
            if S[i] == T[i] :
                if S[i] == "#" and len(count_dif1) > 0:
                    count_dif1 = count_dif1[:-1]
                if T[i] == "#" and len(count_dif2) > 0:
                    count_dif2 = count_dif2[:-1]
                if S[i] != "#":
                    count_dif1 += S[i]
                    count_dif2 += S[i]
                    # print("lala",count_dif1,count_dif2)
            else:
                if S[i] == "#" and len(count_dif1) > 0:
                    count_dif1 = count_dif1[:-1]
                elif S[i] != "#":
                    count_dif1 += S[i]

                if T[i] == "#" and len(count_dif2) > 0:
                    count_dif2 = count_dif2[:-1]
                elif T[i] != "#":
                    count_dif2 += T[i]

        # print("alal",count_dif1,count_dif2)

        if len_s > len_t:
            for i in range(len_t, len_s):
                if S[i] == "#" and len(count_dif1) > 0:
                    count_dif1 = count_dif1[:-1]
                elif S[i] != "#":
                    count_dif1 += S[i]
        if len_s < len_t:
            for i in range(len_s, len_t):
                if T[i] == "#" and len(count_dif2) > 0:
                    count_dif2 = count_dif2[:-1]
                else:
                    count_dif2 += T[i]

        # print("alal",count_dif1,count_dif2)


        if count_dif1 == count_dif2:
            return True
        else:
            return False

print("S = ",S)
print("T = ",T)
a = Solution()
q = a.backspaceCompare(S,T)
print("q=",q)