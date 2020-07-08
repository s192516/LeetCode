#-*- coding:utf-8 -*-
#@Date   : 2018/12/31
#@Author : suyifan
#@File   : 712. Minimum ASCII Delete Sum for Two Strings.py


# s1 = "abc"
# s2 = "cba"
# s1 = "sea"
# s2 = "eat"
#
#
s1 = "ccaccjp"
s2 = "fwosarcwge" # ans = 1399

s1 = "sjfqkfxqoditw"
s2 = "fxymelgo" # 1638
s1 = "sjfqkfxqoditw"
s2 = "f" # ans = 1327
s1 = "delete"
s2 = "leet" # ans = 403
s1 = "cccc"
s2 = "c" # ans = 297
s1 = "c"
s2 = "cccc" # ans = 297


s1 = "gqirsclhrchxsqgmpfdeploxfixowfqqubuvsupkejabcrfqgcnsauunllsfskclenkxmdyraerhfmmiwryeyqoldgxctuvsjarjvfelsglvlbnozmejncnlaqpxmbrgwayfzczvatel"

s2 ="kgievqcxvrgeyklbcidngseersbiubgdwzlraagerenyfavkdcriinaugodaoacfiasmhhoxxsnqcyfriknrjfwyfglplvodefdlbmykfgpdpzjndlrskzctfkfkwcjbibuglrjvdyfhnsgwuunpzoakyejkxczznfljimkkanlsyuhvwjitrdvktrvufgyllgjpjixotsgwjkzbdqhvzyappucwvberchznrzdqjwpvyckwbfnlulscxynfbqqkhgxxkdzawjtlncqqswfwwbvywdchnxtblboobjzkurpjutdbwaxlxkxuiaxiddntniuuvghprslmpctnokubadbbxhuezbesvgvptqbnfjpmxopjdrajectbpkszvzzjivzhlesfnzaetgvxcnrhuglvoncgsyoyucjnuedgcfdrnkhxfyhujxzvxieeevwqn"
# -------------------------------------------草稿
class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        len_s1 = len(s1)
        len_s2 = len(s2)

        dp = [[0 for i in range(len_s1+1)]for j in range(len_s2+1)]

        for i in range(len_s1):
            dp[0][i+1] = dp[0][i]+ord(s1[i])

        for i in range(len_s2):
            dp[i+1][0] = dp[i][0]+ord(s2[i])


        for i in range(len_s2):
            for j in range(len_s1):
                if s2[i] == s1[j] :
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(ord(s1[j]) + ord(s2[i]) + dp[i][j],
                                       ord(s1[j]) + dp[i + 1][j],
                                       ord(s2[i]) + dp[i][j + 1])
        return dp[len_s2][len_s1]


a = Solution()
q = a.minimumDeleteSum(s1,s2)
print("q =",q)

# ans = 0
# for i in "sjqkfxqoditw": # f
#     if i != "f":
#         ans += ord(i)
#     print(i,ans,end=" ")
# ------------------------------差一点就正确的版本
# class Solution:
#     def minimumDeleteSum(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: int
#         """
#
#         len_s1 = len(s1)
#         len_s2 = len(s2)
#
#         dp = [[0 for i in range(len_s1+1)]for j in range(len_s2+1)]
#
#         for i in range(len_s1):
#             if s1[i] != s2[0] :
#                 dp[0][i+1] = dp[0][i]+ord(s1[i])
#             else:
#                 dp[0][i+1] = dp[0][i]
#         for i in range(len_s2):
#             if s2[i] != s1[0] :
#                 dp[i+1][0] = dp[i][0]+ord(s2[i])
#             else:
#                 dp[i+1][0] = dp[i][0]
#         for i in range(len_s2):
#             for j in range(len_s1):
#                 if s2[i] != s1[j]:
#                     dp[i+1][j+1] = min(ord(s1[j])+ord(s2[i])+dp[i][j],
#                                        ord(s1[j])+dp[i+1][j],
#                                        ord(s2[i])+dp[i][j+1])
#                 else:
#                     dp[i+1][j+1] = dp[i][j]
#
#         for i in dp:
#             print(i)
#         return dp[len_s2][len_s1]
#
#
# a = Solution()
# q = a.minimumDeleteSum(s1,s2)
# print("q =",q)


  # 3   3   3   3   3   3   3
  # 3   3   3   3   3   3   3
  # 3   3   3   3   3   3   3
  # 3   3   3   3   3   3   3
  # 3   3   3   2   2   2   2
  # 3   3   3   3   3   3   3
  # 3   2   1   1   0   -1   -1
  # 4   4   4   4   4   4   4
  # 3   3   3   3   3   3   3
  # 3   3   3   3   3   3   3