#-*- coding:utf-8 -*-
#@Date   : 2019/2/19
#@Author : huali
#@File   : 28. Implement strStr().py


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        def temp_array(str1):
            n = len(str1)
            if not n:
                return []
            array = [0] * n
            # for i,c in enumerate(str1):
            array[0] = 0
            left = 0
            right = 1
            while right < n:
                if str1[right] == str1[left]:
                    array[right] = left + 1
                    left += 1
                    right += 1
                else:
                    # if array[left-1] != 0 : #todo
                    if left != 0:
                        left = array[left - 1]
                    else:
                        # left = 0
                        array[right] = 0
                        right += 1
            return array

        def kmp(s, t):
            s_len = len(s)
            t_len = len(t)
            array = temp_array(s)

            left = 0
            idx_s = 0
            idx_t = 0
            while idx_t < t_len and idx_s < s_len:
                if s[idx_s] == t[idx_t]:
                    idx_s += 1
                    idx_t += 1
                else:
                    if idx_s != 0:
                        idx_s = array[idx_s - 1]
                        # idx_t = idx_s
                    else:
                        idx_t += 1
            if idx_s == s_len:
                return idx_t - s_len
            return -1

        ans = kmp(needle, haystack)
        return ans
