#-*- coding:utf-8 -*-
#@Date   : 2018/12/13
#@Author : suyifan
#@File   : 93. Restore IP Addresses.py



s = "25525511135"


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        self.ans = []
        self.helper(0,s,0,"")
        return self.ans

    def helper(self,count,s,idx,sub_str):
        if count > 4:
            return
        if count == 4 and idx == len(s):
            self.ans.append(sub_str)
            return

        for i in range(1,4):
            if idx+i>len(s):
                break
            temp = s[idx:idx+i]
            if ( len(temp)>1 and temp[0] == "0") or (i ==3 and int(temp)>256):
                continue
            if count != 3:
                temp +=   "."
            # else:
            #     sub_str += temp
            # sub_str += temp
            self.helper(count+1,s,idx+i,sub_str+temp) #+temp + ("." if count != 3 else ""))
            # self.helper(count+1,s,idx+i,sub_str+temp + ("." if count != 3 else ""))#+temp+".")

# a = Solution()
# q = a.restoreIpAddresses(s)
# print("q =",q)


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = []
        self.helper(s,0,0,"")
        return self.ans

    def helper(self,s,count,idx,sub_str):
        if count > 4:
            return
        n = len(s)
        if count == 4 and idx == n:
            self.ans.append(sub_str)
            return

        for i in range(1,4):
            if idx+i>n:
                break
            temp = s[idx:idx + i]
            if (len(temp)>1 and temp[0] == "0") or (int(temp)>255):
                continue
            if count != 3:
                temp += "."
            self.helper(s,count+1,idx+i,sub_str+temp)

a = Solution()
q = a.restoreIpAddresses(s)
print("q =",q)