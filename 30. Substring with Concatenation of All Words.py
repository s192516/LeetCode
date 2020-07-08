#-*- coding:utf-8 -*-
#@Date   : 2018/11/30
#@Author : suyifan
#@File   : 30. Substring with Concatenation of All Words.py


s = "barfoothefoobarman"
words = ["foo","bar"]

# s = "barfoobar"
# words = ["foo","bar"]

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        dict1 = {}
        for i in words:
            dict1[i] = dict1.get(i,0) + 1
        n = len(words[0])
        len_s = len(s)
        len_word = n * len(words)
        left = 0
        ans = []
        while left <= len_s - len_word:
            idx = left
            temp = {}
            while idx + n -1 < left + len_word:
                str1 = s[idx:idx+n]
                if str1 in dict1:
                    temp[str1] = temp.get(str1,0) + 1
                    idx += n
                else:
                    break
            num = 0
            for k,v in temp.items():
                if dict1[k] != v:
                    break
                else:
                    num += v
            if num == len(words):
                ans.append(left)
            left += 1
        return ans


a = Solution()
q = a.findSubstring(s,words)
print("q =",q)