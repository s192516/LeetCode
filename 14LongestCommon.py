#-*- coding:utf-8 -*-
#@Date   : 2018/8/30
#@Author : huali
#@File   : 14LongestCommon.py
# strs = ["flower","flow","flight",]
strs = ["aca","cba"]

def mergePrefix(strs):
    start = 0
    end =len(strs)-1
    tempStr = ""
    helperMergePrefix(strs,start,end,tempStr)

    if len(strs)>0:
        return strs[0]
    else:
        return ""
def helperMergePrefix(strs,start,end,tempStr):
    if(start < end):
        middle =(start+end)//2
        helperMergePrefix(strs,start,middle,tempStr)
        helperMergePrefix(strs,middle+1,end,tempStr)
        merge(strs,start,end,tempStr)
    # return a
    #这里如果return a 在if 外面就不能访问a,如果在 if 里面 当不执行if判断时候
    #这里的return 就无法执行,将会返回 None而不是""

def merge(strs,start,end,tempStr):


    for i in range(len(strs[start])):
        try:
            if  strs[start][i]==strs[end][i]:
                tempStr +=strs[start][i]
            else:
                break
        except:
            pass

    for i in range(start,end+1):
        strs[i] = tempStr
    # return tempStr


a =mergePrefix(strs)
print(a)



# strs = ["flower","flow","flight",]
#
# class Solution:
#
#     def merge(self,strs):
#         tempStr = ""
#         tempList = []
#         len1 = len(strs)
#         if len1%2 != 0 and len1 != 1:
#             tempList.append(strs[-1])
#
#         for i in range(0, len1, 2):
#             for j in range(len(strs[i])):
#                 try:
#                     if strs[i][j] == strs[i + 1][j]:
#                         tempStr += strs[i][j]
#                     else:
#                         break
#                 except:
#                     break
#
#             if tempStr != "":
#                 tempList.append(tempStr)
#                 tempStr = ''
#             elif i != len1-1:
#
#                 return ""
#
#         strs = tempList
#         return strs
#
#     def longgestCommonPrefix(self, strs):
#         while len(strs) !=1 and strs !="":
#             strs = self.merge(strs)
#         return strs
#
# s = Solution()
# a =s.longgestCommonPrefix(strs)
#
# print(a)