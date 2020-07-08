#-*- coding:utf-8 -*-
#@Date   : 2018/9/27
#@Author : suyifan
#@File   : 678. Valid Parenthesis String.py

s = "(*))*)*()"
s = "(*))"
s = "())"
s = "("
s = "((*"
s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
s = "((*"
s = ")"
s = "**((*"

s = "("
s = "(*)"

s = "*((*"
s = "(())(())(((()*()()()))()((()()(*()())))(((*)()"
s = "(**((*"
s = "((*"

s = "()"
s = "(()(())()())*((()(())))*()(*)()()(*((()((*(*))))()*()(()((()(*((()))*(((())(())))*))(()*))(()*)"
# s = "(*(***(*****"
s = "()*()(()(*()(((())()()())*))()*()(*)(((*))(())(())((*()*(()(())()*(((*(**))((())*)(((()()))(())()))"
s = "*(****(*((**(*(****"

class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count1 = 0
        # count2 = 0
        count3 = 0
        count4 = 0
        list1 = list2 = []
        for i in range(len(s)):
            if s[i] == "(":
                list1.append(i)
                if count1 == 0:
                    count4 = 0
                    list2 = []
                count1 += 1

            elif s[i] == ")":
                if count1 > 0:
                    count1 -= 1
                    list1.pop()
                elif count3 > 0:
                    count3 -= 1
                    # count4 = 0
                else:
                    return False
            else:
                count3 += 1
                if count1 !=0 :
                    count4 += 1
                    list2.append(i)



        if count1 > count4:
            return False
        elif count1 != 0:
            i = count1 - 1
            j = count4 - 1
            while i >= 0:
                if list1[i] < list2[j]:
                    j -= 1
                    i -= 1
                    continue
                else:
                    return False
            return True
        else :
            return True

print(s)
a = Solution()
q = a.checkValidString(s)
print("q = ",q)
