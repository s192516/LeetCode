#-*- coding:utf-8 -*-
#@Date   : 2018/12/19
#@Author : suyifan
#@File   : 784. Letter Case Permutation.py



S = "a1b2"
class Solution:
    '''
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
    '''

    def letterCasePermutation(self,S):
        if not S:
            return []
        S = S.lower()
        ans = []
        cur = ""
        ans = self.slove(S, cur, ans)
        return ans

    def slove(self,s, cur, ans):
        if not s:
            ans.append(cur)
            return ans
        
        q = s[0]
        if q.isdigit():
            cur += q
            self.slove(s[1:],cur,ans)
        else:
            for i in [q,chr(ord(q)-32)]:
                cur += i
                self.slove(s[1:],cur,ans)
                cur = cur[:-1]
        return ans


a = Solution()
q = a.letterCasePermutation(S)
print("q =",q)

