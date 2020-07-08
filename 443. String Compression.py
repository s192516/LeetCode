#-*- coding:utf-8 -*-
#@Date   : 2018/10/6
#@Author : suyifan
#@File   : 443. String Compression.py

chars = ["a","a","b","b","b"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# chars = ["a","a","b","b","b","c","c"]

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        temp = chars[0]
        length = len(chars)
        idx = idx_now = 0
        count = 0
        for i in range(length):
            if chars[i] == temp:
                count += 1
                continue
            else:
                # idx = i
                if count == 1:
                    chars[idx_now] = temp
                    idx_now += 1
                    # idx += 1
                else:
                    chars[idx_now] = temp
                    idx_now += 1
                    count = list(str(count))
                    print("count =",count)
                    for j in count:
                        chars[idx_now] = j
                        idx_now += 1
                temp = chars[i]

            count = 1
        if count == 1:
            chars[idx_now] = temp
            idx_now += 1
            # idx += 1
        else:
            chars[idx_now] = temp
            idx_now += 1
            count = list(str(count))
            print("count =", count)
            for j in count:
                chars[idx_now] = j
                idx_now += 1

        chars[:] = chars[:idx_now ]

        print("chars_finally = ",chars)
        return idx_now


print("chars =",chars)
a = Solution()
q = a.compress(chars)
print("q =",q)