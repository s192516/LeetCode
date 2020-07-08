#-*- coding:utf-8 -*-
#@Date   : 2018/8/30
#@Author : huali
#@File   : 20.validParentheses.py


s ="()[]{[}"


class Solution():
    def isValid(self,s):
        rtype = True
        dict1 ={"(":0,")":0,"{":0,"}":0,"[":0,"]":0}
        dict1 ={"(":0,"{":0,"[":0}
        dict2 ={")":"(","}":"{","]":"["}
        temp = ""

        for item in s:
            temp +=item
            if item  in dict1:
                dict1[item] += 1
            elif item in dict2:
                try:
                    dict1[dict2[item]] -=1
                    if (temp[-2] =="(" and  temp[-1]!=")")or(temp[-2]=="[" and temp[-1] !="]") or(temp[-2]=="{" and temp[-1] !="}"):
                        rtype = False
                    else:
                        temp=temp[:-2]
                except:
                    rtype =False

        if temp !="":
            rtype = False
        for key in dict1.keys():
            if dict1[key] != 0:
                rtype = False




        return rtype

ss = Solution()
print(ss.isValid(s))

