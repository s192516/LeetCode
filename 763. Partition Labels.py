#-*- coding:utf-8 -*-
#@Date   : 2019/1/5
#@Author : suyifan
#@File   : 763. Partition Labels.py


S = "ababcbacadefegdehijhklij" # ans = [9,7,8]
S = "eccbbbbdec" #ans = [10]
S = "eaaaabaaec" #ans = [9,1]
S = "caedbdedda" #ans = [1,9]
S = "vhaagbqkaq" # ans = [1,1,8]
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dp = [None] * 26

        for i, c in enumerate(S):
            idx = ord(c) - ord("a")
            dp[idx] = i

        # print(dp)
        ans = []
        count = dp[ord(S[0])-ord("a")]
        last = -1
        for i, c in enumerate(S):
            temp = dp[ord(c) - ord("a")]
            # if i < count and temp > count:
            if i+1 != len(S) and temp > count:
                count = temp
                if temp == i:
                    if ans:

                        ans.append(count - last)
                        last = count
                    else:
                        last = count
                        ans.append(count + 1)
            elif i +1 == len(S):
                # if last != -1:
                ans.append(i-last)
                # else:
                #     ans.append(i)
            elif i == count:
                if ans:

                    ans.append(count - last)
                    last = count
                else:
                    last = count
                    ans.append(count + 1)
        return ans

a = Solution()
q = a.partitionLabels(S)
print("q =",q)