#-*- coding:utf-8 -*-
#@Date   : 2018/12/19
#@Author : suyifan
#@File   : 784. Letter Case Permutation.py



S = "a1b2"
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        s = S.lower()
        ans = []
        def print1(s,temp):
            if not s:
                ans.append(temp)
                return
            count = 0

            # for i in s:
            i = s[0]
            if i.isdigit():
                temp += i
                count += 1
                print1(s[1:],temp)
                # continue
            else:
                for c in [i,chr(ord(i)-32)]:
                    temp += c
                    print1(s[1+count:],temp)
                    temp = temp[:-1]
                    # temp += chr(ord("a")-32)
                    # print1(s[1:],temp)
                    # temp = temp[:-1]
            # ans.append(temp)
        print1(s,"")
        return ans


a = Solution()
q = a.letterCasePermutation(S)
print("q =",q)