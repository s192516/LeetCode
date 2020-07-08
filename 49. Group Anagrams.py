#-*- coding:utf-8 -*-
#@Date   : 2018/10/17
#@Author : suyifan
#@File   : 49. Group Anagrams.py



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
import collections
class Solution:
    def groupAnagrams(self,strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        # print(type(ans.values()))
        return list(ans.values())

# a = Solution()
# q = a.groupAnagrams(strs)
# print("q =",q)


print("".join(sorted("eat")))